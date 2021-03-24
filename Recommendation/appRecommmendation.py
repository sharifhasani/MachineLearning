# from Recommendation.recommendationSystemMethods import showLinearRegression
# from Recommendation.utils import NormalizeDataset
from appRecommendationReadData import *
from utils import *
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
numpy.random.seed(2)

## Read Orginal file and save useful data
# df = ReadFileData(["Installs", "Rating"], "Installs", "Rating", "Price", "Type")
# WriteDataFrameToCSV(df, "puredata.csv")

# read useful data
df = ReadPureData()
data= {
    "installs":df["Installs"].values.reshape(-1,1),
    "rating":df["Rating"]
}

# dataframe = pd.DataFrame(data)
# print(NormalizeDatasetMethod2(df["Installs"]))

model = LinearRegression().fit(data["installs"], data["rating"])
print("coef : ", model.coef_)
print("intercept : ", model.intercept_)
