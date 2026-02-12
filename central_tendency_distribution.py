
# Data Analysis - Derive, Analyze and Report/Insights
    # Statistical Analysis - when data is new
    # Exploratory Analysis - when data has been processed

# Statistical Analysis -
    # Mean - Effected by the extreme values; should check whether data is properly distributed.
    # Median - Data should always be sorted and is not affected by extreme values
    # Mode -
    # Std
    # Variance
    # Correlation

# Distribution - Normal Distribution, Gausian and Bell data can be represented with a Bell-Curve.
# Here PMF is used for discrete values and CDF is used for continous values. And these two are calculated for drawing the bell-curve.

import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df=pd.read_csv("https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/diabetes.csv")
print(df.head())

a = [3, 5, 7, 9, 10, 12, 13, 14, 16, 17, 22, 24, 25, 27, 28, 30]

print (np.average(a))
print (np.mean(a))
print (np.median(a))
print (np.min(a))
print (np.max(a))

print(np.mean(df["BloodPressure"]))
print(np.median(df["BloodPressure"]))
print(np.min(df["BloodPressure"]))
print(np.max(df["BloodPressure"]))

# draw histogram with df.bloodpressure
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sns.histplot(df['BloodPressure'], kde = True, bins = 30)
plt.title('Distribution of Blood Pressure')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.show()

# Age Column
print(np.mean(df["Age"]))
print(np.median(df["Age"]))
print(np.min(df["Age"]))
print(np.max(df["Age"]))

plt.figure(figsize = (10, 6))
sns.histplot(df["Age"], kde = True, bins = 30)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# Central Limit Theorem
# Skewness - An asymmetrical statistical data used to understand where majority of data is grouped for a quick inference.
# Left skewed - Mode > Mean & Mode
# Right Skewed - Mode < Mean & Mode
# Mean ≈ Median → likely symmetric
# Mean > Median → right-skewed
# Mean < Median → left-skewed