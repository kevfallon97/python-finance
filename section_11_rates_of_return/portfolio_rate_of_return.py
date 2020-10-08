import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# r = SUM OF (rate of return for a single security * weight in portfolio)

# retrieve data
tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
	mydata[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

# check data
print(mydata.info())
print(mydata.head())
print(mydata.tail())

# normalise to 100 and plot data
(mydata / mydata.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

# show data without normalisation
mydata.plot(figsize=(15,6))
plt.show()

# calculate the return of the portfolio (use simple returns)
returns = (mydata / mydata.shift(1)) - 1
annual_returns = returns.mean() * 250
# assume an equally weighted portfolio
weights = np.array([0.25, 0.25, 0.25, 0.25])
# calculate the return of the portfolio
portfolio_return_A = np.dot(annual_returns, weights)
print(f"Portfolio A Return: {str(round(portfolio_return_A, 5) * 100)}%")

# calculate the return of a second portfolio with different weights
weights_B = np.array([0.4, 0.4, 0.15, 0.05])
portfolio_return_B = np.dot(annual_returns, weights_B)
print(f"Portfolio B Return: {str(round(portfolio_return_B, 5) * 100)}%")
