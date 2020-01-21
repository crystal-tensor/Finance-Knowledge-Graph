import os
import tushare as ts

# 获取股票行业信息
df = ts.get_industry_classified()
csvPath = "myJob1/stock_industry_prep.csv"
df.to_csv(csvPath, index=False)

# 获取股票概念信息
df = ts.get_concept_classified()
csvPath = "myJob1/stock_concept_prep.csv"
df.to_csv(csvPath, index=False)
#print(df)
stockList = []
data = ts.get_stock_basics()
for indexs in data.index:
    name = data.loc[indexs].values[1]
    code = str(data.loc[indexs].values[0]).zfill(6)
    stockList.append([indexs, name, code])