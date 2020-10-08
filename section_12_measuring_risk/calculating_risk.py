import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# CALCULATE THE RISK OF A SECURITY

tickers = ['PG', 'BEI.DE']
sec_data = pd.DataFrame()
for t in tickers:
	sec_data[t] = wb.DataReader(t, data_source = 'yahoo', start='2007-1-1')['Adj Close']

sec_returns = np.log(sec_data / sec_data.shift(1))

# # PG
# avg_annual_return_pg = sec_returns['PG'].mean() * 250
# std_dev_pg = sec_returns['PG'].std() * 250 ** 0.5

# # BEI.DE
# avg_annual_return_bd = sec_returns['BEI.DE'].mean() * 250
# std_dev_bd = sec_returns['BEI.DE'].std() * 250 ** 0.5

print(sec_returns[['PG', 'BEI.DE']].mean() * 250)
print(sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5)

# print(sec_returns[['PG', 'BEI.DE']])