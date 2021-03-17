from scipy import stats
from pandas import read_csv


df = read_csv("data/cars.csv")
# print(df)

x = df["Weight"]
y = df["Volume"]

slope, intercept , r , p , std_err = stats.linregress(x,y)
print(r)
