import pandas as pd
import numpy as np

big = float("inf")

def KDJ_2(KDJ_2):
    if not KDJ_2 is None: gb = 0.0001
    if KDJ_2<43.028: gb= 0.020408
    if KDJ_2>= 43.028 and KDJ_2 < 63.078: gb= 6.90263
    if KDJ_2>= 63.078 and KDJ_2 < 67.891: gb= 14.43635
    if KDJ_2>= 67.891 and KDJ_2 < 71.247: gb= 11.56308
    if KDJ_2>= 71.247 and KDJ_2 < 77.165: gb= 23.43814
    if KDJ_2>= 77.165 and KDJ_2 < 82.906: gb= 22.65665
    if KDJ_2>= 82.906 and KDJ_2 < 88.605: gb= 19.58754
    if KDJ_2 >= 88.605 and KDJ_2 < big: gb = 21.320709
    return gb


def RSI(RSI):
    if not RSI is None: gb = 0.0001
    if RSI < 1.384: gb= 6.23399
    if RSI>= 1.384 and RSI < 30.405: gb= 7.864
    if RSI>= 30.405 and RSI < 99.759: gb= 11.9817
    if RSI>= 99.759 and RSI < big: gb= 0.020408
    return gb

def VAR33_1(VAR33):
    if not VAR33 is None: gb = 0.0001
    if VAR33 < 0: gb= 3.84736
    if VAR33 >= 0 and VAR33 < 1: gb= 0.020408
    if VAR33 >= 1: gb = 0.0190408
    return gb


def VAR35_1(VAR35):
    if not VAR35 is None: gb = 0.0001
    if VAR35 < 77319.0: gb= 24.5021
    if VAR35>= 77319.0 and VAR35 < 106120.0: gb= 24.13250
    if VAR35>= 106120.0 and VAR35 < 163609: gb= 14.6890
    if VAR35>= 163609 and VAR35 < 219444: gb= 17.6607
    if VAR35>= 219444 and VAR35 < 329607.0: gb= 4.4077
    if VAR35>= 329607.0 and VAR35 < 1491059: gb= 4.67171
    if VAR35>= 1491059 and VAR35 < 2147483647: gb= 0.02040
    if VAR35>= 2147483647 and VAR35 < big: gb= 0.019
    return gb


def VAR36_1(VAR36):
    if not VAR36 is None: gb = 0.0001
    if VAR36 < 8779.51  : gb= 4.2437
    if VAR36>= 8779.51  and VAR36 < 12446.86 : gb= 2.7942
    if VAR36>= 12446.86  and VAR36 < 16709.87  : gb= 7.9176
    if VAR36>= 16709.87  and VAR36 < 22351.1 : gb= 11.7639
    if VAR36>= 22351.1  and VAR36 < 29362.59 : gb= 5.9812
    if VAR36>= 29362.59  and VAR36 < 43957.96 : gb= 1.15117
    if VAR36>= 43957.96 and VAR36 < 68756.27: gb= 4.7812
    if VAR36>= 68756.27  and VAR36 < 106871.38 : gb= 4.8037
    if VAR36>= 106871.38  and VAR36 < big : gb= 0.0204
    return gb


def VAR37_1(VAR37):
    if not VAR37 is None: gb = 0.020408
    if VAR37 < big: gb= 2.11007
    return gb


def VAR38_1(VAR38):
    if not VAR38 is None: gb = 1.70545
    if VAR38 < 0  : gb= 5.92976
    if VAR38>= 0  and VAR38 < big: gb= 0.020408
    return gb

def VAR39_1(VAR39):
    if not VAR39 is None: gb = 0.020408
    if VAR39 < 1  : gb= 2.11007
    if VAR39 >=  1 : gb= 0.0204
    return gb


def VAR40_1(VAR40):
    if not VAR40 is None : gb= 20.6475
    if VAR40>= 0 and VAR40 < 81311 : gb= 0.02040
    if VAR40>= 81311  and VAR40 < 160720 : gb=12.9211
    if VAR40>= 160720  and VAR40 < 257176 : gb=17.0822
    if VAR40>= 257176  and VAR40 < 333971 : gb=27.4035
    if VAR40>=  333971 and VAR40 < 499427  : gb=20.2264
    if VAR40>=  499427 and VAR40 < 716185 : gb=30.3518
    if VAR40>= 716185 and VAR40 < 1039738: gb=41.2039
    if VAR40>=  1039738 and VAR40 < big : gb=34.7442
    return gb


