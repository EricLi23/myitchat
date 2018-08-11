import requests
import json
from base_config import *


def get_weather_byid(id):
    # id = '101010300'  # 朝阳  101272001 德阳
    url = 'http://d1.weather.com.cn/sk_2d/' + id + '.html?_=1533955388379'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Referer': 'http://www.weather.com.cn/weather1d/101272001.shtml',
        'Cookie': 'vjuids=-4b59ea6f3.1647ca58c5f.0.9f165fe4c6652; f_city=%E5%8C%97%E4%BA%AC%7C101010100%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1533952317; vjlast=1531099582.1533952317.23; UM_distinctid=16526aed86b9f9-022f8e5ec0a3fc-9393265-130980-16526aed86de0; Wa_lvt_1=1533952318; __auc=850da46016526b63374d5556115; Wa_lpvt_1=1533955228; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1533955388',
        'host': 'd1.weather.com.cn'
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    _data = r.text
    data = json.loads(_data[13:])

    if version == 'local':
        with open('./weather.js', 'w') as f:
            txt = f.write(_data)
            print("update success!")
        return data
    else:
        return data


if __name__ == '__main__':
    get_weather_byid('101272001')
