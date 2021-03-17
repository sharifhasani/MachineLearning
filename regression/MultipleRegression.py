from pandas import read_csv
from sklearn import linear_model
from scipy import stats

df = read_csv("data/cars.csv")
# print(df)

X= df[["Weight","Volume"]]
Y = df["CO2"]
# print(X)
# print(Y)

regr = linear_model.LinearRegression()
regr.fit(X,Y)

print(regr.coef_)

res = regr.predict([["120","500"]])
# print(res)
# print(type(res))
