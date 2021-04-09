import os
import pandas as pd
from bs4 import BeautifulSoup as BS

temp_result = {
    "Job_name": [],
    "Company": [],
    "Region": [],
    "Salary": [],
    "Edu_require": [],
    "Experience": [],
    "Url": []
}


def str_process(string):
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return string


def main():

    for j in range(103):
        # print(j, "Success")
        with open("./first_page/" + str(j) + ".txt", "r", encoding="utf-8") as f:
                text = f.read()

        soup = BS(text, "lxml")
        Job_info = soup.find_all("div", class_="job-info")
        Comp_info = soup.find_all("div", class_="company-info nohover")

        if len(Job_info) == 0:
            print(j, "No message")
        else:
            # print(j, "Success")
            for i in range(len(Job_info)):
                try:
                    # get name
                    Name_url = Job_info[i].find("h3")
                    name = str_process(Name_url["title"])
                    temp_result["Job_name"].append(name)
                except:
                    temp_result["Job_name"].append("None")

                try:
                    # get url
                    url = Name_url.find("a")["href"]
                    if len(url) < 40:
                        temp_result["Url"].append("https://www.liepin.com" + url)
                    else:
                        temp_result["Url"].append(url)
                except:
                    temp_result["Url"].append("None")


                # get company
                try:
                    com = Comp_info[i].find("p", class_="company-name")
                    com = com.find("a")
                    comp_name = com["title"]
                    comp_name = str_process(comp_name)[2:]
                    temp_result["Company"].append(comp_name)
                except:
                    temp_result["Company"].append("None")
                # get salary
                try:
                    sal = Job_info[i].find("span", class_="text-warning")
                    sal = str_process(sal.get_text())
                    sal = sal.replace("·12薪", "")
                    temp_result["Salary"].append(sal)
                except:
                    temp_result["Salary"].append("None")
                #

                # get Experience
                try:
                    exp = Job_info[i].find("span", class_=None)
                    exp = str_process(exp.get_text())
                    temp_result["Experience"].append(exp)
                except:
                    temp_result["Experience"].append("None")

                # get Edu
                try:
                    edu = Job_info[i].find("span", class_="edu")
                    edu = str_process(edu.get_text())
                    temp_result["Edu_require"].append(edu)
                except:
                    temp_result["Edu_require"].append("None")

                # get region
                try:
                    region = Job_info[i].find("a", class_="area")
                    region = str_process(region.get_text())
                    temp_result["Region"].append(region)
                except:
                    temp_result["Region"].append("None")

    result_58 = pd.DataFrame(temp_result)
    result_58.to_csv("first_page_result.csv", encoding="utf-8", index=None)


if __name__ == '__main__':
    main()
