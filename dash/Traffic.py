import dash_html_components as html
import plotly.graph_objects as go

introduction = html.Div([
    html.Div("Dans un premier temps, nous avons réalisé des graphiques afin de visualiser le nombre de mails envoyés "
             "par jour de la semaine, par heure, par mois d’une année et enfin par année. Cela nous a permis de "
             "supprimer les mails dont les dates sont  avant 1999 et après 2003 car ils n’étaient pas exploitables ("
             "trop peu nombreux, mails souvent automatiques…)."
             ),
])


def weeklyTraffic(df):
    x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df_count = df.groupby(['weekDay']).size().reindex(x)
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="Nombre de mails envoyés en fonction du jour de la semaine"
    )
    return fig


def yearTraffic(df):
    df_count = df.groupby(df['year']).size()
    print(df_count)
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="Nombre de mails envoyés en fonction de l'année"
    )
    return fig


def monthTraffic(df, year):
    x = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
    dfFiltered = df.drop(df[df.year != year].index)
    df_count = dfFiltered.groupby(dfFiltered['month']).size().reindex(x)
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="Nombre de mails envoyés en fonction du mois de l'année sélectionnée"
    )
    return fig


def hourTraffic(df):
    df_count = df.groupby(df['hour']).size()
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="Nombre de mail envoyés en fonction de l'heure dans la journée"
    )
    return fig
