import time
import random
import settings
import spider
import storage

def main():
    #1.初始化浏览器
    driver = spider.init_driver()
    try:
        for page in range(1,settings.MAX_PAGES+1):
            url=f"{settings.CITY_URL}pg{page}/"
            driver.get(url)
            print(f"\n=== 正在处理第 {page} 页 ===")
            page_data = []
            for house_item in spider.parse_page(driver, url):
                # 拿到一条，先存到内存列表里
                page_data.append(house_item)
                # 可选：打印个小点点代表进度，不换行
                print(".", end="", flush=True)
            print()
            if page_data:
                print(f"第 {page} 页采集完毕，正在保存 {len(page_data)} 条数据...")
                storage.save_data(page_data)
                print("保存成功！")
            else:
                print("本页未采集到数据，可能是被反爬或已到最后一页。")

                # 翻页间隔：防止请求太快被封 IP
                # 虽然 spider 内部有 sleep，但翻页时再多歇会儿更稳
            if page < settings.MAX_PAGES:
                wait_time = random.uniform(2, 4)
                print(f"☕ 休息 {wait_time:.1f} 秒后继续下一页...")
                time.sleep(wait_time)


    except Exception as e:
        print(f"程序发生严重错误: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()