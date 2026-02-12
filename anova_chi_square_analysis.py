import pandas as pd
import seaborn as sns
import scipy.stats as stats
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df=pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/cs1%20(1).csv')
df.shape
print(df.head())

print(df["region"].unique())
print(df["children"].unique())
# ANOVA - Analysis of Variance
# When need to test more than 2 columns.
# Scenario 1
g1 = df[df['region']=='INNER_CITY']['income']
g2 = df[df['region']=='TOWN']['income']
g3 = df[df['region']=='RURAL']['income']
g4 = df[df['region']=='SUBURBAN']['income']
print(stats.f_oneway(g1,g2,g3,g4))   #anova testing analyzing the effect of one categorical factor on a numerical dependent variable

sns.boxplot(x='region',y='income',data=df)

# IQR - Inter Quartile Range(Q2 and Q3) - Min => Median => Max - Answers Data present in what range
# Percentage/ Percentile
# Scenario 2
g1 = df[df['region']=='INNER_CITY']['age']
g2 = df[df['region']=='TOWN']['age']
g3 = df[df['region']=='RURAL']['age']
g4 = df[df['region']=='SUBURBAN']['age']
print(stats.f_oneway(g1,g2,g3,g4))

sns.boxplot(x='region',y='age',data=df)

# Scenario 3
g1 = df[df['children']== 0]['income']   # Representation of numeric column items matter
g2 = df[df['children']== 1]['income']
g3 = df[df['children']== 2]['income']
g4 = df[df['children']== 3]['income']
print(stats.f_oneway(g1,g2,g3,g4))

sns.boxplot(x='children',y='income',data=df)


# Chi-Squared Test
# Scenario 1
b = pd.crosstab(df['gender'],df['mortgage'])
print(b)
print(stats.chi2_contingency(b))

# Sceanrio 2
c = pd.crosstab(df['age'], df['married'])
print(c)
print(stats.chi2_contingency(c))


# Example 1
#Income vs Save_Act
A = df[df['save_act'] == 'YES']['income']
B = df[df['save_act'] == 'NO']['income']
print(stats.ttest_ind(A, B))
# The p-value is less than 0.05, so we reject the Ho and save_act is dependent on income.

# Tell me what will you do with 100 crores
#1] Since mortgage is independent of income, we can offer appropriate remortgage offers to the residents.(p-value = 0.72)
#2] Since having a car is independent of income, we can set-up new showrooms(p-value = 0.07 for the people living in inner city and town
#   since the number of people without car is 84 and 50 respectively.
