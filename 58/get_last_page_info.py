#!/usr/bin/python
# -*- coding:utf8 -*-

import pandas as pd
from bs4 import BeautifulSoup as BS

temp_result = {
    "Require_num": [],
    "Job_description": []
}


def str_process(string):
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return string


def main():

    for j in range(1803):
        pass
        with open("./last_page/" + str(j) + ".txt", "r", encoding="utf-8") as f:
            text = f.read()

        soup = BS(text, "lxml")
        print(j)
        # get description
        try:
            Job_des = soup.find("div", class_="des")
            Descri = str_process(Job_des.get_text())
            temp_result["Job_description"].append(Descri)
        except:
            temp_result["Job_description"].append("None")

        # get require_num
        try:
            num = soup.find("span", class_="item_condition pad_left_none")
            Num =str_process(num.get_text())
            temp_result["Require_num"].append(Num)
        except:
            temp_result["Require_num"].append("None")

    last_result = pd.DataFrame(temp_result)
    last_result.to_csv("58_last_result.csv", encoding="utf-8", index=None)


if __name__ == '__main__':
    main()