import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt

# retrieve excel data
data = pd.read_excel('Housing.xlsx')
print(data[['House Price', 'House Size (sq.ft.)']])

X = data['House Size (sq.ft.)'] 	# independent variable
Y = data['House Price']				# dependent variable

plt.scatter(X,Y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft.)')
plt.show()

# Computing R squared value
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()
print(reg.summary())