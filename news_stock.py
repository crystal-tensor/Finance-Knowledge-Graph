import re
import csv
import pandas as pd
import tushare as ts

# 创建“概念_股票”的关系
stockList = []
data = pd.read_csv("myJob1/kg/stock.csv")
for indexs in data.index:
    id = data.loc[indexs].values[0]
    code = str(data.loc[indexs].values[2]).zfill(6)
    print(id, code)
    stockList.append([id, code])
conceptList = []
data = pd.read_csv("myJob1/kg/concept.csv")
for indexs in data.index:
    id = data.loc[indexs].values[0]
    concept = data.loc[indexs].values[1]
    print(id, concept)
    conceptList.append([id, concept])
stock_concept_list = []
data = pd.read_csv("myJob1/stock_concept_prep.csv")
for indexs in data.index:
    stock = str(data.loc[indexs].values[0]).zfill(6)
    concept = data.loc[indexs].values[2]
    stock_id =  ""
    for j in range(len(stockList)):
        if stock == stockList[j][1]:
            stock_id = stockList[j][0]
            break
    concept_id = ""
    for j in range(len(conceptList)):
        if concept == conceptList[j][1]:
            concept_id = conceptList[j][0]
            break
    if stock_id!="" and concept_id!="":
        stock_concept_list.append([stock_id, concept_id, "概念属于", "概念属于"])