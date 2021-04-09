import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}


def main():

    data = pd.read_csv("./result.csv", encoding="GBK", usecols=["Url"])

    for i in range(909, 5850):
        req = requests.get(data.loc[i, "Url"], headers=headers)
        req.encoding = "GBK"
        html = req.text
        try:
            with open("./last_page/" + str(i) + ".txt", "w", encoding="GBK") as f:
                f.write(html)
            print(i)
        except:
            with open("./last_page/" + str(i) + ".txt", "w", encoding="GBK") as f:
                f.write("None")
            print(i, "None")

        time.sleep(random.randint(2, 3))


if __name__ == '__main__':
    main()