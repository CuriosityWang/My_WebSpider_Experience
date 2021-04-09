#!/usr/bin/python
# -*- coding:utf8 -*-

import pandas as pd
from bs4 import BeautifulSoup as BS

temp_result = {
    "Job_Category": [],
    "Welfare": [],
    "Require_num": [],
    "Edu_require": [],
    "Experience": [],
    "Job_description": []
}


def str_process(string):
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return string


def Job_describe_get(string):
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    start = string.find("职能类别")
    string = string[0:start]
    return string


def find_edu_exp_num(soup):
    soup = str(soup)
    soup = soup.replace("\xa0", "")
    soup = soup.replace("\xa9", "")
    soup = soup.replace("\xae", "")
    soup = BS(soup, "lxml", exclude_encodings="GBK")
    message = soup.find("p", class_="msg ltype")
    try:
        content = message["title"]
        content = str_process(content)
        content = content.split("|")
        if len(content) == 5:
            temp_result["Edu_require"].append(content[2])
            temp_result["Experience"].append(content[1])
            temp_result["Require_num"].append(content[3])
        elif len(content) == 4:
            temp_result["Edu_require"].append("None")
            temp_result["Experience"].append(content[1])
            temp_result["Require_num"].append(content[2])
        else:
            temp_result["Edu_require"].append("None")
            temp_result["Experience"].append("None")
            temp_result["Require_num"].append("None")
    except:
        print("Wrong")
        temp_result["Edu_require"].append("None")
        temp_result["Experience"].append("None")
        temp_result["Require_num"].append("None")


def replace(temp):
    temp = temp.replace('\xa0', '')
    temp = temp.replace('\xae', '')
    temp = temp.replace('\xa9', '')
    return temp


def main():

    for j in range(5850):
        pass
        with open("./last_page/" + str(j) + ".txt", "r", encoding="GBK") as f:
            text = f.read()
            text = text.replace('\xa0', " ")
            text = text.replace('\xae', " ")
            text = text.replace('\xa9', " ")
        soup = BS(text, "lxml", exclude_encodings="GBK")
        print(j)
        # get description
        try:
            Job_des = soup.find(class_="bmsg job_msg inbox")
            Descri = Job_describe_get(Job_des.get_text())
            Descri = replace(Descri)
            temp_result["Job_description"].append(Descri)
        except:
            temp_result["Job_description"].append("None")

        # get_category
        try:
            Cat = Job_des.find(class_="el tdn").get_text()
            Cat = str_process(Cat)
            Cat = replace(Cat)
            temp_result["Job_Category"].append(Cat)
        except:
            temp_result["Job_Category"].append("None")

        # get welfare
        try:
            Wel = soup.find_all("span", class_="sp4")
            welfare = [str_process(Wel[i].get_text()) for i in range(len(Wel))]
            if len(welfare) != 0:
                welfare = ','.join(welfare)
                welfare = replace(welfare)
                temp_result["Welfare"].append(welfare)
            else:
                temp_result["Welfare"].append("None")
        except:
            temp_result["Welfare"].append("None")

        # get exp edu num
        find_edu_exp_num(soup)

    last_result = pd.DataFrame(temp_result)
    last_result.to_csv("last_result", encoding="utf-8", index=None)


if __name__ == '__main__':
    main()