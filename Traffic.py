from matplotlib import pyplot as plt
from pandas import *

def weeklyTraffic (csvIn) :
    df = pandas.read_csv(csvIn, sep=",", low_memory=False)
    x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    count_sorted_by_day = df.groupby(['weekDay']).size().reindex(x)

    plt.bar(x, count_sorted_by_day, color='pink')
    plt.xlabel('jour de la semaine')
    plt.ylabel('nombre de mail')
    plt.title('nombre de mail en fonction du jour de la semaine')
    plt.show()

def yearTraffic (csvIn):
    df = pandas.read_csv(csvIn, sep=",", low_memory=False)
    df_count = df.groupby(df['year']).size()
    print(df_count)
    plt.bar(df_count.index,df_count)
    plt.show()