import os
import time
import json
import requests as re

if __name__ == '__main__':

    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36"
    }

    name_list = os.listdir("./SPDA_data/first_page")

    ID_list = []
    # 打开所有的第一页数据,提取每个公司的 ID
    for i in name_list:
        with open("./SPDA_data/first_page/" + i, 'r', encoding="utf-8") as fp:
            tmp_data = json.load(fp)
            for j in tmp_data["list"]:
                ID_list.append(j["ID"])

    # 开始请求网页
    for k,i in enumerate(ID_list):
        data = {
            "id": i
        }
        time.sleep(1)
        tem_json = re.post(url=url, headers=headers, data=data).json()

        # 永久储存
        path = "./SPDA_data/last_page/" + '/' + str(k) + ".json"
        with open(path, 'w', encoding="utf-8") as fp:
            json.dump(tem_json, fp, ensure_ascii=False)
        print(i, "over")