def VAR41_1(VAR41):
    if not VAR41 is None: gb=20.0317
    if VAR41>= 0 and VAR41 < 11271.18 : gb=31.0293
    if VAR41>= 11271.18  and VAR41 < 17319.41 : gb=31.4851
    if VAR41>= 17319.41  and VAR41 < 22315.25 : gb=28.59064
    if VAR41>= 22315.25  and VAR41 < 28671.46 : gb=27.63547
    if VAR41>= 28671.46 and VAR41 < 36942.3 : gb=30.9357
    if VAR41>= 36942.3  and VAR41 < 50587.07 : gb=18.88754
    if VAR41>= 50587.07  and VAR41 < 71743.51 : gb=23.1686
    if VAR41>= 71743.51  and VAR41 < 171064 : gb=11.171407
    if VAR41>= 171064  and VAR41 < big  : gb=0.020408
    return gb


def VAR43_1(VAR43):
    if not VAR43 is None: gb = 0.0001
    if VAR43<0 : gb=6.14222
    if VAR43>= 0  and VAR43 <1: gb=0.020408
    if VAR43 >= 1: gb = 0.01925
    return gb


def VAR45_1(VAR45):
    if not VAR45 is None: gb = 0.0001
    if VAR45>= 0 and VAR45 < 72020 : gb=13.3649
    if VAR45>= 72020 and VAR45 < 131110 : gb=4.43968
    if VAR45>= 131110  and VAR45 < 205731: gb=14.18636
    if VAR45>= 205731 and VAR45 < 294651.0 : gb=11.38658
    if VAR45>= 294651 and VAR45 < 452797 : gb=17.25659
    if VAR45>= 452797 and VAR45 < 763087 : gb=18.0357
    if VAR45>= 763087 and VAR45 < big : gb=0.02040
    return gb


def VAR46_1(VAR46):
    if not VAR46 is None: gb = 0.0001
    if VAR46 < 7500.41: gb=11.21801
    if VAR46>= 7500.41  and VAR46 < 12116.53: gb=13.16524
    if VAR46>= 12116.53  and VAR46 < 20201.43: gb=9.23118
    if VAR46>= 20201.43  and VAR46 < 23772.09: gb=0.06967
    if VAR46>= 23772.09 and VAR46 < 29947.4 : gb=7.9699
    if VAR46>= 29947.4 and VAR46 < 37733.76 : gb=3.56138
    if VAR46>= 37733.76  and VAR46 < 47715.75: gb=6.6857
    if VAR46>= 47715.75 and VAR46 < 66729.84 : gb=5.4682
    if VAR46>= 66729.84 and VAR46 < 97586.22 : gb=0.020408
    if VAR46>= 97586.22  and VAR46 < 155363.81: gb=13.0273
    if VAR46 >= 155363.81 and VAR46 < big: gb = 9.8571
    return gb

def VAR48_1(VAR48):
    if not VAR48 is None: gb= 0.020408
    if VAR48<0: gb= 1.10442
    if VAR48>=0   and VAR48 <1: gb= 0.17589
    if VAR48 >= 1: gb = 0.019589
    return gb


def VAR49_1(VAR49):
    if not VAR49 is None: gb= 0.02040
    if VAR49 < 1 : gb= 0.8647
    if VAR49 >= 1: gb = 0.019
    return gb


def VAR50_1(VAR50):
    if not VAR50 is None: gb= 10.2411
    if VAR50>= 0  and VAR50 < 88923 : gb= 3.77103
    if VAR50>= 88923   and VAR50 < 130928 : gb= 2.58228
    if VAR50>= 130928  and VAR50 < 184901 : gb= 13.17023
    if VAR50>= 184901  and VAR50 < 240270 : gb= 3.9062
    if VAR50>= 240270  and VAR50 < 324552 : gb= 7.9744
    if VAR50>= 324552 and VAR50 < 501716 : gb= 0.79015
    if VAR50>= 501716  and VAR50 < 710920 : gb= 0.020408
    if VAR50>= 710920  and VAR50 < 1136161 : gb= 1.167402
    if VAR50>= 1136161  and VAR50 < big: gb= 2.73416
    return gb


