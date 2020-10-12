import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('Housing.xlsx')

# MULTIVARIATE REGRESSION

# independent variables: "House Size (sq.ft.)" , "Number of Rooms" , "Year of Construction"
X = data[["House Size (sq.ft.)" , "Number of Rooms" , "Year of Construction"]]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
print(reg.summary())

# Perform additional regressions

# independent variables: "House Size (sq.ft.)" , "Number of Rooms"
X = data[["House Size (sq.ft.)" , "Number of Rooms"]]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
print(reg.summary())


# independent variables: "House Size (sq.ft.)" , "Year of Construction"
X = data[["House Size (sq.ft.)" , "Year of Construction"]]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
print(reg.summary())

# independent variables: "Number of Rooms" , "Year of Construction"
X = data[["Number of Rooms" , "Year of Construction"]]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
print(reg.summary())