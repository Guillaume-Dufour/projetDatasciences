import pandas as pd
import plotly.express as px
import dash_html_components as html
import statsmodels.api as sm
from statsmodels.formula.api import ols

introduction = html.Div([
    html.H4("Anova nombre de mails reçus et envoyés en fonction du poste"),
    html.Br(),
    html.Div("Nous nous sommes ensuite demandé si le poste occupé avait une incidence sur le nombre de mails envoyés. "
             "Par exemple, les employés envoient plus de mails que les personnes haut placées. Le boxplot ci-dessous "
             "ne nous permet pas à première vue de mettre en évidence de lien entre le nombre de mails "
             "envoyés et le poste des employés, en effet les moyennes ont l’air sensiblement égales. ",
             style={'marginBottom': 30}
             ),
    html.Br()
])

titleBoxPlot = html.Div(
    "Boxplot du nombre de mails reçus et envoyés en fonction du poste au sein de l'entreprise",
    style={'text-decoration': 'underline', 'text-align': 'center', 'marginBottom': 20}
)

introAnova = html.Div(
    "Nous avons donc réalisé une anova pour vérifier cela. ",
    style={'marginBottom': 30}

)

titleTabAnova = html.Div(
    "Tableau analyse variance",
    style={'text-decoration': 'underline', 'text-align': 'center', 'marginBottom': 20}
)

analyse = html.Div([
    html.H4("Analyse de l'Anova"),
    html.Br(),
    html.P("Nous supposons que nous avons l’égalité des variances et que nos variables sont issues d’une loi "
           "gaussienne."),
    html.P("H0 → m1 = … = m5"),
    html.P("H1 → ∃(r,s) ϵ {1, …, 5}  tel que mr ≠ ms"),
    html.P("nous avons pour modèle, xij = mj + eij = μ + αj + eij avec : "),
    html.P("  -  mj  = la moyenne théorique de la variable d’intérêt pour chaque modalité"),
    html.P("  -  eij = la marge d’erreur"),
    html.P("  -  μ = la moyenne générale"),
    html.P("  -  αj = effet du niveau j du facteur niveau de poste"),
    html.P("Sous l’hypothèse H0: le niveau de poste n’a pas d’influence sur le nombre de mails reçus et envoyés d’une "
           "personne, la variable aléatoire F suit la loi de Fisher à (4, 98) degré de liberté. Nous fixons un risque "
           "d’erreur de première espèce de 5 %. Nous avons la pvalue = 0.480406 ce qui est supérieur à 5%, "
           "nous ne rejetons donc pas H0. Nous n’avons donc pas mis en évidence de lien entre le poste et le nombre "
           "de mails reçus et envoyés."),
    html.P("Finalement, cette Anova nous a permis de confirmer qu’il n’y avait pas de lien entre le poste et le "
           "nombre de mails envoyés et le poste de l'employé.")

])

print("... ouverture data_constructed_job.csv en cours ...")
print("... anova strenght job en cours")
dataFrame = pd.read_csv("../data/data_constructed_job.csv", sep=",", low_memory=False)

fig = px.box(dataFrame, x='JobLevel', y='strength')

model = ols('strength ~ JobLevel', data=dataFrame).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
