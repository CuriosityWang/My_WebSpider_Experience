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
    driver.get("https://www.liepin.com/zhaopin/?isAnalysis=true&dqs=&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E5%BF%83%E7%90%86%E5%AD%A6&init=-1&searchType=1&headckid=313f234f94934859&compkind=&fromSearchBtn=2&sortFlag=15&ckid=313f234f94934859&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=EQONmcO8WLCO92tEJ0ikKA%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_prime&d_ckId=408e3201ed52d2f929e88afacb2b0b5b&d_curPage=19&d_pageSize=40&d_headId=408e3201ed52d2f929e88afacb2b0b5b&curPage=0")
    time.sleep(2)

    for i in range(300):

        with open("./first_page/" + str(i) + ".txt", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        ac = driver.find_element_by_link_text("下一页")
        ActionChains(driver).move_to_element(ac).click(ac).perform()
        time.sleep(random.randint(2, 3))


if __name__ == '__main__':
    main()
