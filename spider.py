#导包
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import map_api
import  settings
def init_driver():
    options = webdriver.ChromeOptions()
    # 关键：禁用自动化标志，防止被链家识别为爬虫
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    return driver
#爬取单页逻辑
def parse_page(driver, url):
    data_list = []
    driver.get(url)
    time.sleep(random.uniform(3, 5))#模拟看房
    # 拿到源码
    html = driver.page_source
    # 交给 BS4 解析
    soup = BeautifulSoup(html, 'lxml')
    items = soup.select("ul.sellListContent > li.clear")
    for item in items:
        try:

            # 标题
            title_tag = item.select_one('.title a')
            title = title_tag.get_text(strip=True) if title_tag else "无标题"

            # 小区名 & 区域 (在 .positionInfo a 中，通常有两个)
            pos_links = item.select('.positionInfo a')
            community_name = pos_links[0].get_text(strip=True) if len(pos_links) > 0 else "未知小区"
            region = pos_links[1].get_text(strip=True) if len(pos_links) > 1 else "未知区域"

            # 户型 & 面积 (在 .houseInfo 中，需要切割)
            # 原始文本如: "3室2厅 | 96.12平米 | 南 | 精装"
            house_info_tag = item.select_one('.houseInfo')
            house_info_text = house_info_tag.get_text(strip=True) if house_info_tag else ""

            # 数据清洗
            info_parts = house_info_text.split('|')
            layout = "未知户型"
            area = "未知面积"
            for part in info_parts:
                txt = part.strip()
                if "室" in txt:
                    layout = txt
                elif "平米" in txt:
                    area = txt

            # 价格 (注意 CSS 选择器要有点 .totalPrice)
            price_tag = item.select_one('.totalPrice span')
            price = price_tag.get_text(strip=True) if price_tag else "0"

            # 关注人数
            follow_tag = item.select_one(".followInfo")
            follow_text = follow_tag.get_text(strip=True) if follow_tag else ""
            if "/" in follow_text:
                followers = follow_text.split('/')[0].strip()
            else:
                followers = follow_text

            # --- 2. 调用 API 获取经纬度 (核心要求) ---
            lng, lat = map_api.get_lat_lng(community_name)

            # --- 3. 封装数据 ---
            house_data = {
                "小区名字": community_name,
                "户型": layout,
                "面积": area,
                "价格(万)": price,
                "关注人数": followers,
                "经度": lng,  # API 返回数据
                "纬度": lat,  # API 返回数据
                "所在区域": region,
                "标题": title
            }
            print(house_data)

            data_list.append(house_data)
        except Exception as e:
            print(f"⚠️ 解析单条房源出错: {e}")
            continue

if __name__ == '__main__':
    driver = init_driver()
    parse_page(driver,settings.CITY_URL)
    driver.quit()












