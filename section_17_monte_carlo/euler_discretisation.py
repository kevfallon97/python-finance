import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1', end='2017-3-21')['Adj Close']

log_returns = np.log(1 + data.pct_change())

r = 0.025
stdev = log_returns.std() * 250 ** 0.5
stdev = stdev.values

T = 1.0
t_intervals = 250
delta_t = T / t_intervals

iterations = 10000

Z = np.random.standard_normal((t_intervals + 1, iterations))
S = np.zeros_like(Z)
# fill first row with most recent available stock price
S0 = data.iloc[-1]
S[0] = S0

for t in range(1, t_intervals + 1):
	S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])

plt.figure(figsize=(10,6))
plt.plot(S[:, :10])
plt.show()

# create an array that contains either 0's or the numbers equal to the differences
p = np.maximum(S[-1] - 110, 0)

C = np.exp(-r * T) * np.sum(p) / iterations
print(f"Call Price: {C}")