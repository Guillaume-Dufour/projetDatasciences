import dash_table
from pandas import *
import prince
from plotly.express import scatter
from plotly.express import bar
import dash_html_components as html
import dash_core_components as dcc

print("... ouverture data_afc_afc_job_job_extern_final.csv en cours ...")
print("... afc job job en cours ...")
dataFrame = pandas.read_csv("../data/data_afc_job_job_extern_final.csv", sep=",", low_memory=False)

X = "job_sender"
Y = "job_receiver"
cont = dataFrame[[X, Y]].pivot_table(index=X, columns=Y, aggfunc=len).fillna(0).copy().astype(int)

pandas.set_option('display.float_format', lambda x: '{:.6f}'.format(x))

df = pandas.DataFrame(
    data=cont.values,
    columns=pandas.Series(cont.columns.values),
    index=pandas.Series(cont.index.values)
)

display_contingence_tab = {
    "job_sender/job_receiver": [],
    "Associate":[],
    "Employee": [],
    "Executive": [],
    "Extern": [],
    "Manager": []
}

for index, row in df.iterrows():
    display_contingence_tab["job_sender/job_receiver"].append(index)
    display_contingence_tab["Associate"].append(row[0])
    display_contingence_tab["Employee"].append(row[1])
    display_contingence_tab["Executive"].append(row[2])
    display_contingence_tab["Extern"].append(row[3])
    display_contingence_tab["Manager"].append(row[4])

display_contingence_frame = pandas.DataFrame(data=display_contingence_tab)


ca = prince.CA(
    n_components=2,
    n_iter=3,
    copy=True,
    check_input=True,
    engine="auto"
)

ca.fit(df)
row = ca.row_coordinates(df)
column = ca.column_coordinates(df)

d = {
    "name": [],
    "dim1": [],
    "dim2": [],
    "type": []
}

for index, r in row.iterrows():
    d["name"].append(index)
    d["dim1"].append(r[0])
    d["dim2"].append(r[1])
    d["type"].append("sender")

for index, c in column.iterrows():
    d["name"].append(index)
    d["dim1"].append(c[0])
    d["dim2"].append(c[1])
    d["type"].append("receiver")

complete = pandas.DataFrame(data=d)

eigen_value = {
    "value": [],
    "dim": [],
    "percentage": []
}

eigen_value["value"].append(ca.eigenvalues_[0])
eigen_value["value"].append(ca.eigenvalues_[1])
eigen_value["dim"].append("1")
eigen_value["dim"].append("2")
eigen_value["percentage"].append(round(ca.eigenvalues_[0] / ca.total_inertia_, 3)*100)
eigen_value["percentage"].append(round(ca.eigenvalues_[1] / ca.total_inertia_, 3)*100)

df_eigen_value = pandas.DataFrame(data=eigen_value)

fig_afc = scatter(complete, x="dim1", y="dim2", text="name", color="type",
                  labels={
                     "dim1": "dim 1 : ( " + str(df_eigen_value['percentage'][0]) + "%)",
                     "dim2": "dim 2 : ( " + str(df_eigen_value['percentage'][1]) + "%)",
                     "type": ""
                 })
fig_afc.update_traces(textposition='top center')

fig_eigen_value = bar(df_eigen_value, x='dim', y='percentage')

ax = ca.plot_coordinates(
    X=df,
    ax=None,
    figsize=(5, 5),
    x_component=0,
    y_component=1,
    show_row_labels=True,
    show_col_labels=True
)

ki2 = ca.total_inertia_ * len(dataFrame.index)

