#导包
import settings
import requests
import traceback

def get_lat_lng(address):
    """
        接收一个地址字符串，调用百度地图地理编码 API，返回经纬度。
        :param address: 小区名字或地址，例如 "武汉大学"
        :return: (经度 lng, 纬度 lat) 如果失败则返回 (0, 0)
    """
    if not address or not hasattr(settings, 'BAIDU_AK') or not settings.BAIDU_AK:
        print("缺失baiduAK或者地址为空")
        return 0, 0
    #准备请求参数
    base_url="https://api.map.baidu.com/geocoding/v3/"
    params={
        "address": address,
        "output": "json",
        "ak": settings.BAIDU_AK,
        "city":settings.CITY


    }
    try:
        response = requests.get(url=base_url, params=params,timeout=5)
        data=response.json()
        #解析json数据
        if data.get('status')==0:
            location=data.get('result').get('location')
            lng = location["lng"]  # 经度
            lat = location["lat"]  # 纬度
            return lng, lat
        else:
            return 0, 0


    except Exception as e:
        print(e)
        return 0,0
if __name__ == '__main__':
    print("正在测试百度地图 API...")
    test_address = "武汉大学"
    longitude, latitude = get_lat_lng(test_address)
    print(f"测试结果：{test_address}")
    print(f"经度: {longitude}")
    print(f"纬度: {latitude}")

    if longitude > 0:
        print("🎉 测试通过！你的 API配置是正确的。")
    else:
        print("😭 测试失败，请检查 settings.py 里的 AK 是否正确，或者额度是否用完。")

