import jieba
import wordcloud
import pandas as pd


def get_text():

    cat1 = ""
    cat2 = ""
    cat3 = ""
    cat4 = ""
    cat5 = ""
    cat6 = ""
    cat7 = ""

    data = pd.read_excel("./进阶数据.xlsx", usecols=["聚类结果", "Job_Category"])

    for i in range(19812):  # 19812
        print(i)
        cls = data.loc[i, "聚类结果"]
        if cls == 1:
            cat1 += data.loc[i, "Job_Category"]

        elif cls == 2:
            cat2 += data.loc[i, "Job_Category"]

        elif cls == 3:
            cat3 += data.loc[i, "Job_Category"]

        elif cls == 4:
            cat4 += data.loc[i, "Job_Category"]

        elif cls == 5:
            cat5 += data.loc[i, "Job_Category"]

        elif cls == 6:
            cat6 += data.loc[i, "Job_Category"]

        elif cls == 7:
            cat7 += data.loc[i, "Job_Category"]

    cat_all = [cat1, cat2, cat3, cat4, cat5, cat6, cat7]

    for i in range(7):
        with open("./text/" + str(i + 1) + ".txt", "w") as f:
            f.write(cat_all[i])


def main():

    # get_text()

    for i in range(6):
        try:
            with open("./text/" + str(i + 1) + ".txt", "r", encoding="GBK") as f:
                text = f.read()
        except:
            with open("./text/" + str(i + 1) + ".txt", "r", encoding="utf-8") as f:
                text = f.read()

        # jieba.del_word("岗位职责")
        # jieba.del_word("任职要求")
        # jieba.del_word("任职资格")

        del_word = ["岗位", "职责", "任职", "要求", "任职", "资格", "工作内容", "岗位职责"
                    , "任职要求", "任职资格",  "工作"]

        del_word2 = ["其他"]

        w = wordcloud.WordCloud(font_path="msyh.ttc")

        lst = jieba.lcut(text)

        lst = [i for i in lst if i not in del_word2]

        tex = "".join(lst)
        w.generate(tex)
        print(i)
        w.to_file("./职业类别云图/" + str(i+1) + ".png")


if __name__ == '__main__':
    main()