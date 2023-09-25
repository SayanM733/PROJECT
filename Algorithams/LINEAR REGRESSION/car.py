import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

cars = pd.read_csv("Car_sales.csv")
# print(cars.head())
print(cars.columns)

plt.figure(figsize=(16,8))
plt.scatter(
    cars['Horsepower'],
    cars['Price in thousands'],
    c='black'
)
plt.xlabel("Horsepower")
plt.ylabel("price")
plt.show()

X = cars['Horsepower']