import settings
import os
import csv
CSV_FILE=os.path.join(settings.SAVE_PATH, 'result.csv')
TXT_FILE=os.path.join(settings.SAVE_PATH, 'result.txt')
def ensure_dir():
    if not os.path.exists(settings.SAVE_PATH):
        os.makedirs(settings.SAVE_PATH)
def save_to_csv(data_list):
    if not data_list:
        return
    ensure_dir()
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a',encoding='utf-8-sig') as f:
        headers = data_list[0].keys()
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data_list)
    print(f"已追加 {len(data_list)} 条数据到 CSV")

def save_to_txt(data_list):
    if not data_list:
        return
    ensure_dir()
    with open(TXT_FILE, mode='a', encoding='utf-8') as f:
        for item in data_list:
            # 将字典转为字符串写入，每条数据后面加个换行符
            f.write(str(item) + "\n")

    print(f"已备份数据到 TXT")

def save_data(data_list):
    """
    同时保存 CSV 和 TXT
    """
    save_to_csv(data_list)
    save_to_txt(data_list)
if __name__ == '__main__':
    # 造一点假数据测试一下
    mock_data = [
        {"小区": "测试小区1", "价格": "100万", "经度": 114.1},
        {"小区": "测试小区2", "价格": "200万", "经度": 114.2}
    ]
    # 如果以前有文件，建议先手动删掉 output 文件夹再测
    save_data(mock_data)
    print("测试完成，请去 output 文件夹查看结果")
