import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

"""dataFrame = pd.read_csv("data/data_annova_job_time_response.csv", sep=",", low_memory=False)
dataFrame = dataFrame.drop(dataFrame.columns[[0, 1, 4]], axis=1)
ax = sns.boxplot(x='JobLevel', y='strength', data=dataFrame, color='#99c2a2')
plt.show()"""

dataFrame = pd.read_csv("data/data_annova_job_time_response.csv", sep=",", low_memory=False)
dataFrame["time_response"] = dataFrame["time_response"] / 36000
#dataFrame = dataFrame[dataFrame.time_response < 1000]
sns.boxplot(x='job_answerer', y='time_response', data=dataFrame, color='#99c2a2')
plt.xlabel("Type of job")
plt.ylabel("Time of response in hours")
plt.show()

# Ordinary Least Squares (OLS) model
model = ols('time_response ~ job_answerer', data=dataFrame).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

