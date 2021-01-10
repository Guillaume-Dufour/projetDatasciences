import plotly.express as px
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import dash_html_components as html

introduction = html.Div([

    html.H4("Anova temps de réponse à un mail reçu en fonction du poste"),
    html.P(
        "Nous nous sommes demandés si le poste des employés avait une influence sur le temps de réponse, un employé met-il plus de temps à répondre qu’un manager ? Pour vérifier cela, nous avons donc, dans un premier temps, réalisé un diagramme pour visualiser les données.",
        style={'marginBottom': 30}
    ),

    html.P("Boxplot temps de réponse moyen en heures en fonction du poste au sein de l'entreprise",
           style={'text-decoration': 'underline', 'text-align': 'center'}
           )
])

dataFrame = pd.read_csv("../data/data_annova_job_time_response.csv", sep=",", low_memory=False)

# First diagram, without removing any value
fig1 = px.box(dataFrame,
              x='job_answerer',
              y='time_response',
              labels={'job_answerer': "Type of job", 'time_response': "Time of response in hours"},
              height=600)

analyseDiagramme = html.Div([
    html.P(
        "En regardant ce diagramme, on a l’impression que les managers répondent plus vite. On remarque aussi que l’un des employés met beaucoup plus de temps à répondre (1400 heures) ainsi qu’un externe (>5000 heures) on a donc décidé de l’enlever des données avant de faire l’analyse. ",
        style={'marginBottom': 20}
    ),
    html.P(
        "On a donc réalisé une anova:",
        style={'marginBottom': 30}
    ),
    html.P(
        "Boxplot temps de réponse moyen en heures en fonction du poste au sein de l'entreprise",
        style={'text-decoration': 'underline', 'text-align': 'center' }
    )

])

# Diagram 2 : Les 2 individus atypiques enlevés
dataFrame1 = dataFrame.copy()[dataFrame.time_response < 31536000]  # superieur à 1 an
dataFrame1["time_response"] = dataFrame["time_response"] / 3600

fig2 = px.box(dataFrame1,
              x='job_answerer',
              y='time_response',
              labels={'job_answerer': "Type of job", 'time_response': "Time of response in hours"},
              height=600)

# Ordinary Least Squares (OLS) model
model2 = ols('time_response ~ job_answerer', data=dataFrame1).fit()
anova_table2 = sm.stats.anova_lm(model2, typ=2)

titleTabAnova = html.Div(
    "Tableau analyse variance",
    style={'text-decoration': 'underline', 'text-align': 'center', 'marginBottom':20}
)
analyseAnova1 = html.Div([
    html.P(
        "On suppose que l’on a égalité des variances et que nos variables suivent une loi gaussienne. ",
        style={'marginTop': 20}
    ),
    html.P(
        "H0 → m1 = … = mp"
    ),
    html.P(
        "H1 → Il existe rs tel que mr ≠ ms"
    ),
    html.P(
        "On a la Pvalue = 0.277963 ce qui est supérieur à 5%, on ne rejette donc pas H0. Nous n’avons donc pas mis en évidence un lien entre le poste et le nombre de mails envoyés.",
    ),
    html.P(
        "Cependant, nous avons remarqué que beaucoup de personnes (~250) mettent plus d’un mois à répondre, ce qui nous semble très bizarre.",
        style={'marginBottom': 20}
    ),
    html.P(
        "On a donc décidé de refaire une anova sans ces données pour prendre en compte seulement celles réalistes.",
        style={'marginBottom': 30}
    ),
    html.P(
        "Boxplot temps de réponse moyen en heures en fonction du poste au sein de l'entreprise",
        style={'text-decoration': 'underline', 'text-align': 'center'}
    )
])
# Diagram 3 : On garde toutes les réponses inférieurs à 1 mois
dataFrame2 = dataFrame.copy()[dataFrame.time_response < 31536000 / 12]  # superieur à 1 an
dataFrame2["time_response"] = dataFrame["time_response"] / 3600

fig3 = px.box(dataFrame2,
              x='job_answerer',
              y='time_response',
              labels={'job_answerer': "Type of job", 'time_response': "Time of response in hours"},
              height=1000)

# Ordinary Least Squares (OLS) model
model3 = ols('time_response ~ job_answerer', data=dataFrame2).fit()
anova_table3 = sm.stats.anova_lm(model3, typ=2)

conclusion = html.Div([
    html.P("On suppose que l’on a égalité des variances et que nos variables suivent une loi gaussienne."),
    html.P("H0 → m1 = … = mp "),
    html.P("H1 → Il existe rs tel que mr ≠ ms "),
    html.P("On a la Pvalue = 0.0015  ce qui est inférieur à 5%, on rejette H0. Nous avons donc  mis en évidence un lien entre le poste et le temps de réponse."),
    html.P(
        "Maintenant, si on regarde de nouveau le boxplot, ça ne soit voit pas trop, mais en zoomant, on remarque que les externes répondent plus vite que les associés."

    )
])
