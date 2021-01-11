# -*- coding: utf-8 -*-
import base64

import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
import traffic as traffic
import introduction as intro
import anova_strenght_job as asj
import anova_time_answer_job as ataj
import afc_job_job as ajj
import dash_table
import conclusion as ccl

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

print("... ouverture data_constructed.csv en cours ...")
print("... chargement du site en cours ...")
dataframe_constructed = pd.read_csv("../data/data_constructed.csv", sep=',', low_memory=False)

logo_ig = '../ressources/logoig.png'
logo_popo = '../ressources/logopopo.png'
encoded_ig = base64.b64encode(open(logo_ig, 'rb').read())
encoded_popo = base64.b64encode(open(logo_popo, 'rb').read())

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Introduction', children=[
            html.Div(
                html.Img(src='data:image/png;base64,{}'.format(encoded_ig.decode()),
                         style={'height': '100px', 'width': '100px'}),
                style={'width': '32%', 'display': 'inline-block'}
            ),
            html.Div(
                html.H2("Projet data science"),
                style={'width': '32%', 'display': 'inline-block', 'textAlign': 'center'}
            ),
            html.Div(
                html.Img(src='data:image/png;base64,{}'.format(encoded_popo.decode()),
                         style={'height': '100px', 'width': '100px'}),
                style={'width': '32%', 'display': 'inline-block', 'textAlign': 'right'}
            ),
            intro.introduction
        ]),

        dcc.Tab(label='Prise en main des données', children=[
            dcc.Tabs([
                dcc.Tab(label="Par année", children=[
                    dcc.Tab(label='Introduction', children=[
                        traffic.introduction
                    ]),
                    dcc.Graph(id="year", figure=traffic.year_traffic(dataframe_constructed))
                ]),
                dcc.Tab(label="Par mois", children=[
                    dcc.Tab(label='Introduction', children=[
                        traffic.introduction
                    ]),
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
                    dcc.Tab(label='Introduction', children=[
                        traffic.introduction
                    ]),
                    dcc.Graph(id="weekday", figure=traffic.weekly_traffic(dataframe_constructed))
                ]),
                dcc.Tab(label="Par heure de la journée", children=[
                    dcc.Tab(label='Introduction', children=[
                        traffic.introduction
                    ]),
                    dcc.Graph(id="hour", figure=traffic.hour_traffic(dataframe_constructed))
                ])

            ]),
            dcc.Tab(label='Conclusion', children=[
                traffic.conclusion
            ]),
        ]),

        dcc.Tab(label='Analyse du nombre de mails en fonction du poste', children=[
            asj.introduction,

            asj.titleBoxPlot,
            dcc.Graph(figure=asj.fig),

            asj.introAnova,

            asj.titleTabAnova,

            dash_table.DataTable(
                id='first_result',
                columns=[{"name": i, "id": i} for i in asj.anova_table.reset_index().columns],
                data=asj.anova_table.reset_index().to_dict("records")
            ),

            asj.analyse
        ]),

        dcc.Tab(label="Analyse du temps de réponse à un mail reçu en fonction du poste de l'expéditeur", children=[
            ataj.introduction,

            dcc.Graph(figure=ataj.fig1),

            ataj.analyseDiagramme,

            dcc.Graph(figure=ataj.fig2),
            ataj.titleTabAnova,
            dash_table.DataTable(
                id='third_result2',
                columns=[{"name": i, "id": i} for i in ataj.anova_table2.reset_index().columns],
                data=ataj.anova_table2.reset_index().to_dict("records")
            ),

            ataj.analyseAnova1,

            dcc.Graph(figure=ataj.fig3),

            ataj.titleTabAnova,

            dash_table.DataTable(
                id='third_result3',
                columns=[{"name": i, "id": i} for i in ataj.anova_table3.reset_index().columns],
                data=ataj.anova_table3.reset_index().to_dict("records")
            ),

            ataj.conclusion
        ]),

        dcc.Tab(label="Analyse du poste du destinataire en fonction du poste de l'expéditeur", children=[
            ajj.resultat
        ]),

        dcc.Tab(label="Conclusion", children=[
            ccl.content
        ])

    ])
])


@app.callback(
    Output('month', 'figure'),
    Input('year_slider', 'value'))
def update_graph(year_slider):
    fig = traffic.month_traffic(dataframe_constructed, year_slider)
    return fig


app.run_server(debug=False)
