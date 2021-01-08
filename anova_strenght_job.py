import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

'''
dataFrame = pd.read_csv("data/data_constructed_job.csv", sep=",", low_memory=False)
dataFrame = dataFrame.drop(dataFrame.columns[[0, 1, 4]], axis=1)
ax = sns.boxplot(x='JobLevel', y='strength', data=dataFrame, color='#99c2a2')
plt.show()
'''

dataFrame = pd.read_csv("data/data_job.csv", sep=",", low_memory=False)
dataFrame = dataFrame.groupby(['Name', 'Note', 'JobLevel'])['out_degree'].sum().reset_index()
# dataFrame.to_csv("data/data_constructed_job.csv", index=False)

ax = sns.boxplot(x='JobLevel', y='out_degree', data=dataFrame, color='#99c2a2')
plt.show()

# Ordinary Least Squares (OLS) model
model = ols('out_degree ~ JobLevel', data=dataFrame).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

