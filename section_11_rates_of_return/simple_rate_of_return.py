import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Retrieve Proctor & Gamble data
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')

# check data is valid
print(PG.head())
print(PG.tail())

# Simple Rate of Return 
# r = (endPrice / startPrice) - 1

# calculate the daily return of PG stocks
# use the current adj close price and the preceding daily adj close price
# store the daily return values in a new column 'simple_return'
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])

# plot the daily returns
PG['simple_return'].plot(figsize=(8,5))
plt.show()

# calculate the average daily return
avg_daily_returns = PG['simple_return'].mean()
print(f"Daily Avg: {str(round(avg_daily_returns, 5) * 100)}%")

# approximate annual average return using 250 trading days
avg_annual_returns = PG['simple_return'].mean() * 250
print(f"Annual Avg: {str(round(avg_annual_returns, 5) * 100)}%")