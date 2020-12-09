from matplotlib import pyplot as plt
from pandas import *

def weeklyTraffic () :
    df = pandas.read_csv("dataWeekDay.csv", sep=",", low_memory=False)
    x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    count_sorted_by_day = df.groupby(['weekday']).size().reindex(x)

    plt.bar(x, count_sorted_by_day, color='pink')
    plt.xlabel('jour de la semaine')
    plt.ylabel('nombre de mail')
    plt.title('nombre de mail en fonction du jour de la semaine')
    plt.show()

def yearTraffic ():
    df = pandas.read_csv("dataWeekDay.csv", sep=",", low_memory=False)
    df_count = df.groupby(df['year']).size()
    print(df_count)
    plt.bar(df_count.index,df_count)
    #TODO : signaler qu'il faut enlever tout ce qu'il y a au dessus de 2003
    plt.show()