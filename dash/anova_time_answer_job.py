import plotly.express as px
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import dash_html_components as html

introduction = html.Div([

    html.H4("Anova temps de réponse à un mail reçu en fonction du poste"),
    html.P(
        "Nous nous sommes donc demandés si le poste avait une influence sur le temps de réponse, un employé met-il plus de temps à répondre qu’un manager ? Pour vérifier cela, nous avons donc, dans un premier temps, réalisé un diagramme pour visualiser les données (voir Annexe 3). En regardant ce diagramme, on a l’impression que les personnes externes à l’entreprise répondent plus vite. On remarque aussi que l’un des employés met beaucoup plus de temps à répondre (1400 heures) ainsi qu’un externe (>5000 heures) on a donc décidé de l’enlever des données avant de faire l’analyse. On a donc réalisé une anova (voir annexe 4), celle-ci nous a montré que le poste n’influait pas sur le temps de réponse…",
        style={'marginBottom': 20}
    ),
    html.P(
        "Cependant, nous avons remarqué que beaucoup de personnes (~250 ) mettent plus d’un mois à répondre, ce qui nous semble très bizarre. On a donc décidé de refaire une anova sans ces données pour prendre en compte seulement celles réalistes (voir annexe 5). Cette fois ci, on a montré un lien avec le temps de réponse et le poste de l’employé. Maintenant, si on regarde le boxplot (annexe 5), ça ne soit voit pas trop, mais en zoomant, on remarque que les externes répondent plus vite que les associés.",
        style={'marginBottom': 20}
    )


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
