import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# r = ln( Price(t) / Price(t-1) )

# Retrieve Proctor & Gamble data
PG = wb.DataReader('PG', data_source='yahoo', start='1995-1-1')

PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print(PG['log_return'])

# plot the daily log returns
PG['log_return'].plot(figsize=(8,5))
plt.show()

# calculate the average daily return
avg_daily_returns = PG['log_return'].mean()
print(f"Daily Avg: {str(round(avg_daily_returns, 5) * 100)}%")

# approximate annual average return using 250 trading days
avg_annual_returns = PG['log_return'].mean() * 250
print(f"Annual Avg: {str(round(avg_annual_returns, 5) * 100)}%")