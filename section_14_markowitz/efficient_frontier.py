import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# retrieve data
assets = ['PG', '^GSPC']
pf_data = pd.DataFrame()
for asset in assets:
	pf_data[asset] = wb.DataReader(asset, data_source='yahoo', start='2010-1-1')['Adj Close']

# normalise to 100
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10,5))
plt.show()

# calculate log returns
log_returns = np.log(pf_data / pf_data.shift(1))
print(f"MEAN:\n{log_returns.mean() * 250}\n")
print(f"CO-VARIANCE:\n{log_returns.cov() * 250}\n")
print(f"CORRELATION:\n{log_returns.corr()}\n")

num_assets = len(assets)

# create random weights, must sum to 1
weights = np.random.random(num_assets)
weights /= np.sum(weights)

# EXPECTED PORTFOLIO RETURN
exp_r = np.sum(weights * log_returns.mean()) * 250

# EXPECTED PORTFOLIO VARIANCE
exp_v = np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))

# EXPECTED PORTFOLIO VOLATILITY
exp_s = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))

print(f"Return: {exp_r}")
print(f"Variance: {exp_v}")
print(f"Volatility: {exp_s}")

# Generate 1000 random weightings and apply them to the portfolio
pfolio_returns = []
pfolio_volatilites = []

for i in range(1000):
	weights = np.random.random(num_assets)
	weights /= np.sum(weights)
	pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
	pfolio_volatilites.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))))

pfolio_returns = np.array(pfolio_returns)
pfolio_volatilites = np.array(pfolio_volatilites)

print(pfolio_returns)
print(pfolio_volatilites)

# PLOT DATA
# create a dataframe object with two columns, one for returns and one for volatility
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilites})
# plot the data
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10,6))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.show()
