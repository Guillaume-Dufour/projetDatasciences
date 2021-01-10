import plotly.express as px
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import dash_html_components as html

introduction = html.Div([
    html.H4("Anova temps de réponse à un mail reçu en fonction du poste"),
    html.Div("Afin de ne pas fausser nos résultats, nous avons pris la liberté d'enlever"
             " une donnée extrême "),
    html.Div("Voici le boxplot fourni par nos données illustrant le temps de réponse à un mail reçu "
             "en fonction du poste")
])

dataFrame = pd.read_csv("../data/data_annova_job_time_response.csv", sep=",", low_memory=False)

dataFrame = dataFrame[dataFrame.time_response < (31536000 / 12)]  # superieur à 1 an

dataFrame["time_response"] = dataFrame["time_response"] / 3600

fig = px.box(dataFrame,
             x='job_answerer',
             y='time_response',
             labels={'job_answerer': "Type of job", 'time_response': "Time of response in hours"},
             height=1000)

# Ordinary Least Squares (OLS) model
model = ols('time_response ~ job_answerer', data=dataFrame).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

conclusion = html.Div([
    html.P("On suppose que l’on a égalité des variances et que nos variables suivent une loi gaussienne."),
    html.P("H0 → m1 = … = mp "),
    html.P("H1 → Il existe rs tel que mr ≠ ms "),
    html.P("On a la Pvalue = 0.18 ce qui est supérieur à 5%, on ne rejette donc pas H0. "
           "Nous n’avons donc pas mis en évidence un lien entre le poste et le temps de réponse")
])
