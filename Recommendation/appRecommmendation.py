# from Recommendation.recommendationSystemMethods import showLinearRegression
# from Recommendation.utils import NormalizeDataset
from appRecommendationReadData import *
from utils import *
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)


df = ReadFileData(["Installs", "Rating"])
print(df)
data= {
    "installs":df["Installs"],
    "rating":df["Rating"]
}
dataframe = pd.DataFrame(data)

print(NormalizeDatasetMethod2(df["Installs"]))

showLinearRegression(data["installs"], data["rating"])
# # print(dataframe)


# x = data["installs"]
# y = data["raiting"]

# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]


# plt.scatter(train_x, train_y)
# plt.show() 
# # mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

# # print(mymodel(5))
