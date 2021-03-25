# from Recommendation.classifier import classification
from appRecommendationReadData import *
from MLAlgorithms import *
from utils import *
import matplotlib.pyplot as plt
import pandas as pd
# from Recommendation.classifier import classification
from classifier import classification

## Read Orginal file and save useful data
# df = ReadFileData(["Installs", "Rating"], "Installs", "Rating", "Price", "Type")
# WriteDataFrameToCSV(df, "puredata.csv")

# read useful data
df = ReadPureData()
data= {
    "installs":df["Installs"],
    "rating":df["Rating"]
}

dataframe = pd.DataFrame(data)
# print(NormalizeDatasetMethod2(df["Installs"]))

classifier = classification()
classifier.BinaryClassifier(df)
print(Classifier(df))
model = LinReg(data["installs"], data["rating"])
print("coef : ", model.coef_)
print("intercept : ", model.intercept_)

print(data["rating"].mean())

while True:
    inp = input()
    print(model.predict([[int(inp)]]))