import pandas as pd
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg


df = pd.read_csv("data/cars.csv")
# print(df)

features = ["Volume", "Weight"]

X = df[features]
y = df["CO2"]

dtree = tree.DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print(dtree.predict([[890,870]]))
exit()
data = tree.export_graphviz(dtree,out_file= None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()