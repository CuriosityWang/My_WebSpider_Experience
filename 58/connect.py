import pandas as pd

left = pd.read_csv("./58_result.csv", encoding="utf-8")
right = pd.read_csv("./58_last_result.csv", encoding="utf-8")
result = pd.concat([left, right], axis=1)
result.to_csv("./58_dataset.csv")
