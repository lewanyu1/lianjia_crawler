# map_api.py (测试版)

def get_lat_lng(address):
    # 暂时只返回假数据，为了让 spider.py 能跑通
    print(f"[测试] 假装在查地址: {address}")
    return 114.3055, 30.5928  # 随便返回两个数字 (经度, 纬度)