resultat = html.Div([

    html.Br(),
    html.P("Nous nous sommes aussi demandés si le poste dans l’entreprise  avait une influence sur les "
           "personnes avec qui ils communiquent. Par exemple, nous voulions savoir si les personnes haut "
           "placées communiquent plus avec des personnes extérieures à l’entreprise que les employés."),
    html.Br(),
    html.P(
        "Pour vérifier cela, nous avons donc réalisé une Analyse Factorielle des Correspondances entre le niveau de "
        "poste de l’expéditeur du mail et le niveau de poste du destinataire du mail. Il faut savoir que nous avons "
        "éliminé les mails envoyés entre 20h et 8h le lendemain afin d’éviter d’être pollué par les mails "
        "automatiques (qui sont présents en très grand nombre et nous n’avons pas pour but de créer un algorithme "
        "capable de les identifier dans le cadre de ce projet). Nous avons aussi remarqué qu’il y avait une grande "
        "quantité de mails envoyés et reçus par des  externes (adresse mail qui n’a pas pour domaine enron.com), "
        "nous ne savons pas comment ce genre de mail peuvent être présents dans les dossiers que nous avons récupéré "
        "au départ et nous sommes conscients que leur omniprésence influe sur le résultat de l’AFC."),
    html.P("tableau de contingence",
           style={'text-decoration': 'underline', 'text-align': 'center'}),
    dash_table.DataTable(
        id='tab_contingence',
        columns=[{"name": i, "id": i} for i in display_contingence_frame.columns],
        data=display_contingence_frame.to_dict("records")
    ),

    html.P("valeurs propres",
           style={'text-decoration': 'underline', 'text-align': 'center'}),
    dash_table.DataTable(
        id='eigen_value',
        columns=[{"name": i, "id": i} for i in df_eigen_value.columns],
        data=df_eigen_value.to_dict("records")
    ),

    html.P(" Nous avons, dans un premier temps, étudié la valeur du ki2 : "),
    html.P("valeur du χ²",
           style={'text-decoration': 'underline', 'text-align': 'center'}),
    html.P("χ² = "+str(ki2)),
    html.P("Soit l’hypothèse H0 : les deux variables sont indépendantes. "
           "Sous H0, la variable aléatoire du χ² suit la loi du χ² à (I - 1)(J - 1) (16 dans notre cas) "
           "degré de liberté. On se fixe un risque d’erreur de première espèce de 5 %. "
           "Ceci implique que le seuil est égal à 34.27. Nous avons la réalisation du χ² = 8 872.79 > 34.27, "
           "ce qui signifie que je réfute H0 avec un risque de première espèce de 5 %. "
           "On conclut donc qu’il n’y a pas d’indépendance entre le niveau de poste de l’expéditeur du mail "
           "et le niveau de poste du destinataire du mail."),

    html.P("pourcentage de représentation des dimensions",
           style={'text-decoration': 'underline', 'text-align': 'center'}),
    dcc.Graph(figure=fig_eigen_value),
    html.P("Par la suite, nous avons effectué un mapping simultané des points lignes et colonnes. "
           "Il était évident de ne faire qu’un graphique, portant sur la dimensions 1 et 2, "
           "ces dernières représentant à elles deux plus de 99% de l’information concernant les résultats de l’AFC.  "
           "Nous ne nous sommes pas attardés sur l’interprétation des graphiques séparés car l’interprétation "
           "sur la dimension 1 (qui représente quasiment la totalité des informations de l’AFC) est identique "
           "pour les deux (nous avons des niveaux de poste dans l’entreprise dans les deux cas). "
           "Nous pouvons constater que la dimension 1 peut représenter une certaine hiérarchie entre les niveaux "
           "de postes."),
    html.Br(),
    html.P("La librairie utilisée (Prince) ne nous permettait pas, à notre connaissance, "
           "de retourner les contributions absolues et relatives de nos modalités. Ceci est dommage au "
           "sens où nous aurions pu, de manière plus précise, analyser les dimensions ainsi que la qualité"
           " de représentation des modalités sur les axes."),

    html.P("AFC : analyse du poste du destinataire en fonction du post de l'expéditeur",
           style={'text-decoration': 'underline', 'text-align': 'center'}),
    dcc.Graph(figure=fig_afc),
    html.P("Nous avons finalement pu conclure, après extraction de différents groupes, que les personnes appartenant "
           "au même type de poste parlaient majoritairement entre elles et que les Exécutifs était légèrement exclus "
           "de la communication avec les autres niveaux de poste. Cependant nous remarquons que les associés et les "
           "employés communiquent beaucoup entre eux et peu avec les managers. Enfin, les externes communiquent "
           "majoritairement avec les associés, les employés et les managers mais pas du tout avec l'exécutif.")
])