def VAR51_1(VAR51):
    if not VAR51 is None: gb= 6.22334
    if VAR51>= 0  and VAR51 < 7423.08 : gb= 22.86327
    if VAR51>= 7423.08  and VAR51 < 11214.3 : gb= 15.30725
    if VAR51>= 11214.3  and VAR51 < 19171.22 : gb= 17.136336
    if VAR51>= 19171.22  and VAR51 < 25500.7 : gb= 7.82033
    if VAR51>= 25500.7  and VAR51 < 45908.92 : gb= 3.01746
    if VAR51>= 45908.92  and VAR51 < 76280.34 : gb= 4.3366
    if VAR51>= 76280.34 and VAR51 < 102100.6 : gb= 3.90378
    if VAR51>= 102100.6  and VAR51 < 165718.17 : gb=5.13207
    if VAR51>= 165718.17  and VAR51 < big : gb= 0.020408
    return gb

def VAR53_1(VAR53):
    if not VAR53 is None: gb = 0.0001
    if VAR53<0 : gb= 0.54369
    if VAR53>= 0 and VAR53 < 1: gb= 0.020408
    if VAR53 >= 1 : gb = 0.019408
    return gb


def VAR55_1(VAR55):
    if not VAR55 is None: gb = 0.0001
    if VAR55>= 0  and VAR55 < 64980 : gb=1.3912
    if VAR55>= 64980  and VAR55 < 106045 : gb=10.97048
    if VAR55>= 106045  and VAR55 < 134082 : gb=1.147016
    if VAR55>= 134082  and VAR55 < 166444 : gb=4.27181
    if VAR55>=  166444 and VAR55 < 199383 : gb=0.020408
    if VAR55>= 199383  and VAR55 < 245264 : gb=0.54963
    if VAR55>= 245264  and VAR55 < 335063 : gb=13.57916
    if VAR55>= 335063  and VAR55 < 473830 : gb=22.27843
    if VAR55>= 473830  and VAR55 < 905185 : gb=20.370161
    if VAR55>= 905185  and VAR55 < 1583630 : gb=24.81614
    if VAR55>= 1583630  and VAR55 < big : gb=35.176292
    return gb


def VAR56_1(VAR56):
    if not VAR56 is None: gb = 0.0001
    if VAR56 < 7222.94  : gb=33.01424
    if VAR56>= 7222.94  and VAR56 < 13759.4 : gb=36.35627
    if VAR56>= 13759.4  and VAR56 < 18704.85  : gb=20.1377
    if VAR56>= 18704.85  and VAR56 < 25932.25 : gb=28.41691
    if VAR56>= 25932.25  and VAR56 < 43917.25 : gb=18.19527
    if VAR56>=  43917.25 and VAR56 < 67007.26 : gb=11.99811
    if VAR56>=  67007.26 and VAR56 < 118839.54 : gb=6.55267
    if VAR56>=  118839.54 and VAR56 < big  : gb=0.020408
    return gb


def VAR58_1(VAR58):
    if not VAR58 is None: gb = 0.0001
    if VAR58<0: gb=0.020408
    if VAR58>= 0  and VAR58 < 1  : gb=2.824744
    if VAR58 >= 1: gb =0.01955
    return gb

def VAR60_1(VAR60):
    if not VAR60 is None: gb = 0.0001
    if VAR60 < 9265.39 : gb=3.93215
    if VAR60>= 9265.39  and VAR60 < 14198 : gb=0.020408
    if VAR60>= 14198  and VAR60 < 18082 : gb=6.07631
    if VAR60>= 18082  and VAR60 < 31583  : gb=7.05776
    if VAR60>= 31583  and VAR60 < 46625  : gb=9.17736
    if VAR60>= 46625  and VAR60 < 66075 : gb=1.72721
    if VAR60>= 66075 and VAR60 < 95239  : gb=4.64637
    if VAR60>= 95239  and VAR60 < 126157 : gb=0.79226
    if VAR60>= 126157  and VAR60 < 252287 : gb=10.9973
    if VAR60>= 252287 and VAR60 < big: gb=7.46181
    return gb


