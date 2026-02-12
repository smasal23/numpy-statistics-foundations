# Inferential Statistics - EDA(Exploratory Data Analysis) - does data testing or hypothesis testing
# Hypothesis Testing
    # Pavlov Experiment
    # Testing is done only to find out whether the assumption is right or wrong
    # H0 and H1 is Null Hypothesis and Alternative Hypothesis resp.
    # Each data has different techniques.
    # Summarize P-value and the value when P < 0.05; reject the H0 and when p >= 0.05, fail to reject the H0. 0.05 is the possibility of 5%.
        # 5% is the standard acceptance value for measuring the hypothesis.
    # Need to know what test to which data.

    # Mean Test

# Z-test
from statsmodels.stats.weightstats import ztest as ztest, ttest_ind
import scipy.stats as stats

#enter IQ levels for 20 patients
data = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99,105, 109, 109, 109, 110, 112, 112, 113, 114, 115]

#perform one sample z-test
print(ztest(data, value=100))  # when sample size is above 30
print(stats.ttest_1samp(data, popmean=10))  # when sample size is below 30; ttest_1samp for


# Two Sample Test
# 2 sample test - check for independence
# This test will only confirm whether the two are related. Always take Independent events as null hypothesis.
#Independent - No difference
#Dependent - difference
#enter IQ levels for 20 individuals from each city
cityA = [82, 84, 85, 89, 91, 91, 92, 94, 99, 99,
       105, 109, 109, 109, 110, 112, 112, 113, 114, 114]

cityB = [90, 91, 91, 91, 95, 95, 99, 99, 108, 109,
       109, 114, 115, 116, 117, 117, 128, 129, 130, 133]
#perform two sample z-test
print(ztest(cityA, cityB, value=0))   # has a weak evidence
print(stats.ttest_ind(a=cityA, b=cityB, equal_var=True))

# Example 1
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df=pd.read_csv("https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/diabetes.csv")
print(df.head())
print(stats.ttest_ind(a = df['Insulin'], b = df['BloodPressure']))
print(stats.ttest_ind(a = df['Age'], b = df['BMI']))

# Example 2
df1 =pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/cs1%20(1).csv')
print(df1.shape)
print(df1.head())

print(stats.ttest_ind(a = df1['age'], b = df1["income"]))
    # Test 1
m = df1[df1['gender']=='MALE']['income']
print(m.head())
n= (df1[df1['gender']=='FEMALE']['income'])
print(n.head())
print(stats.ttest_ind(m, n))

    # Test 2
a = df1[df1['mortgage'] == 'YES']['income']
b = df1[df1['mortgage'] == 'NO']['income']
print(stats.ttest_ind(a, b))
# The p-value is 0.72, so the null hypothesis fails to be rejected, hence the relation is independent with no difference.

    # Test 3
c = df1[df1['married'] == 'YES']['income']
d = df1[df1['married'] == 'NO']['income']
print(stats.ttest_ind(c, d))
# The p-value is 0.61, so the null hypothesis fails to be rejected, hence the relation is independent with no difference.