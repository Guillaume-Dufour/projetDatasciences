# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
import Traffic
import introduction as intro
import anova_strenght_job as asj
import anova_time_answer_job as ataj
import dash_table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dataframe_constructed = pd.read_csv("../data/data_constructed.csv", sep=',', low_memory=False)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Introduction', children=[
            intro.introduction
        ]),
        dcc.Tab(label='Prise en main des données', children=[
            dcc.Tabs([
                dcc.Tab(label="Par année", children=[
                    dcc.Graph(id="year", figure=Traffic.yearTraffic(dataframe_constructed))
                ]),
                dcc.Tab(label="Par mois", children=[
                    dcc.Graph(id="month"),
                    dcc.Slider(
                        id='year_slider',
                        min=dataframe_constructed['year'].min(),
                        max=dataframe_constructed['year'].max(),
                        value=dataframe_constructed['year'].max(),
                        marks={str(year): str(year) for year in dataframe_constructed['year'].unique()},
                        step=None
                    )
                ]),
                dcc.Tab(label="Par jour de la semaine", children=[
                    dcc.Graph(id="weekday", figure=Traffic.weeklyTraffic(dataframe_constructed))
                ]),
                dcc.Tab(label="Par heure de la journée", children=[
                    dcc.Graph(id="hour", figure=Traffic.hourTraffic(dataframe_constructed))
                ])
            ])
        ]),
        dcc.Tab(label='Analyse du nombre de mail en fonction du poste', children=[
            asj.introduction,
            dcc.Graph(figure=asj.fig),
            dash_table.DataTable(
                id='first_result',
                columns=[{"name": i, "id": i} for i in asj.anova_table.reset_index().columns],
                data=asj.anova_table.reset_index().to_dict("records")
            )
        ]),
        dcc.Tab(label="Analyse du poste du destinataire en fonction du poste de l'expéditeur", children=[
            html.Div(children=
            html.Img(
                src="../brouillon/img2.png")
            )
        ]),
        dcc.Tab(label="Analyse du temps de réponse à un mail reçu en fonction du poste de l'expéditeur", children=[
            ataj.introduction,
            dcc.Graph(figure=ataj.fig),
            dash_table.DataTable(
                id='third_result',
                columns=[{"name": i, "id": i} for i in ataj.anova_table.reset_index().columns],
                data=ataj.anova_table.reset_index().to_dict("records")
            ),
            ataj.conclusion
        ])
    ])
])


@app.callback(
    Output('month', 'figure'),
    Input('year_slider', 'value'))
def update_graph(year_slider):
    fig = Traffic.monthTraffic(dataframe_constructed, year_slider)
    return fig


app.run_server(debug=True)