def VAR61_1(VAR61):
    if not VAR61 is None: gb = 0.0001
    if VAR61 < 1143.44  : gb=6.94237
    if VAR61>= 1143.44  and VAR61 < 1718.85 : gb=0.020408
    if VAR61>= 1718.85  and VAR61 < 2278.54 : gb=6.5346
    if VAR61>= 2278.54  and VAR61 < 2910.02 : gb=5.90171
    if VAR61>= 2910.02  and VAR61 < 4531.11 : gb=14.12564
    if VAR61>= 4531.11  and VAR61 < 9736.39  : gb=7.47721
    if VAR61>= 9736.39  and VAR61 < big : gb=8.79076
    return gb

#主营收入
def income1(income):
    if not income is None: gb = 0.0001
    if income < 50284: gb = 2.557202
    if income >= 50284  and income < 67710: gb = 1.54461
    if income >= 67710  and income < 84880: gb = 8.5168
    if income >= 84880  and income < 114529: gb = 0.020408
    if income >= 114529 and income < 148444: gb = 8.80206
    if income >= 148444  and income < 266865: gb = 7.00573
    if income >= 266865  and income < 647837: gb = 9.94524
    if income >= 647837  and income < 1204372: gb = 0.14144
    if income >= 1204372: gb = 6.49023
    return gb

#主营收入同比
def incomegrowthrate1(incomegrowthrate):
    if  not incomegrowthrate is None: gb = 0.0001
    if  incomegrowthrate < 3.248 : gb=4.071247
    if  incomegrowthrate>= 3.248  and  incomegrowthrate < 11.568 : gb=0.9817
    if  incomegrowthrate>= 11.568  and  incomegrowthrate < 17.018  : gb=6.95596
    if  incomegrowthrate>= 17.018  and  incomegrowthrate < 22.093 : gb=0.020408
    if  incomegrowthrate>= 22.093 and  incomegrowthrate < 41.593 : gb=2.27162
    if  incomegrowthrate>= 41.593  and  incomegrowthrate < big  : gb=7.62120
    return gb

#净利润
def revenues1(revenues):
    if not revenues is None: gb = 0.0001
    if revenues < 411 : gb=26.83916
    if revenues>= 411  and revenues < 3079 : gb=7.50711
    if revenues>= 3079  and revenues < 5152  : gb=0.020408
    if revenues>= 5152 and revenues < 7530 : gb=8.39818
    if revenues>= 7530  and revenues < 10842 : gb=10.3772
    if revenues>= 10842  and revenues < 21707 : gb=1.14736
    if revenues>= 1.14736  and revenues < 31428 : gb=7.76754
    if revenues>= 31428  and revenues < 53050 : gb=1.69234
    if revenues>= 53050  and revenues < 100060 : gb=4.03374
    if revenues>= 100060  and revenues < big: gb=12.01157
    return gb

#净利润同比
def revenuesgrowthrate1(revenuesgrowthrate):
    if not revenuesgrowthrate is None: gb = 0.0001
    if revenuesgrowthrate<0: gb=11.43988
    if revenuesgrowthrate>= 0  and revenuesgrowthrate < 7.409: gb=11.62207
    if revenuesgrowthrate>= 7.409  and revenuesgrowthrate < 18.649: gb=0.020408
    if revenuesgrowthrate>= 18.649  and revenuesgrowthrate < 39.96: gb=8.35751
    if revenuesgrowthrate>= 39.96  and revenuesgrowthrate < 170.955: gb=10.91314
    if revenuesgrowthrate>= 170.955  and revenuesgrowthrate < big: gb=8.19601
    return gb

#净资产收益率
def ROE1(ROE):
    if not ROE is None: gb=6.37555
    if ROE<0: gb=6.21541
    if ROE>=0   and ROE < 1: gb=0.020408
    if ROE >= 1 : gb = 0.01908
    return gb

#市净率
def PB_1(pb):
    if not pb is None: gb = 0.020408
    if pb < 1.28: gb = 18.8844
    if pb >= 1.28 and pb < 1.52: gb = 21.428206
    if pb >= 1.52 and pb < 1.74: gb = 16.631003
    if pb >= 1.74 and pb < 2.19: gb = 20.34075
    if pb >= 2.19 and pb < 2.68: gb = 14.47257
    if pb >= 2.68 and pb < 3.48: gb = 29.04896
    if pb >= 3.48 and pb < 5.15: gb = 27.82325
    if pb < big: gb = 37.95336
    return gb

