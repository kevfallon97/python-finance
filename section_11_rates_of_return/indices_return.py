import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# '^...' the hat denotes index data
# GSPC -> S&P500
# IXIC -> NASDAQ
# GDAXI -> German DAX
# FTSE -> London FTSE

tickers = ['^GSPC', '^IXIC', '^GDAXI']
ind_data = pd.DataFrame()
for t in tickers:
	ind_data[t] = wb.DataReader(t, data_source='yahoo', start='1997-1-1')['Adj Close']

(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15,6))
plt.show()

ind_returns = (ind_data / ind_data.shift(1)) - 1
annual_ind_returns = ind_returns.mean() * 250
print(f"Indices Return: \n{str(round(annual_ind_returns, 5) * 100)}%")