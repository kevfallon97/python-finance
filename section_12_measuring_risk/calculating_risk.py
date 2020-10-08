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

# COVARIANCE AND CORRELATION

# annualised variance
PG_var_a = sec_returns['PG'].var() * 250
BEI_var_a = sec_returns['BEI.DE']. var() * 250

# annualised covariance matrix
cov_matrix = sec_returns.cov() * 250
print(f"COVARIANCE MATRIX \n{cov_matrix}")

# calculate the correlation 
corr_matrix = sec_returns.corr()
print(f"CORRELATION MATRIX\n{corr_matrix}")
# NOTE: THIS IS THE CORRELATION BETWEEN RETURNS, NOT THE EQUITY PRICES
# NOTE: DO NOT ANNUALISE THE CORRELATION TABLE, IT DOES NOT CONTAIN AVERAGE DAILY VALUES