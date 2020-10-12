import numpy as np
import matplotlib.pyplot as plt

# Objective: Prefict the firm's future gross profit
# Requirements:
# 1 - Expected revenue
# 2 = Expected COGS (Cost of goods sold)

# Perform 1000 simulations of the company's expected revenues
# Figures represent millions in this example
rev_m = 170
rev_stdev = 20
iterations = 1000

# create a normal distribution with 1000 values
rev = np.random.normal(rev_m, rev_stdev, iterations)

# plot the values
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

# assume that COGS are typically 60% of the revenues generated for the same period, m = 60% stdev = 10% 
# assign a random cogs value to each one of the norm dist data pints
COGS = -(rev * np.random.normal(0.6, 0.1))

plt.figure(figsize=(15,6))
plt.plot(COGS)
plt.show()

print(f"COGS mean: {COGS.mean()}")
print(f"COGS stdev: {COGS.std()}")

# Gross profit calculation
gross_profit = rev + COGS #COGS is negative
plt.figure(figsize=(15,6))
plt.plot(gross_profit)
plt.show()

print("Gross Profit Figures")
print(f"Max:\t{max(gross_profit)}")
print(f"Min:\t{min(gross_profit)}")
print(f"Mean:\t{gross_profit.mean()}")
print(f"Stdev:\t{gross_profit.std()}")

# plot data on a histogram
plt.figure(figsize=(10,6))
plt.hist(gross_profit, bins=20)
plt.show()