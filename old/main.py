from pandas import *
import re

"""print("SANS TRAITEMENT")
print(df['X-Origin'].value_counts(dropna=False))

print("\n\n")

print("AVEC TRAITEMENT")

df['X-Origin'] = df['X-Origin'].str.lower()
print(df['X-Origin'].value_counts(dropna=False))"""




"""
df['weekday'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%A"), axis=1)

df2 = df.drop(df[df.Date < "2000-00-00 00:00:00"].index)

df.to_csv('dataV4.csv', index=False)"""


"""df = pandas.read_csv("dataV3.csv", sep=',', low_memory=False)
df2 = df.drop_duplicates(subset=["Date", "From", "To"])"""


"""
from Traffic import *

dataFrame = pandas.read_csv("constructedData.csv", sep=',', low_memory=False)
weeklyTraffic(dataFrame)
yearTraffic(dataFrame)
monthTraffic(dataFrame, 2001)
hourTraffic(dataFrame)"""
