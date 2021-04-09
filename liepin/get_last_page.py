import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}


def str_process(string):
    string = string.replace("\t", "")
    string = string.replace("\r", "")
    return string


def main():

    data = pd.read_csv("./first_page_result.csv", encoding="utf-8", usecols=["Url"])

    for i in range(4119, 4122):

        req = requests.get(data.loc[i, "Url"], headers=headers)
        html = str_process(req.text)

        # chrome = webdriver.Chrome()
        # chrome.get(data.loc[i, "Url"])
        # time.sleep(3)
        # html = chrome.page_source

        try:
            with open("./last_page/" + str(i) + ".txt", "w", encoding="utf-8") as f:
                f.write(html)
            print(i)
        except:
            with open("./last_page/" + str(i) + ".txt", "w", encoding="utf-8") as f:
                f.write("None")
            print(i, "None")

        time.sleep(random.randint(3, 5))


if __name__ == '__main__':
    main()