# settings.py

# 1. 百度地图 API 秘钥 (去百度地图开放平台申请后填在这里)
# 这是给 map_api.py 用的
BAIDU_AK = "Hz4lr486lcmR0R7W0a6fpQ2OvUlRmW1d"

# 2. 爬虫伪装头 (这是给 spider.py 用的)
# 建议先把 Cookie 留空，等会儿如果跑不通再填
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'lianjia_ssid=1a31a955-8b56-4758-9a27-7338d8f51226; lianjia_uuid=5c014ace-15ac-4e69-9c73-74c21724e0c1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219b73b038feb71-02959544964f34-1c525631-1405320-19b73b038ffea7%22%2C%22%24device_id%22%3A%2219b73b038feb71-02959544964f34-1c525631-1405320-19b73b038ffea7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; select_city=440300; crosSdkDT2019DeviceId=-thzo0j-n2uwxv-g3jrlkzt8x1x9hn-gsklpj52n; hip=1vhLuElARLeaTj0DWWue9x5Y-taiblHSW-8vFmYkIixll8iF4ZakYVbRggreYQfGWTR5QYkAv4RXudeDr7nfeFbOYW4Mz1uu39VXR8yURAjh1ts9Gm2S4gAB-V9qFHC2Cv5xkJHm8cjcXLaXyI8S50cRIX_FcnwnSpBMdjBn8xbi6j0GEkSu1uly4ek2bqaJ8uzTPUY5h9TrzKM8fmDjK4TAJlLY9XKc3Lj4Il2iZhUKRe4GGguHjtFpjNAa93OpR_dm9A%3D%3D',
    'Host': 'sz.lianjia.com',
    'Referer': 'https://sz.lianjia.com/ershoufang/pg4/',
    'Sec-Ch-Ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}

# 3. 基础 URL 配置
# 方便你修改城市，或者修改起止页码
CITY_URL = "https://sz.lianjia.com/ershoufang/"
MAX_PAGES = 10  # 比如只爬10页，不用写死在循环里
CITY="深圳"

#4.谷歌浏览器的地址
chrome_address='/Users/rulerwxe/routine/Google Chrome.app/Contents/MacOS/Google Chrome'
driver_path='/Users/rulerwxe/programming/temporory/ETL/lianjia_crawler/chromedriver-mac-arm64/chromedriver'