from pandas import *
import re

"""df = pandas.read_csv("dataV3.csv", sep=',', low_memory=False)

destinataires = []"""

"""chaine = "frozenset({'david.l.johnson@enron.com', 'john.shafer@enron.com'})"
res = re.split("[{}]", chaine)

for i in range(1, len(res)):
    if i != len(res) - 1:
        print(res[i])"""

"""print("SANS TRAITEMENT")
print(df['X-Origin'].value_counts(dropna=False))

print("\n\n")

print("AVEC TRAITEMENT")

df['X-Origin'] = df['X-Origin'].str.lower()
print(df['X-Origin'].value_counts(dropna=False))"""


"""for row in df.iterrows():
    if len(df[df['From'].astype(str).str.contains(row['To'])].index) and len(df[df['To'].astype(str).str.contains(row['From'])].index):"""




"""
df['weekday'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%A"), axis=1)

df2 = df.drop(df[df.Date < "2000-00-00 00:00:00"].index)

df.to_csv('dataV4.csv', index=False)"""


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

df = pandas.read_csv("dataV3.csv", sep=',', low_memory=False)
df2 = df.drop_duplicates(subset=["Date", "From", "To"])
from Traffic import *
from ConstructeurCSV import *

dropLine("data.csv", "constructedData.csv")
dropColumn("constructedData.csv", "constructedData.csv")
addYear("constructedData.csv", "constructedData.csv")
addHour("constructedData.csv", "constructedData.csv")
addWeekDay("constructedData.csv", "constructedData.csv")

weeklyTraffic("constructedData.csv")
yearTraffic("constructedData.csv")
