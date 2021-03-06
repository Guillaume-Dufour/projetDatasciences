import dash_html_components as html
import plotly.graph_objects as go

introduction = html.Div([
    html.H5(
        "Prise en main des données"
    ),
    html.Div(
        html.P(
            "Dans un premier temps, nous avons réalisé des graphiques afin de visualiser le nombre de mails envoyés "
            "par jour de la semaine, par heure, par mois d’une année et enfin par année. Cela nous a permis de "
            "supprimer les mails dont les dates sont  antérieures à 1999 et postérieurs à 2003 car ils n’étaient pas "
            "exploitables (trop peu nombreux, mails souvent automatiques …). ",
            style={'marginBottom': 20, 'marginTop': 20}
        )
    )
])

conclusion = html.Div([
    html.Br(),
    html.H5(
        "Résultats"
    ),
    html.Div(
        html.P(
            "Nous avons ensuite voulu regarder s'il y avait des heures / jours où on envoyait plus de mails que "
            "d’autres. Sans surprise, nous nous sommes rendus compte que les employés envoient des mails uniformément "
            "durant leurs heures / jours de travail. Cela nous a aussi permis de nous rendre compte que nos dates "
            "n’étaient pas toutes dans le même fuseau horaire.",
            style={'marginBottom': 20, 'marginTop': 20}
        )
    )
])


def weekly_traffic(df):
    x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df_count = df.groupby(['weekDay']).size().reindex(x)
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="Nombre de mails envoyés en fonction du jour de la semaine"
    )
    return fig


def year_traffic(df):
    df_count = df.groupby(df['year']).size()
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="Nombre de mails envoyés en fonction de l'année"
    )
    return fig


def month_traffic(df, year):
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


def hour_traffic(df):
    df_count = df.groupby(df['hour']).size()
    fig = go.Figure(
        data=[go.Bar(
            x=df_count.index,
            y=df_count)],
        layout_title_text="Nombre de mail envoyés en fonction de l'heure dans la journée"
    )
    return fig
