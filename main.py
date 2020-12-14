from matplotlib import pyplot
from pandas import *
from matplotlib import *
from datetime import datetime
from Traffic import *

weeklyTraffic()
yearTraffic()


"""

df = pandas.read_csv("dataWeekDay.csv", sep=',', low_memory=False)

df['year'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%Y"), axis=1)
df['hour'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%H"), axis=1)

df.to_csv('dataWeekDay.csv', index=False)"""

"""
df = pandas.read_csv("data.csv", sep=',', low_memory=False)

df2 = df.drop_duplicates(subset=["Date", "From", "To"])

df2 = df2.drop(df2[df2.Date < "2000-00-00 00:00:00"].index)

df2['weekday'] = df2.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%A"), axis=1)

df2.to_csv('dataWeekDay.csv', index=False)

def compter_weight(i):
    dataframe = df.groupby(by=['Cat_' + str(i) + '_weight'], dropna=False).count()
    print(dataframe)


def compter_level(i, j):
    dataframe = df.groupby(by=['Cat_' + str(i) + '_level_' + str(j)], dropna=False).count()
    print(dataframe)


for x in range(1, 13):
    for y in range(1, 3):
        compter_level(x, y)

x = datetime.fromisoformat("2000-08-22 14:44:00")

print(x.strftime("%A"))
print(x.weekday())

"""