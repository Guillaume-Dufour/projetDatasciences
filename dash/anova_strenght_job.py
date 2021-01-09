import pandas as pd
import plotly.express as px
import dash_html_components as html
import statsmodels.api as sm
from statsmodels.formula.api import ols

introduction = html.Div([
    html.H4("Anova nombre de mails reçus et envoyés en fonction du poste"),
    html.Div("Afin de ne pas fausser nos résultats, nous avons pris la liberté d'enlever"
             " une donnée extrême qui concerne un manager du nom de Vince Kaminiski "),
    html.Div("Voici le boxplot fourni par nos données illustrant le nombre de mails reçus et envoyés "
             "en fonction du poste")
])

dataFrame = pd.read_csv("../data/data_constructed_job.csv", sep=",", low_memory=False)

fig = px.box(dataFrame, x='JobLevel', y='strength')

model = ols('strength ~ JobLevel', data=dataFrame).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

