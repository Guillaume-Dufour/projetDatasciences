import pandas as pd
import scipy.stats as st
from fanalysis.ca import CA

# création du tableau de contingence

dataFrame = pd.read_csv("../data/data_partiel_constructed.csv", sep=",", low_memory=False)

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
print(X)
my_ca = CA(row_labels=cont.index.values, col_labels=cont.columns.values)
truc = my_ca.fit(X)
print(my_ca.eig_)
my_ca.plot_eigenvalues(type="percentage")
my_ca.mapping(num_x_axis=1, num_y_axis=2)
