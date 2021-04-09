import pandas as pd
from bs4 import BeautifulSoup as BS

temp_result = {
    "Job_name": [],
    "Company": [],
    "Region": [],
    "Salary": [],
    "Url": []
}


def str_process(string):
    string = string.replace("\t", "")
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return string


def main():

    for j in range(117):

        with open("./first_page/" + str(j) + ".txt", "r", encoding="utf-8") as f:
            text = f.read()
        soup = BS(text, "lxml")

        Job_name = soup.find_all(class_="t1")[1:]
        Company = soup.find_all(class_="t2")[1:]
        Region = soup.find_all(class_="t3")[1:]
        Salary = soup.find_all(class_="t4")[1:]

        for i in range(len(Job_name)):
            # get url
            try:
                alist = Job_name[i].select('a')
                temp_result["Url"].append(alist[0]["href"])
            except:
                temp_result["Url"].append("None")

            # get job_name
            try:
                name = str_process(alist[0].get_text())
                temp_result["Job_name"].append(name)
            except:
                temp_result["Job_name"].append("None")

            # get salary
            try:
                sa = str_process(Salary[i].get_text())
                temp_result["Salary"].append(sa)
            except:
                temp_result["Salary"].append("None")

            # get region
            try:
                re = str_process(Region[i].get_text())
                temp_result["Region"].append(re)

            except:
                temp_result["Salary"].append("None")

            # get company
            try:
                com = str_process(Company[i].get_text())
                temp_result["Company"].append(com)
            except:
                temp_result["Company"].append("None")

        print(j, "success")

    result = pd.DataFrame(temp_result)
    result.to_csv("result.csv", encoding="GBK", index=None)


if __name__ == '__main__':
    main()