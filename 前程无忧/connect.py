import pandas as pd

left = pd.read_csv("./result.csv", encoding="GBK")
right = pd.read_csv("./last_result.csv", encoding="utf-8")
result = pd.concat([left, right], axis=1)
result.to_csv("./dataset.csv")
