import os
import time
import json
import requests as re

if __name__ == '__main__':

    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36"
    }

    # 创建文件夹
    dirs_1 = "./SPDA_data/first_page"
    if not os.path.exists(dirs_1):
        os.makedirs(dirs_1)

    dirs_2 = "./SPDA_data/last_page"
    if not os.path.exists(dirs_2):
        os.makedirs(dirs_2)

    for i in range(300, 373):
        params = {
            "on": "true",
            "page": i,
            "pageSize": 15,
            "productName": None,
            "conditionType": 1,
            "applyname": None,
            "applysn": None
        }

        response = re.post(url, params, headers).json()

        path = dirs_1 + '/' + str(i) + ".json"
        with open(path, 'w', encoding="utf-8") as fp:
            json.dump(response, fp, ensure_ascii=False)
        print(i, "over")
        time.sleep(1.5)
