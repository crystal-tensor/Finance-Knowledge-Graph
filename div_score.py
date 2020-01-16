import pandas as pd
import numpy as np
import math
import sys
sys.path.append('E:/crystal-forcase/alpha-stock')
import function
big = float("inf")



#读txt文件的代码
csv_file = 'data/20200115_utf8.txt'
f = open(csv_file, 'r', encoding=u'utf-8', errors='ignore')
df = pd.read_csv(f, sep='\t')
# df.dropna(inplace=True)
# 读csv的代码
# csv_file = 'data/newdata_stock20191203-13_standard.csv'
# f = open(csv_file, 'r', encoding=u'utf-8', errors='ignore')
# df = pd.read_csv(f)
#print(df)


#File = open("data/score.txt", "w")
File = open("data/score20200115.txt", "w", encoding=u'utf-8', errors='ignore')
File.write("id"+"," + "code" +","+ "name" +","+ "score" +"\n")

for i in range(3659):
    incomev = df.iloc[i:i + 1, 8:9].values
    incomegrowthratev = df.iloc[i:i + 1, 20:21].values
    revenuesv = df.iloc[i:i + 1, 6:7].values
    revenuesgrowthratev = df.iloc[i:i + 1, 21:22].values
    ROEv = df.iloc[i:i + 1, 11:12].values
    pb=df.iloc[i:i+1, 5:6].values
    pe=df.iloc[i:i+1, 10:11].values
    Investmentincomev = df.iloc[i:i + 1, 19:20].values
    Persharereservev = df.iloc[i:i + 1, 13:14].values
    Netassetspersharev = df.iloc[i:i + 1, 7:8].values
    EPSv = df.iloc[i:i + 1, 4:5].values
    Operatingcashpersharev = df.iloc[i:i + 1, 11:12].values
    Currentliabilityv = df.iloc[i:i + 1, 14:15].values
    cashflowv = df.iloc[i:i + 1, 18:19].values
    stockholderequityv = df.iloc[i:i + 1, 16:17].values
    Shareholdersequityratiov = df.iloc[i:i + 1, 22:23].values
    operatingprofitv = df.iloc[i:i + 1, 9:10].values
    capitalsurplusv = df.iloc[i:i + 1, 17:18].values
    grossprofitratiov = df.iloc[i:i + 1, 23:24].values
    longtermdebtv = df.iloc[i:i + 1, 15:16].values
    volumeoftransactionv = df.iloc[i:i + 1, 27:28].values
    amountoftransactionv = df.iloc[i:i + 1, 28:29].values
    stagerangev = df.iloc[i:i + 1, 25:26].values
    KDJ_v = df.iloc[i:i + 1, 60:61].values
    RSI_v = df.iloc[i:i + 1, 59:60].values
    VAR33_v = df.iloc[i:i + 1, 30:31].values
    VAR35_v = df.iloc[i:i + 1, 32:33].values
    VAR36_v = df.iloc[i:i + 1, 33:34].values
    VAR37_v = df.iloc[i:i + 1, 34:35].values
    VAR38_v=df.iloc[i:i+1, 35:36].values
    VAR39_v=df.iloc[i:i+1, 36:37].values
    VAR40_v=df.iloc[i:i+1, 37:38].values
    VAR41_v=df.iloc[i:i+1, 38:39].values
    VAR43_v=df.iloc[i:i+1, 40:41].values
    VAR45_v=df.iloc[i:i+1, 42:43].values
    VAR46_v=df.iloc[i:i+1, 43:44].values
    VAR48_v=df.iloc[i:i+1, 45:46].values
    VAR49_v = df.iloc[i:i + 1, 46:47].values
    VAR50_v = df.iloc[i:i + 1, 47:48].values
    VAR51_v = df.iloc[i:i + 1, 48:49].values
    VAR53_v = df.iloc[i:i + 1, 50:51].values
    VAR55_v = df.iloc[i:i + 1, 52:53].values
    VAR56_v = df.iloc[i:i + 1, 53:54].values
    VAR58_v = df.iloc[i:i + 1, 55:56].values
    VAR60_v = df.iloc[i:i + 1, 57:58].values
    VAR61_v = df.iloc[i:i + 1, 58:59].values

    print(i)
    #score=function.PB_1(pb)+function.PE_1(pe)
    score = function.income1(incomev) +function.incomegrowthrate1(incomegrowthratev)+function.revenues1(revenuesv) + \
            function.revenuesgrowthrate1(revenuesgrowthratev)+\
            function.ROE1(ROEv) + function.Investmentincome1(Investmentincomev) + function.Persharereserve1(Persharereservev) + \
            function.Netassetspershare1(Netassetspersharev)+\
            function.EPS1(EPSv) + function.Operatingcashpershare1(Operatingcashpersharev) + \
            function.Currentliability1(Currentliabilityv) + function.cashflow1(cashflowv)+\
            function.stockholderequity1(stockholderequityv) + function.Shareholdersequityratio1(Shareholdersequityratiov) + \
            function.operatingprofit1(operatingprofitv) + function.capitalsurplus1(capitalsurplusv)+\
            function.grossprofitratio1(grossprofitratiov) + function.longtermdebt1(longtermdebtv) + \
            function.volumeoftransaction1(volumeoftransactionv) + function.amountoftransaction1(amountoftransactionv)+\
            function.stagerange1(stagerangev) + function.KDJ_2(KDJ_v) + \
            function.PB_1(pb)+function.PE_1(pe)+ function.RSI(RSI_v) + \
            function.VAR33_1(VAR33_v)+\
            function.VAR35_1(VAR35_v) + function.VAR36_1(VAR36_v) + function.VAR37_1(VAR37_v) + function.VAR38_1(VAR38_v)+\
            function.VAR39_1(VAR39_v) + function.VAR40_1(VAR40_v) + function.VAR43_1(VAR43_v) + function.VAR45_1(VAR45_v)+\
            function.VAR46_1(VAR46_v) + function.VAR48_1(VAR48_v) + function.VAR49_1(VAR49_v) + function.VAR50_1(VAR50_v)+\
            function.VAR51_1(VAR51_v) + function.VAR53_1(VAR53_v) + function.VAR55_1(VAR55_v) + function.VAR56_1(VAR56_v)+\
            function.VAR58_1(VAR58_v) + function.VAR60_1(VAR60_v) + function.VAR61_1(VAR61_v)

    #File.write(str(df.iloc[i:i+1, 0:1].values)+"," + str(df.iloc[i:i+1, 1:2].values)+"," + "\n")
    File.write(str(i)+"," + str(df.iloc[i:i+1, 0:1].values)+"," + str(df.iloc[i:i+1, 1:2].values) +"," + str(score) +"," + "\n")

File.close()
print("ok!!!")