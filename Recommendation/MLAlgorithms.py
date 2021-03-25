from pandas.core.frame import DataFrame
from sklearn.linear_model import LinearRegression
from pandas.core.series import Series

def FindDiffrentValue(series:Series):
    values = set()
    for item in series:
        values.add(item)
    return len(values)

def Classifier(df:DataFrame):
    valuesLen = {}
    result = []
    for colname in df:
       valuesLen[colname] = FindDiffrentValue(df[colname])
       if valuesLen[colname] < 5:
           result.append(colname)
    return result


def LinReg(x, y):
    if type(x) is Series:
        x = x.values.reshape(-1, 1)
    else:
        x = x.reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    return model
