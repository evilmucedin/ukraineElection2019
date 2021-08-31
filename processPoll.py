#!/usr/bin/env python

import pandas
from sklearn.linear_model import LinearRegression, Ridge

data = pandas.read_csv("poll.csv")
print(data)
x = pandas.DataFrame(data, columns=["Гордость", "Надежду", "Страх", "Унижение", "Трудно сказать", "Не знаю"])
print(x)
print(x.sum(1))
y = pandas.DataFrame(data, columns=["Результат"])
print(y)
lr = Ridge(alpha=100).fit(x, y)
print(lr.coef_)
print(lr.predict(x))