#市盈率
def PE_1(PE):
    if not PE is None: gb=0.020408
    if PE < 1 : gb=89.73698
    if PE>= 1  and PE < 14.35 : gb=20.73637
    if PE>=14.35   and PE < 17.48  : gb=14.0666
    if PE>= 17.48  and PE <20.69  : gb=10.25078
    if PE>= 20.69  and PE < 28.93  : gb=14.3363
    if PE>=28.93   and PE < 38.85 : gb=9.7639
    if PE>= 38.85  and PE < 54.79 : gb=22.97599
    if PE>=54.79   and PE < 112.89 : gb=15.97741
    if PE < big: gb=21.648014
    return gb

#投资收益
def Investmentincome1(Investmentincome):
    if not Investmentincome is None: gb = 0.18701
    if Investmentincome < 28: gb= 1.1904
    if Investmentincome>=28   and Investmentincome <120  : gb=0.020408
    if Investmentincome>=120   and Investmentincome <287  : gb=11.9747
    if Investmentincome>= 287  and Investmentincome <709  : gb=1.61483
    if Investmentincome>= 709  and Investmentincome <2317  : gb=3.827008
    if Investmentincome>= 2317  and Investmentincome < 7014 : gb=6.2092
    if Investmentincome>=7014   and Investmentincome < big : gb=5.35745
    return gb

#每股公积金
def Persharereserve1(Persharereserve):
    if not Persharereserve is None: gb=12.91906
    if Persharereserve < 1  : gb=8.041266
    if Persharereserve>= 1  and Persharereserve <1.25  : gb=3.038358
    if Persharereserve>= 1.25  and Persharereserve <1.736 : gb=10.59354
    if Persharereserve>= 1.736  and Persharereserve < 2.001 : gb=5.60317
    if Persharereserve>= 2.001  and Persharereserve < 2.332  : gb=6.54077
    if Persharereserve>=2.332  and Persharereserve < 2.647  : gb=3.06069
    if Persharereserve>= 2.647  and Persharereserve <3.67  : gb=4.45335
    if Persharereserve>= 3.67  and Persharereserve < 4.944 : gb=4.3002
    if Persharereserve>= 4.944  and Persharereserve < big: gb=0.020408
    return gb

#每股净资产
def Netassetspershare1(Netassetspershare):
    if not Netassetspershare is None: gb = 0.0001
    if Netassetspershare <1.967  : gb=0.020408
    if Netassetspershare>= 1.967  and Netassetspershare <2.828  : gb=4.2333
    if Netassetspershare>= 2.828  and Netassetspershare <3.28  : gb=0.6359
    if Netassetspershare>= 3.28  and Netassetspershare < 4.03  : gb=7.94902
    if Netassetspershare>= 4.03  and Netassetspershare < 4.628 : gb=12.5024
    if Netassetspershare>= 4.628  and Netassetspershare < 5.389 : gb=4.53942
    if Netassetspershare>= 5.389  and Netassetspershare < 6.368 : gb=9.01132
    if Netassetspershare>= 6.368  and Netassetspershare < 9.255  : gb=19.718074
    if Netassetspershare>= 9.255  and Netassetspershare < big  : gb=31.99056
    return gb

#每股收益
def EPS1(EPS):
    if not EPS is None: gb=66.897076
    if EPS<0: gb=0.020408
    if EPS>= 0  and EPS < big : gb=101.96149
    return gb

#每股经营现金
def Operatingcashpershare1(Operatingcashpershare):
    if not Operatingcashpershare is None: gb = 0.0001
    if Operatingcashpershare<0 : gb=1.74793
    if Operatingcashpershare>= 0  and Operatingcashpershare <1: gb=3.479613
    if Operatingcashpershare>= 1  and Operatingcashpershare < big: gb=0.020408
    return gb

