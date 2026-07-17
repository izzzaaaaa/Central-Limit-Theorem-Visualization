import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#Part A
#1.loading the dataset
df = pd.read_csv('IndianHousePrices.csv')

#2.extracting the Price column
prices = df['Price'].copy()

#3.removing missing values(NaN)
prices = prices.dropna()

#removing zero values
prices = prices[prices > 0]

#converting to list of numbers (already numeric)
prices = prices.astype(float)

#4.report number of valid price values
n = len(prices)
print(f"Number of valid observations: {n}")

min_price = min(prices)
max_price = max(prices)
print(f"Minimum price: {min_price}")
print(f"Maximum price: {max_price}")

#calculating mean
total = 0
for value in prices:
    total = total + value
manual_mean = total / n
print(f"Manually calculated mean: {manual_mean:.2f}")

#calculating variance
sum_squared_diff = 0
for value in prices:
    diff = value - manual_mean
    sum_squared_diff = sum_squared_diff + (diff * diff)

manual_variance = sum_squared_diff / (n - 1)
print(f"Manually calculated variance: {manual_variance:.2f}")

#calculating standard deviation
manual_std = math.sqrt(manual_variance)
print(f"Manually calculated standard deviation: {manual_std:.2f}")

#5.plot histogram of original Price data
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Original House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()


#saving
cleaned_prices = prices.tolist()
population_mean = manual_mean
population_std = manual_std

#Part C
#1.defining sample sizes
sample_sizes = [5, 10, 30, 100]

#number of repetitions set to 1000
num_repetitions = 1000

#dictionary to store all sample means for each N
all_sample_means = {}

#loop through each sample size
for N in sample_sizes:
    print(f"\nSampling for N = {N} ")
    
    #list to store 1000 sample means for specific N
    sample_means = []
    
    #1,2,4 repeating sampling process
    for i in range(num_repetitions):
        # Step 1: Randomly draw a sample of size N with replacement
        random_indices = np.random.choice(len(cleaned_prices), size=N, replace=True)
        sample = [cleaned_prices[idx] for idx in random_indices]
        
        #3.calculating sample mean
        sample_total = 0
        for value in sample:
            sample_total = sample_total + value
        sample_mean = sample_total / N
        
        #5.storing sample means
        sample_means.append(sample_mean)
    
    #storing in dictionary
    all_sample_means[N] = sample_means
    
    #6.plotting histogram
    plt.figure(figsize=(10, 6))
    plt.hist(sample_means, bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Sampling Distribution of Sample Mean (N = {N})')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.axvline(x=population_mean, color='red', linestyle='--', linewidth=2, label=f'Population Mean = {population_mean:.2f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    #print basic summary
    mean_of_means = sum(sample_means) / len(sample_means)
    print(f"  Mean of 1000 sample means: {mean_of_means:.2f}")
    print(f"  Population mean: {population_mean:.2f}")

#Part D
#sample sizes for Part D 
sample_sizes_D = [10, 30, 100]

#number of repetitions
num_repetitions_D = 1000

#getting population parameters from Part A
mu = population_mean  #u symbol = population mean
sigma = population_std  #o symbol = population standard deviation

#looping through each sample size
for N in sample_sizes_D:
    #list to store z-values
    z_values = []
    
    #1.Repeat 1000 times
    for i in range(num_repetitions_D): 
        random_indices = np.random.choice(len(cleaned_prices), size=N, replace=True)
        sample = [cleaned_prices[idx] for idx in random_indices]
        
        #2.Calculating sample mean 
        sample_total = 0
        for value in sample:
            sample_total = sample_total + value
        x_bar = sample_total / N
        
        #3.converting to z-value using formula
        standard_error = sigma / math.sqrt(N)
        z = (x_bar - mu) / standard_error
        
        #z-value stored
        z_values.append(z)
    
    #4.plotting histogram   
    plt.figure(figsize=(10, 6))
    plt.hist(z_values, bins=30, color='purple', edgecolor='black')
    plt.axvline(x=0, color='red', linestyle='--', linewidth=2, label='z = 0')
    plt.title(f'Distribution of z-values for N = {N}')
    plt.xlabel('z-value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()