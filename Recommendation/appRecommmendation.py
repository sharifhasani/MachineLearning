# from Recommendation.classifier import classification
from appRecommendationReadData import *
from classifier import classification
from MLAlgorithms import *
from utils import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, r2_score
import matplotlib.pyplot as plt
import pandas as pd

## Read Orginal file and save useful data
# df = ReadFileData(["Installs", "Rating"], "Installs", "Rating", "Price", "Type")
# WriteDataFrameToCSV(df, "puredata.csv")

# read useful data
df = ReadPureData()
data= {
    "installs":df["Installs"],
    "rating":df["Rating"]
}

installs_train, installs_test, rating_train, rating_test = train_test_split(df["Installs"], df["Rating"], test_size=0.2, random_state=0)

sc = StandardScaler()
installs_train = sc.fit_transform(installs_train.values.reshape(-1,1))
installs_test = sc.transform(installs_test.values.reshape(-1,1))

decision_tree_model = DecisionTreeClassifier(criterion='entropy', random_state=0)
decision_tree_model.fit(installs_train, rating_train)

rating_pred_decisionTree = decision_tree_model.predict(installs_test)


linear_regression_model = LinReg(data["installs"], data["rating"])
rating_pred_linearRegression = linear_regression_model.predict(installs_test)

print("Decision Tree Accuracy : ", accuracy_score(rating_pred_decisionTree, rating_test))
print("Linear Regression R2_Score : ", r2_score(rating_pred_linearRegression, rating_test))

dataframe = pd.DataFrame(data)

print("Linear Regression coef : ", linear_regression_model.coef_)
print("Linear Regression intercept : ", linear_regression_model.intercept_)

while True:
    print("Enter value for predict . . . ")
    inp = input()
    print(linear_regression_model.predict([[int(inp)]]))
    print(decision_tree_model.predict([[int(inp)]]))