#流动负债
def Currentliability1(Currentliability):
    if not Currentliability is None : gb=0.020408
    if Currentliability < 17749: gb=42.657299
    if Currentliability>= 17749  and Currentliability < 41872  : gb= 31.37411
    if Currentliability>= 41872  and Currentliability < 67805 : gb=35.86446
    if Currentliability>= 67805  and Currentliability < 94403 : gb=28.40803
    if Currentliability>= 94403  and Currentliability < 118701 : gb=33.06355
    if Currentliability>= 118701   and Currentliability < 154040  : gb=22.87249
    if Currentliability>= 154040  and Currentliability < 293731  : gb=26.96313
    if Currentliability>= 293731  and Currentliability < big : gb=19.97311
    return gb

#经营现金流量
def cashflow1(cashflow):
    if not cashflow is None: gb = 0.0001
    if cashflow<1: gb=2.035205
    if cashflow >=1   and cashflow  < 5567  : gb=0.24589
    if cashflow >= 5567   and cashflow  <12232  : gb=4.45852
    if cashflow >= 12232  and cashflow  < 18996  : gb=0.020408
    if cashflow >= 18996  and cashflow  < 34002 : gb=1.02909
    if cashflow >= 34002  and cashflow  < 82981 : gb=2.18616
    if cashflow >= 82981  and cashflow  < big : gb=8.71717
    return gb

#股东权益
def stockholderequity1(stockholderequity):
    if not stockholderequity is None: gb = 0.0001
    if stockholderequity < 52676  : gb=2.19407
    if stockholderequity>= 52676  and stockholderequity <102078: gb=0.020408
    if stockholderequity>= 102078  and stockholderequity <144376: gb=8.1202
    if stockholderequity>= 144376  and stockholderequity < 181280: gb=10.86791
    if stockholderequity>= 181280  and stockholderequity <278681: gb=7.95683
    if stockholderequity>= 278681  and stockholderequity < 453098: gb=9.81188
    if stockholderequity>= 453098  and stockholderequity < 652440: gb=11.1213
    if stockholderequity>=652440  and stockholderequity <1230921: gb=11.12022
    if stockholderequity>=1230921   and stockholderequity < big  : gb=15.01879
    return gb

#股东权益比
def Shareholdersequityratio1(Shareholdersequityratio):
    if not Shareholdersequityratio is None: gb = 0.0001
    if Shareholdersequityratio < 29.101 : gb=0.020408
    if Shareholdersequityratio>= 29.101  and Shareholdersequityratio < 37.261 : gb=12.81002
    if Shareholdersequityratio>= 37.261  and Shareholdersequityratio <45.082  : gb=10.53649
    if Shareholdersequityratio>= 45.082  and Shareholdersequityratio < 53.413 : gb=5.59867
    if Shareholdersequityratio>= 53.413  and Shareholdersequityratio <60.846  : gb=7.77582
    if Shareholdersequityratio>= 60.846  and Shareholdersequityratio < 65.61 : gb=5.17068
    if Shareholdersequityratio>= 65.61  and Shareholdersequityratio < 73.516 : gb=11.43853
    if Shareholdersequityratio>= 73.516  and Shareholdersequityratio < 86.425 : gb=1.13651
    if Shareholdersequityratio>= 86.425  and Shareholdersequityratio < big : gb=6.14852
    return gb

#营业利润
def operatingprofit1(operatingprofit):
    if not operatingprofit is None: gb = 0.0001
    if operatingprofit<1: gb=12.06823
    if operatingprofit>= 1  and operatingprofit < 2177 : gb=0.0204081
    if operatingprofit>= 2177  and operatingprofit < 3880 : gb=7.51031
    if operatingprofit>= 3880  and operatingprofit < 8680 : gb=7.701602
    if operatingprofit>= 8680  and operatingprofit < 15406 : gb=15.90353
    if operatingprofit>= 15406  and operatingprofit < 48966  : gb=13.67607
    if operatingprofit>= 48966   and operatingprofit <big  : gb=23.197575
    return gb

#资本公积金
def capitalsurplus1(capitalsurplus):
    if not capitalsurplus is None: gb=0.0204081
    if capitalsurplus < 15182 : gb=11.00745
    if capitalsurplus>= 15182  and capitalsurplus < 24162 : gb=3.06527
    if capitalsurplus>= 24162  and capitalsurplus < 42580 : gb=11.183809
    if capitalsurplus>= 42580  and capitalsurplus < 63141  : gb=22.89289
    if capitalsurplus>= 63141  and capitalsurplus < 83469 : gb=10.07029
    if capitalsurplus>= 83469  and capitalsurplus < 130700 : gb=16.21322
    if capitalsurplus>= 130700  and capitalsurplus < 192784 : gb=19.32758
    if capitalsurplus>= 192784  and capitalsurplus < 437172 : gb=19.224904
    if capitalsurplus>= 437172  and capitalsurplus < big: gb=18.28482
    return gb

