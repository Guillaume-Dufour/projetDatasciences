import pandas as pd
import scipy.stats as st
from fanalysis.ca import CA
from matplotlib import pyplot
from plotly.express import scatter

# création du tableau de contingence

dataFrame = pd.read_csv("../data/data_constructed.csv", sep=",", low_memory=False)

X = "hour"
Y = "weekDay"
cont = dataFrame[[X, Y]].pivot_table(index=X, columns=Y, aggfunc=len).fillna(0).copy().astype(int)
print(cont)

# test du ki2
st_chi2, st_p, st_dof, st_exp = st.chi2_contingency(cont)
print("st_chi2")
print(st_chi2)
print("st_p")
print(st_p)

# AFC
X = cont.values
#print(X)
my_ca = CA(row_labels=cont.index.values, col_labels=cont.columns.values)
my_ca.fit(X)
print(my_ca)
#print(my_ca.eig_)
df_cols = my_ca.col_topandas()
df_row = my_ca.row_topandas()
print(df_cols)
my_ca.plot_eigenvalues(type="percentage")
fig = pyplot.figure()
my_ca.mapping(num_x_axis=1, num_y_axis=2)
text = [i for i in df_cols.index.values]
print(text)

def test():
    fig = scatter(df_cols, x="col_coord_dim1", y="col_coord_dim2", text=text)
    return fig

test()