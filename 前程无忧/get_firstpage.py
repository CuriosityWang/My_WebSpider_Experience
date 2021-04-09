import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def main():

    driver = webdriver.Chrome()
    driver.get("https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25BF%2583%25E7%2590%2586%25E5%25AD%25A6,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=")
    for i in range(600):

        with open("./first_page/" + str(i) + ".txt", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        time.sleep(random.randint(1, 3))

        ac = driver.find_element_by_link_text("下一页")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    main()
