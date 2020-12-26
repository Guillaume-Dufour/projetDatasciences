from matplotlib import pyplot as plt
from pandas import *
from matplotlib import *

df = pandas.read_csv("dataV3.csv", sep=',', low_memory=False)

x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


df_weekday = df.groupby(['weekday']).size().reindex(x)

plt.bar(x, df_weekday, color="green")
plt.xlabel('jour de la semaine')
plt.ylabel('nombre de mail')
plt.title('nombre de mail en fonction du jour de la semaine')
plt.show()

print(df_weekday)
