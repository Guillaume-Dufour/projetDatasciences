import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import Traffic

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("data/constructedData.csv", sep=',', low_memory=False)

app.layout = html.Div([

    html.Div([

        html.Div([
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['by month', 'by hour', 'by year', 'by weekday']],
                value='by month',
                labelStyle={'display': 'inline-block'}
            )
        ])
    ]),

    dcc.Graph(id='indicator'),

    dcc.Slider(
        id='year--slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].max(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


@app.callback(
    Output('indicator', 'figure'),
    Input('xaxis-type', 'value'),
    Input('year--slider', 'value'))
def update_graph(xaxis_type, year_value):
    if xaxis_type == 'by month':
        fig = Traffic.monthTraffic(df, year_value)
        return fig
    elif xaxis_type == 'by hour':
        fig = Traffic.hourTraffic(df)
        return fig
    elif xaxis_type == 'by year':
        fig = Traffic.yearTraffic(df)
        return fig
    elif xaxis_type == 'by weekday':
        fig = Traffic.weeklyTraffic(df)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
