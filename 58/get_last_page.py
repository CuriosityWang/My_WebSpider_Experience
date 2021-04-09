import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}


def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BS(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def main():

    data = pd.read_csv("./58_result.csv", encoding="utf-8", usecols=["Url"])

    # url = 'http://www.xicidaili.com/nn/'
    # ip_list = get_ip_list(url, headers=headers)
    # proxies = get_random_ip(ip_list)
    proxies = {'http': 'http://120.35.201.33:9999'}

    for i in range(1635, 5922):

        # req = requests.get(data.loc[i, "Url"], headers=headers, proxies=proxies)
        # html = req.text

        chrome = webdriver.Chrome()
        chrome.get(data.loc[i, "Url"])
        time.sleep(5)
        html = chrome.page_source


        try:
            with open("./last_page/" + str(i) + ".txt", "w", encoding="utf-8") as f:
                f.write(html)
            print(i)
        except:
            with open("./last_page/" + str(i) + ".txt", "w", encoding="uft-8") as f:
                f.write("None")
            print(i, "None")

        chrome.quit()

        time.sleep(random.randint(5, 7))


if __name__ == '__main__':
    main()