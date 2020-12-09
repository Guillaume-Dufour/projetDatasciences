from pandas import *
from datetime import datetime

df = pandas.read_csv("dataV2.csv", sep=',', low_memory=False)

df['weekday'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%A"), axis=1)

df.to_csv('dataV3.csv', index=False)


"""
def compter_weight(i):
    dataframe = df.groupby(by=['Cat_' + str(i) + '_weight'], dropna=False).count()
    print(dataframe)


def compter_level(i, j):
    dataframe = df.groupby(by=['Cat_' + str(i) + '_level_' + str(j)], dropna=False).count()
    print(dataframe)


for x in range(1, 13):
    for y in range(1, 3):
        compter_level(x, y)
"""

"""
df2 = df.drop_duplicates(subset=["Date", "From", "To"])

df2.to_csv('dataV2.csv', index=False)


x = datetime.fromisoformat("2000-08-22 14:44:00")

print(x.strftime("%A"))
print(x.weekday())

"""