import os
import re
import pandas as pd


def process_ab(ab):
    ab = ab.replace("<正>", "")
    return ab


def process_date(ab):
    ab = re.findall("\d+", ab)[0]
    return ab

if __name__ == '__main__':

    data = pd.read_excel("知网.xls")
# len(data)
    for i in range(len(data)):
        try:
            data.loc[i, "摘要"] = process_ab(data.loc[i, "摘要"])
        except:
            pass
        try:
            data.loc[i, "来源"] = process_date(data.loc[i, "来源"])
        except:
            pass
    data.to_excel("11.xlsx", index=False)