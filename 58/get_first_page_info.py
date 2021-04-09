import os
import pandas as pd
from bs4 import BeautifulSoup as BS

temp_result = {
    "Job_name": [],
    "Company": [],
    "Region": [],
    "Salary": [],
    "Job_Category": [],
    "Welfare": [],
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

    list_dir = os.listdir("last_page")

    for idx, j in enumerate(list_dir):
        try:
            with open("./last_page/" + j, "r", encoding="GBK") as f:
                text = f.read()
        except:
            with open("./last_page/" + j, "r", encoding="utf-8") as f:
                text = f.read()

        soup = BS(text, "lxml")
        All_mesg = soup.find_all("li", class_="job_item clearfix")
        if len(All_mesg) == 0:
            print(j, "No message")
        else:
            print(j, "Success")
            for i in range(len(All_mesg)):
                try:
                    # get name
                    Name_url = All_mesg[i].find(class_="job_name clearfix")
                    Name = str_process(Name_url.get_text())
                    temp_result["Job_name"].append(Name)
                except:
                    temp_result["Job_name"].append("None")

                try:
                    # get url
                    url = Name_url.find("a")["href"]
                    temp_result["Url"].append(url)
                except:
                    temp_result["Url"].append("None")

                # get company
                try:
                    com = All_mesg[i].find(class_="comp_name")
                    com = com.find("a")
                    comp_name = com["title"]
                    comp_name = str_process(comp_name)
                    temp_result["Company"].append(comp_name)
                except:
                    temp_result["Company"].append("None")

                # get salary
                try:
                    sal = All_mesg[i].find("p", class_="job_salary")
                    sal = str_process(sal.get_text())
                    temp_result["Salary"].append(sal)
                except:
                    temp_result["Salary"].append("None")

                # get welfare
                try:
                    wel = All_mesg[i].find("div", class_="job_wel clearfix")
                    wel = wel.find_all("span")
                    wel = [i.get_text() for i in wel]
                    wel = ",".join(wel)
                    wel = str_process(wel)
                    temp_result["Welfare"].append(wel)
                except:
                    temp_result["Welfare"].append("None")

                # get Experience
                try:
                    exp = All_mesg[i].find("span", class_="jingyan")
                    exp = str_process(exp.get_text())
                    temp_result["Experience"].append(exp)
                except:
                    temp_result["Experience"].append("None")

                # get cat
                try:
                    cat = All_mesg[i].find("span", class_="cate")
                    cat = str_process(cat.get_text())
                    temp_result["Job_Category"].append(cat)
                except:
                    temp_result["Job_Category"].append("None")

                # get Edu
                try:
                    edu = All_mesg[i].find("span", class_="xueli")
                    edu = str_process(edu.get_text())
                    temp_result["Edu_require"].append(edu)
                except:
                    temp_result["Edu_require"].append("None")

                # get region
                re = j.replace(".txt", "")
                temp_result["Region"].append(j)

    result_58 = pd.DataFrame(temp_result)
    result_58.to_csv("add_58_result.csv", encoding="utf-8", index=None)


if __name__ == '__main__':
    main()
