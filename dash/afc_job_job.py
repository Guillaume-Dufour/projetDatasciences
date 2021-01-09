import pandas as pd
import scipy.stats as st
from fanalysis.ca import CA
import matplotlib.pyplot as plt

df = pd.read_csv("../data/data_afc_job_job.csv", sep=",", low_memory=False)

#création du tableau de contingence
X = "job_sender"
Y = "job_receiver"
cont = df[[X, Y]].pivot_table(index=X, columns=Y, aggfunc=len).fillna(0).copy().astype(int)
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
my_ca.fit(X)
print(my_ca.eig_)
my_ca.plot_eigenvalues(type="percentage")
my_ca.mapping(num_x_axis=1, num_y_axis=2)

