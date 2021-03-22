from appRecommendationReadData import *
import pandas as pd
df = ReadFileData()
data = {}
data["appType"] = GetAppTypeSeries(df)
data["installs"] = GetInstallsSeries(df)
data["raiting"] = GetRatingSeries(df)
data["price"] = GetPriceSeries(df)

dataframe = pd.DataFrame(data)
print(dataframe)