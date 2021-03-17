from pandas import read_csv
from scipy import stats
import matplotlib.pyplot as plt

def findDiffrentValue(dataframe, key:str):
    items = set()
    for value in dataframe[key]:
        items.add(value)
    return items

def countDiffrentValue(dataframe, key:str):
    items = set()
    for value in dataframe[key]:
        items.add(value)
    return len(items)

def getAllCompany(dataframe):
    companies = []
    for row in range(len(dataframe)):
        company = {
            "name":dataframe["Company (Maker-if known)"],
            "country": dataframe["Company Location"],
            "Rating": dataframe["Rating"]
        }
        if company not in companies:
            companies.append(company)
    return companies

def GetRelation(x, y):
    slope, intercept , r , p , std_err = stats.linregress(x,y)
    return r

def showLinearRegression(x, y):
    slope, intercept , r , p , std_err = stats.linregress(x,y)
    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))
    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()
