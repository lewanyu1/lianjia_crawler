# settings_template.py
# ==============================================================================
# ⚠️ 使用说明：
# 1. 这个文件是给别人看的，不包含敏感数据。
# 2. 请复制这个文件，重命名为 settings.py。
# 3. 在新的 settings.py 中填入你真实的 AK、路径和 Cookie。
# ==============================================================================

import os

# 1. 百度地图 API 秘钥 (去百度地图开放平台申请后填在这里)
# 如果不填，map_api.py 会默认返回 (0,0)
BAIDU_AK = ""

# 2. 爬虫伪装头
# ⚠️ 注意：Cookie 包含个人登录隐私，千万不要提交到 Git 仓库！
# 本地运行时，如果需要登录状态，请将浏览器中的 Cookie 复制到下方引号内。
HEADERS = {


    }

# 3. 基础 URL 配置
CITY_URL = "https://sz.lianjia.com/ershoufang/"
CITY = "深圳"
MAX_PAGES = 5  # 默认测试爬取页数

# 4. 谷歌浏览器与驱动路径
# 提示：Windows 和 Mac 路径不同，建议让协作者填自己的路径
# Mac 默认 Chrome 路径示例:
# chrome_address = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_address = ''

# 驱动路径 (建议填绝对路径，或项目下的相对路径)
driver_path = ''

# 5. 存储路径
# 建议默认使用项目根目录下的 output 文件夹，兼容性更好
SAVE_PATH = "output"