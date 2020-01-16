import re
import csv
import pandas as pd
import tushare as ts

#　创建“行业_股票”的关系
stockList = []
data = pd.read_csv("myJob1/kg/stock.csv")
for indexs in data.index:
    id = data.loc[indexs].values[0]
    code = str(data.loc[indexs].values[2]).zfill(6)
    print(id, code)
    stockList.append([id, code])
industryList = []
data = pd.read_csv("myJob1/kg/industry.csv")
for indexs in data.index:
    id = data.loc[indexs].values[0]
    industry = data.loc[indexs].values[1]
    print(id, industry)
    industryList.append([id, industry])
stock_industry_list = []
data = pd.read_csv("myJob1/stock_industry_prep.csv")
for indexs in data.index:
    stock = str(data.loc[indexs].values[0]).zfill(6)
    industry = data.loc[indexs].values[2]
    stock_id =  ""
    for j in range(len(stockList)):
        if stock == stockList[j][1]:
            stock_id = stockList[j][0]
            break
    industry_id = ""
    for j in range(len(industryList)):
        if industry == industryList[j][1]:
            industry_id = industryList[j][0]
            break
    if stock_id!="" and industry_id!="":
        stock_industry_list.append([stock_id, industry_id, "行业属于", "行业属于"])
# 存储关系
with open("myJob1/kg/news_industry.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
    for i in range(len(stock_industry_list)):
        writer.writerows([stock_industry_list[i]])
        print(i, stock_industry_list[i])
