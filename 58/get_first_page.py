import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np


def str_process(string):
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return string


# def get_city_url():
#     CityUrl = {
#         "city": [],
#         "url": []
#     }
#     with open("./resources/test_html", "r", encoding="utf-8") as f:
#         text = f.read()
#     soup = BS(text, "lxml")
#     city_url = soup.find_all("a")
#
#     for i in range(len(city_url)):
#         name = city_url[i].get_text()
#         CityUrl["city"].append(str_process(name))
#
#         url = city_url[i]["href"]
#         CityUrl["url"].append("https:" + url)
#
#     city_url = pd.DataFrame(CityUrl)
#     city_url.to_csv("./city_list.csv", encoding="GBK", index=None)


def main():

    all_url = pd.read_csv("./city_list.csv", encoding="GBK")
    city_list = list(all_url['city'])

    for idx, content in enumerate(city_list): #664

        browser = webdriver.Chrome()
        browser.get(all_url.loc[idx, 'url'])   #获取源代码

        time.sleep(3)
        browser.find_element_by_id('keyword').clear()  #清空对应的文本框
        time.sleep(random.randint(1, 2))
        browser.find_element_by_id('keyword').send_keys(u'心理学')  #传入值
        time.sleep(1)
        browser.find_element_by_id('searchbtn').click()

        time.sleep(random.randint(3, 5))
        source_html = browser.page_source
        with open("./first_page/" + str(content) + '.txt', 'w', encoding="GBK") as f:
            f.write(source_html)

        browser.quit()


if __name__ == '__main__':
    main()


