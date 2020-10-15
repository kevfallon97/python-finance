import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

# calculate the price of a call option using BSM

# S - stock price
# K - strike price
# r - risk free rate
# T - time horizon (years)

# functions for calculating d1 and d2
def d1(S, K, r, stdev, T):
	return (np.log(S/K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

def d2(S, K, r, stdev, T):
	return (np.log(S/K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

# BSM function
def BSM(S, K, r, stdev, T):
	return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))

ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-3-21')['Adj Close']

# get current stock price
S = data.iloc[-1]
# get log returns
log_returns = np.log(1 + data.pct_change())

stdev = log_returns.std() * 250 ** 0.5

r = 0.025
K = 110.0
T = 1

print(f"Call option price: {BSM(S, K, r, stdev, T)}")
