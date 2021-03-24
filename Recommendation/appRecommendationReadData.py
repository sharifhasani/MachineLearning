from numpy import NaN, nan
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from recommendationSystemMethods import *
from scipy import stats
from pandas import read_csv
import pandas as pd


def ReadPureData():
    df = read_csv("data/puredata.csv")
    return df

def WriteDataFrameToCSV(df:DataFrame, filename:str):
    df.to_csv("data/"+filename, header=True)
    pass

def ReadFileData(OrderBy:list, *labels):
    df = read_csv("data/googleplaystore.csv", float_precision='round_trip',usecols=labels)
    try:
        df["Rating"] = GetRatingSeries(df)
        df["Installs"] = GetInstallsSeries(df)
        df["Price"] = GetPriceSeries(df)
        df["Type"] = GetAppTypeSeries(df)
    except:
        pass
    return df.sort_values(by=OrderBy)

def GetInstallsSeries(df:DataFrame):
    download = df["Installs"]
    download = [i[0:-1] for i in download]
    download = [i.replace(',','') for i in download]
    for i in range(len(download)):
        try:    
            download[i] = int(download[i])
        except ValueError:
            download[i] = 0
            continue
    return download


def GetRatingSeries(df:DataFrame):
    rating = df["Rating"]
    for i in range(len(rating)):
        try:
            rating[i] = int(rating[i])
        except ValueError:
            rating[i] = 0
            continue
    return rating

def GetAppTypeSeries(df:DataFrame):
    appType = df["Type"]
    for i in range(len(appType)):
        if type(appType[i]) is float:
            appType[i] = 0
        elif appType[i] == '0' or 'Free':
            appType[i] = 0
        elif  appType[i] == 'Paid':
            appType[i] = 1
    return appType

def GetPriceSeries(df:DataFrame):
    price = df["Price"]
    for i in range(len(price)):
        if price[i] == '0' or price[i] == 0 or price[i]== "Everyone":
            price[i] = float('0')
        else :
            price[i] = float(price[i][1:-1])
    return price
