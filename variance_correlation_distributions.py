# Standard Deviation - amount of dispersion from the mean telling the highest and lowest extend.
# Ideal STD is 0 - 3.5; Lower std means data is dispersed on a small scale, Higher std means data is dispersed on a large scale.
# Formula

# Variance - individual data point, the amount of variation from the mean in a raw form, generally required for mathematical derivations
import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df=pd.read_csv("https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/diabetes.csv")
print(df.head())

print(np.std(df["DiabetesPedigreeFunction"]))
print(np.var(df["BMI"]))

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sns.histplot(df['BMI'], kde = True, bins = 30)
plt.title('Distribution of BMI')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()


# Pearson Correlation - ranges between -1 and +1; if 0 no corr, if +1 high corr, if  -1 negligible corr.
# Will only give the direction and strength of correlation, but not individually which is impacting which.
correlation_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Diabetes Dataset')
plt.show()

# Co-Variance - for calculation purposes only.

# Probability Distributions
# Discrete  # Bernoulli Distribution - To visualize two possible outcomes in a dsitribution using random variables by simulations.
            # Random Variable Sample and Numpy Simulation is an old technique not used nowadays it seems.

            # Binomial Distribution - To visualize getting a success or failure from an event upon a number of trials.

            # Geometrical Distribution - To visualize number of trials needed for getting first success.

# Continuous # Uniform Distribution -
             # Exponential Distribution -


# Random Samples- Numpy Simulation
import matplotlib.pyplot as plt
# Parameters for Bernoulli distribution
p = 0.2  # Probability of success
n_samples = 1000 # Number of samples
# Generate Bernoulli random variables
bernoulli_samples = np.random.binomial(1, p, n_samples)
# Plot the distribution
plt.figure(figsize=(8, 6))
plt.hist(bernoulli_samples, bins=[-0.5, 0.5, 1.5], rwidth=0.8, color='skyblue', edgecolor='black')
plt.xticks([0, 1], ['Failure (0)', 'Success (1)'])
plt.title('Bernoulli Random Variable Simulation')
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.show()