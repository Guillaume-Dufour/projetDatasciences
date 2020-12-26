from pandas import *
from re import *

"""df = pandas.read_csv("dataV3.csv", sep=',', low_memory=False)

dataframe = df.groupby(by=['From', 'weekday'], dropna=False).size()

print(dataframe)"""

"""df = pandas.read_csv("dataV3.csv", sep=',', low_memory=False)
df['X-Origin'] = df['X-Origin'].str.lower()
print(df['X-Origin'].value_counts(dropna=False))"""

df = pandas.read_csv("dataV4.csv", sep=',', low_memory=False)

df2 = df.drop_duplicates(subset=["Date", "From", "To"])

# df2['X-Origin'] = df2['X-Origin'].str.lower()

# print(df2['x-origin'].value_counts(dropna=False))

substring = "-Original Message-"
substring2 = "- Forwarded by"
substring3 = "RE:"


print("Avant DROPNA : " + str(len(df2.index)))

df2 = df2.dropna(subset=['content'])

print("Après DROPNA : " + str(len(df2.index)))

df3 = df2[df2['content'].str.contains(substring)]
# df4 = df2[df2['content'].str.contains(substring2)]
# df5 = df2[df2['content'].str.contains(substring3)]

"""print("Original message : " + str(len(df3.index)))
print("Forwarded by : " + str(len(df4.index)))
print("RE : " + str(len(df5.index)))"""



#df3.to_csv("df3csv.csv")


