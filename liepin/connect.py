import pandas as pd

left = pd.read_csv("./first_page_result.csv", encoding="utf-8")
right = pd.read_csv("./last_result.csv", encoding="utf-8")
result = pd.concat([left, right], axis=1)
result.to_csv("./liepin_dataset.csv")