#销售毛利率
def grossprofitratio1(grossprofitratio):
    if not grossprofitratio is None: gb = 0.0001
    if grossprofitratio < 14.93 : gb=13.35899
    if grossprofitratio>= 14.93  and grossprofitratio < 24.901 : gb=7.53092
    if grossprofitratio>= 24.901  and grossprofitratio < 29.444  : gb=0.657776
    if grossprofitratio>= 29.444  and grossprofitratio < 34.152  : gb=9.190005
    if grossprofitratio>= 34.152  and grossprofitratio < 38.541 : gb=0.020408
    if grossprofitratio>= 38.541  and grossprofitratio < 43.684 : gb=15.0763
    if grossprofitratio>= 43.684  and grossprofitratio < 61.368  : gb=7.81706
    if grossprofitratio>= 61.368  and grossprofitratio < big  : gb=9.12169
    return gb

#长期负债
def longtermdebt1(longtermdebt):
    if not longtermdebt is None: gb = 0.0001
    if longtermdebt is None: gb=16.271027
    if longtermdebt < 1467 : gb=6.670008
    if longtermdebt>= 1467  and longtermdebt < 3329 : gb=0.020408
    if longtermdebt>= 3329  and longtermdebt < 12102 : gb=0.32268
    if longtermdebt>= 12102  and longtermdebt < 21541  : gb=3.54764
    if longtermdebt>= 21541  and longtermdebt < 60391 : gb=3.88658
    if longtermdebt>= 60391  and longtermdebt < 150453 : gb=4.770717
    if longtermdebt>= 150453  and longtermdebt <big : gb=2.40914
    return gb

#阶段成交量
def volumeoftransaction1(volumeoftransaction):
    if not volumeoftransaction is None: gb = 0.0001
    if volumeoftransaction  < 72943 : gb=0.020408
    if volumeoftransaction >= 72943  and volumeoftransaction < 99911.91 : gb=13.92472
    if volumeoftransaction >= 99911.91   and volumeoftransaction  < 141196 : gb=3.67683
    if volumeoftransaction >= 141196  and volumeoftransaction  < 213835 : gb=20.59017
    if volumeoftransaction >= 213835  and volumeoftransaction  < 276842 : gb=18.98813
    if volumeoftransaction >= 276842  and volumeoftransaction  < 346244 : gb=25.01875
    if volumeoftransaction >= 346244  and volumeoftransaction  < 471774 : gb=19.66208
    if volumeoftransaction >= 471774  and volumeoftransaction  < 989027 : gb=26.09589
    if volumeoftransaction >= 989027  and volumeoftransaction  < 1484292  : gb=23.98660
    if volumeoftransaction >= 1484292  and volumeoftransaction  < big: gb=35.2506
    return gb

#阶段成交额
def amountoftransaction1(amountoftransaction):
    if not amountoftransaction is None: gb = 0.0001
    if amountoftransaction < 7554 : gb=34.391644
    if amountoftransaction>= 7554  and amountoftransaction < 10711.1 : gb=26.6226
    if amountoftransaction>= 10711.1  and amountoftransaction < 17070.86 : gb=14.51471
    if amountoftransaction>= 17070.86  and amountoftransaction < 24375.01 : gb=22.23326
    if amountoftransaction>= 24375.01  and amountoftransaction < 44944.95: gb=15.27538
    if amountoftransaction>= 44944.95 and amountoftransaction < 85508.35 : gb=20.7352
    if amountoftransaction>= 85508.35  and amountoftransaction < 149157.36 : gb=9.90349
    if amountoftransaction>= 149157.36  and amountoftransaction < big: gb=0.020408
    return gb

#阶段涨幅
def stagerange1(stagerange):
    if not stagerange is None: gb = 0.0001
    if stagerange<0 : gb=2.79856
    if stagerange>= 0  and stagerange < 1: gb=0.020408
    if stagerange >= 1 : gb = 0.029
    return gb

