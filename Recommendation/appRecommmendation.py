# from Recommendation.classifier import classification
from appRecommendationReadData import *
from classifier import classification
from MLAlgorithms import *
from utils import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, r2_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
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

# Decision Tree classifier
decision_tree_model = DecisionTreeClassifier(criterion='entropy', random_state=0)
decision_tree_model.fit(installs_train, rating_train)

rating_pred_decisionTree = decision_tree_model.predict(installs_test)

# Random Forest classifier
random_forest_model = RandomForestClassifier()
random_forest_model.fit(installs_train, rating_train)

rating_pred_randomForest = random_forest_model.predict(installs_test)

# Linear Regression
linear_regression_model = LinReg(data["installs"], data["rating"])
rating_pred_linearRegression = linear_regression_model.predict(installs_test)

# Support Vector Machine Classification
svm_model = SVC(kernel="linear", random_state=0)
svm_model.fit(installs_train, rating_train)

rating_pred_svm = svm_model.predict(installs_test)

# Show Result for predict
print("Decision Tree Accuracy : ", accuracy_score(rating_pred_decisionTree, rating_test))
print("Random Forest Accuracy : ", accuracy_score(rating_pred_randomForest, rating_test))
print("Support Vector Machine Accuracy : ", accuracy_score(rating_pred_svm, rating_test))
print("Linear Regression R2_Score : ", r2_score(rating_pred_linearRegression, rating_test))

dataframe = pd.DataFrame(data)

print("Linear Regression coef : ", linear_regression_model.coef_)
print("Linear Regression intercept : ", linear_regression_model.intercept_)

while True:
    print("Enter value for predict . . . ")
    inp = input()
    print("Predict By LinearRegression : ",linear_regression_model.predict([[int(inp)]]))
    print("Predict By Decision Tree : ",decision_tree_model.predict([[int(inp)]]))
    print("Predict By Support Vector Machine : ",svm_model.predict([[int(inp)]]))
    print("Predict By Random Forest : ",random_forest_model.predict([[int(inp)]]))
