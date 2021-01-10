from pandas import *
import prince
from plotly.express import scatter
from plotly.express import bar
import dash_html_components as html
import dash_core_components as dcc

dataFrame = pandas.read_csv("../data/data_afc_job_job.csv", sep=",", low_memory=False)

X = "job_sender"
Y = "job_receiver"
cont = dataFrame[[X, Y]].pivot_table(index=X, columns=Y, aggfunc=len).fillna(0).copy().astype(int)

pandas.set_option('display.float_format', lambda x: '{:.6f}'.format(x))

df = pandas.DataFrame(
    data=cont.values,
    columns=pandas.Series(cont.columns.values),
    index=pandas.Series(cont.index.values)
)

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
    "dim": [],
    "percentage": []
}

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
                 },
                  title="AFC : analyse du poste du destinataire en fonction du poste de l'expéditeur")
fig_afc.update_traces(textposition='top center')

fig_eigen_value = bar(df_eigen_value, x='dim', y='percentage', title="pourcentage de représentation des dimensions")

ax = ca.plot_coordinates(
    X=df,
    ax=None,
    figsize=(5, 5),
    x_component=0,
    y_component=1,
    show_row_labels=True,
    show_col_labels=True
)

print(ca.eigenvalues_)
print("ki2", ca.total_inertia_, len(dataFrame.index), ca.total_inertia_ * len(dataFrame.index))
print("dim1", round(ca.eigenvalues_[0] / ca.total_inertia_, 3))
print("dim2", round(ca.eigenvalues_[1] / ca.total_inertia_, 3))

resultat = html.Div([
    dcc.Graph(figure=fig_eigen_value),
    dcc.Graph(figure=fig_afc)
])




