# from Recommendation.recommendationSystemMethods import showLinearRegression
# from numpy import nan
from numpy import float64
from pandas.core.series import Series
from .recommendationSystemMethods import GetRelation
from pandas import read_csv
import pandas as pd
# from Recommendation.recommendationSystemMethods import GetRelation
# from Recommendation.recommendationSystemMethods import findDiffrentValue

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

print(GetRelation(download, rating))
