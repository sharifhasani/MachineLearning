from numpy import NaN, nan
from pandas.core.series import Series
from recommendationSystemMethods import *
from scipy import stats
from pandas import read_csv
import pandas as pd

df = read_csv("data/googleplaystore.csv", float_precision='round_trip')

download = df["Installs"]
download = [i[0:-1] for i in download]
download = [i.replace(',','') for i in download]
for i in range(len(download)):
    try:    
        download[i] = int(download[i])
    except ValueError:
        download[i] = 0
        continue

rating = df["Rating"]
for i in range(len(rating)):
    try:
        rating[i] = int(rating[i])
    except ValueError:
        rating[i] = 0
        continue

appType = df["Type"]
# print(type(appType))
# x = findDiffrentValue(df,"Type")
# for i in x:
#     print(type(i))
for i in range(len(appType)):
    if type(appType[i]) is float:
        appType[i] = 0
    elif appType[i] == '0' or 'Free':
         appType[i] = 0
    elif  appType[i] == 'Paid':
         appType[i] = 1

price = df["Price"]
x = findDiffrentValue(df,"Price")
print(x)
print(GetRelation(download, rating))


