import pandas as pd
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "demo.csv")

# # 造表
# df = pd.DataFrame({
#     "city":["BJ", "SZ", "GZ"],
#     "temp":[18, 26, 20],
# })

# df.to_csv(PATH, index=False, encoding="utf-8")
df3 = pd.read_csv(PATH, encoding="utf-8")
print(df3)

# 
print(df3.head())       # 查看前5行，用于快速确认内容
print(df3.shape)        # 返回（行数，列数）
print(df3.columns)      # 查看所有列名
df3.info()              # 查看列名、非空数量和类型（会自己输出信息）
print(df3.describe())   # 默认统计数值列（这里应只统计temp）
print(df3["city"].value_counts())       # 统计每个城市出现的次数
print(df3.isna().sum())            # 统计每列缺失值的数量、

