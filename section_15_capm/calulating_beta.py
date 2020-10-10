import numpy as np
import pandas as pd
from pandas_datareader import data as wb

# Beta = cov(security, market) / variance(market)


# retrieve data
assets = ['PG', '^GSPC']
data = pd.DataFrame()
for asset in assets:
	data[asset] = wb.DataReader(asset, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']

# generate covariance matrix between PG returns and S&P500
sec_returns = np.log(data / data.shift(1))
cov = sec_returns.cov() * 250

# grab the co-variance value, this is the nominator in the beta calculation
cov_with_market = cov.iloc[0,1]

# calculate the market variance, the denominatior in the beta calculation
market_var = sec_returns['^GSPC'].var() * 250

PG_beta = cov_with_market / market_var
print(f"PG Beta: {PG_beta}")