from matplotlib import pyplot as plt
import plotly.graph_objects as go
from pandas import *

def weeklyTraffic (df) :
    x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df_count = df.groupby(['weekDay']).size().reindex(x)

    """plt.bar(x, count_sorted_by_day, color='pink')
    plt.xlabel('jour de la semaine')
    plt.ylabel('nombre de mail')
    plt.title('nombre de mail en fonction du jour de la semaine')
    plt.show()"""
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="nombre de mail envoyé en fonction du jour de la semaine"
    )
    return fig

def yearTraffic (df):
    df_count = df.groupby(df['year']).size()
    """plt.bar(df_count.index, df_count)
    plt.show()"""
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="nombre de mail envoyé en fonction de l'année"
    )
    return fig

def monthTraffic (df, year) :
    """
    plt.bar(df_count.index, df_count)
    plt.show()
    return plt"""
    x = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dfFiltered = df.drop(df[df.year != year].index)
    df_count = dfFiltered.groupby(dfFiltered['month']).size().reindex(x)
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="nombre de mail envoyé en fonction du mois de l'année sélectionnée"
    )
    return fig

def hourTraffic (df) :
    df_count = df.groupby(df['hour']).size()
    """plt.bar(df_count.index, df_count)
    plt.show()"""
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="nombre de mail envoyé en fonction de l'heure dans la journée"
    )
    return fig