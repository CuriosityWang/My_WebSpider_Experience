#!/usr/bin/python
# -*- coding:utf8 -*-

import pandas as pd
from bs4 import BeautifulSoup as BS

temp_result = {
    "Job_Category": [],
    "Welfare": [],
    "Require_num": [],
    "Job_description": []
}


def str_process(string):
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return string


def replace(temp):
    temp = temp.replace('\xa0', '')
    temp = temp.replace('\xae', '')
    temp = temp.replace('\xa9', '')
    return temp


def main():

    for j in range(4120):

        with open("./last_page/" + str(j) + ".txt", "r", encoding="utf-8") as f:
            text = f.read()
        soup = BS(text, "lxml")
        print(j)

        # get description
        try:
            Job_des = soup.find("div", class_="content content-word")
            Descri = str_process(Job_des.get_text())
            temp_result["Job_description"].append(Descri)
        except:
            temp_result["Job_description"].append("None")

        # get_category
        temp_result["Job_Category"].append("None")
        temp_result["Require_num"].append("None")

        # get welfare
        try:
            Wel = soup.find("ul", class_="comp-tag-list clearfix")
            Wel = Wel.find_all("li")
            welfare = [str_process(Wel[i].get_text()) for i in range(len(Wel))]
            if len(welfare) != 0:
                welfare = ','.join(welfare)
                welfare = replace(welfare)
                temp_result["Welfare"].append(welfare)
            else:
                temp_result["Welfare"].append("None")
        except:
            temp_result["Welfare"].append("None")


    last_result = pd.DataFrame(temp_result)
    last_result.to_csv("last_result.csv", encoding="utf-8", index=None)


if __name__ == '__main__':
    main()