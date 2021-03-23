import pandas as pd
import numpy as np

def NormalizeDatasetMethod1(ds:pd.Series):
    minimum = ds.min()
    maximum = ds.max()
    delta =  maximum - minimum
    result = []
    for i in range(len(ds)):
        result.append(float((ds[i] - minimum) / delta))
    return result

def NormalizeDatasetMethod2(ds:pd.Series):
    median = ds.median()
    temp = 0
    for i in ds:
        temp += abs(i - median)
    asd = temp / len(ds)

    result = []
    for i in ds :
        result.append((i - median) / asd)
    return result