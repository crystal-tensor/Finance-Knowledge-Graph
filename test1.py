import os
import pandas as pd
from bs4 import BeautifulSoup

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files

csvPath = "myJob1/executive_prep.csv"

list_job = []
list_sex = []
list_age = []
list_code = []
list_name = []

# 解析html
file_dir = "target"
files = file_name(file_dir)
for i in range(len(files)):
    print(i, files[i])
    if ".html" in files[i]:
        htmlPath = "target/"+files[i]
        htmlfile = open(htmlPath, 'r', encoding="gbk")
        htmlpage = htmlfile.read()

        soup = BeautifulSoup(htmlpage, "html.parser")
        code = soup.title.string.split(" ")[0].split("(")[1][:-1]

        body_tag = soup.body

        try:
            # 获取序号
            body_tag1 = body_tag.find("div", class_="m_tab_content", id="ml_001").find("tbody").find_all("th", class_="tc")
            for value in body_tag1:
                list_code.append(str(code))

            #　获取姓名
            body_tag2 = body_tag.find("div", class_="m_tab_content", id="ml_001").find("tbody").find_all("a", class_="turnto")
            for value in body_tag2:
                list_name.append(value.string)

            # 获取职务
            body_tag3 = body_tag.find("div", class_="m_tab_content", id="ml_001").find("tbody").find_all("td", class_="jobs")
            for value in body_tag3:
                list_job.append(value.string)

            # 获取性别、年龄
            body_tag4 = body_tag.find("div", class_="m_tab_content", id="ml_001").find("tbody").find_all("td", class_="intro")
            for value in body_tag4:
                if(len(value.string)>0):
                    if(len(value.string.split("  "))>1):
                        list_sex.append(value.string.split("  ")[0])
                        list_age.append(value.string.split("  ")[1])
                    else:
                        list_sex.append("无")
                        list_age.append("无")
        except:
            print(htmlPath+"————error")

print(len(list_name), len(list_sex), len(list_age), len(list_code), len(list_job))

# for i in range(len(list_code)):
#     print(list_name[i], list_sex[i], list_age[i], list_code[i], list_job[i])

# 写入csv文件
dataframe = pd.DataFrame({'高管姓名':list_name, '性别':list_sex, '年龄':list_age, '股票代码':list_code, '职位':list_job})
columns = ['高管姓名','性别','年龄','股票代码', '职位']
dataframe.to_csv(csvPath, index=False, columns=columns)