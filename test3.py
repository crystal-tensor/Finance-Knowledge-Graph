import re
import csv
import pandas as pd
import tushare as ts

# 读取“高管”实体
stockList = []
data = ts.get_stock_basics()
for indexs in data.index:
    stockList.append(indexs)
executiveList = []
data = pd.read_csv("myJob1/executive_prep.csv")
sign = 0
for indexs in data.index:
    name = data.loc[indexs].values[0]
    sex = data.loc[indexs].values[1]
    age = data.loc[indexs].values[2]
    code = str(data.loc[indexs].values[3]).zfill(6)
    job = data.loc[indexs].values[4]
    if code in stockList:
        sign = sign + 1
        executiveList.append([100000+sign, name, sex, age, code, job, "高管"])
with open("myJob1/kg/executive.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index:ID", "name", "sex", "age", "code", "job", ":LABEL"])
    for i in range(len(executiveList)):
        writer.writerows([executiveList[i]])
        print(i, executiveList[i], len(stockList))

# 创建“公司”实体
sign = 0
stockList2 = []
'''
stockList = []
data = pd.read_csv("myJob1/stock_concept_prep.csv")
for indexs in data.index:
    name = data.loc[indexs].values[1]
    code = str(data.loc[indexs].values[0]).zfill(6)
    if [name, code] not in stockList:
        stockList.append([name, code])
        stockList2.append([sign, name, code])
        sign = sign + 1
'''
data = ts.get_stock_basics()
for indexs in data.index:
    status = "normal"
    if "ST" in data.loc[indexs].values[0]:
        status = "ST"
    sign = sign + 1
    stockList2.append([200000+sign, data.loc[indexs].values[0], indexs, status, "企业"])
with open("myJob1/kg/stock.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index:ID", "name", "code", "status", ":LABEL"])
    for i in range(len(stockList2)):
        writer.writerows([stockList2[i]])
        print(i, stockList2[i])

#　创建“概念”实体
conceptList = []
data = pd.read_csv("myJob1/stock_concept_prep.csv")
for indexs in data.index:
    concept = data.loc[indexs].values[2]
    if concept not in conceptList:
        conceptList.append(concept)
with open("myJob1/kg/concept.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index:ID", "name", ":LABEL"])
    for i in range(len(conceptList)):
        writer.writerows([[300000+i+1, conceptList[i], "概念"]])
        print(i, conceptList[i])

# 创建“行业”实体
industryList = []
data = pd.read_csv("myJob1/stock_industry_prep.csv")
for indexs in data.index:
    industry = data.loc[indexs].values[2]
    if industry not in industryList:
        industryList.append(industry)
with open("myJob1/kg/industry.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index:ID", "name", ":LABEL"])
    for i in range(len(industryList)):
        writer.writerows([[400000+i+1, industryList[i], "行业"]])
        print(i, industryList[i])

# 创建”高管“和”公司“的关系
executiveList = []
codeList = []
data = pd.read_csv("myJob1/kg/executive.csv")
for indexs in data.index:
    index = data.loc[indexs].values[0]
    name = data.loc[indexs].values[1]
    code = str(data.loc[indexs].values[4]).zfill(6)
    job = data.loc[indexs].values[5]
    if code not in codeList:
        codeList.append(code)
    executiveList.append([index, name, code, job])
print("done...")
stockList = []
data = pd.read_csv("myJob1/kg/stock.csv")
for indexs in data.index:
    index = data.loc[indexs].values[0]
    name = data.loc[indexs].values[1]
    code = str(data.loc[indexs].values[2]).zfill(6)
    stockList.append([index, name, code])
print("done...")
# 双重循环
execute_stock_List = []
num = 0
for i in range(len(executiveList)):
    sign = ""
    for j in range(len(stockList)):
        if str(executiveList[i][2]) == str(stockList[j][2]):
            str1 = re.sub('"','', executiveList[i][3])
            execute_stock_List.append([executiveList[i][0], stockList[j][0], str1, "董事会成员"])
            sign = "1"
            break
    if len(sign) == 0:
        num = num + 1
        print(num, str(executiveList[i][0])+" , "+str(executiveList[i][2]), len(stockList), len(executiveList[i][2]))
print("done...")
# 存储去重后股票
with open("myJob1/kg/executive_stock.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
    for i in range(len(execute_stock_List)):
        writer.writerows([execute_stock_List[i]])
        print(i, execute_stock_List[i])

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
with open("myJob1/kg/stock_industry.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
    for i in range(len(stock_industry_list)):
        writer.writerows([stock_industry_list[i]])
        print(i, stock_industry_list[i])

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
# 存储关系
with open("myJob1/kg/stock_concept.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([":START_ID", ":END_ID", "relation", ":TYPE"])
    for i in range(len(stock_concept_list)):
        writer.writerows([stock_concept_list[i]])
        print(i, stock_concept_list[i])