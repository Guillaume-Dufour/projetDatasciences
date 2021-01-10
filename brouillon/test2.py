from pandas import *
import prince

dataFrame = pandas.read_csv("../data/data_constructed.csv", sep=",", low_memory=False)

X = "hour"
Y = "weekDay"
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

ax = ca.plot_coordinates(
    X=df,
    ax=None,
    figsize=(5, 5),
    x_component=0,
    y_component=1,
    show_row_labels=True,
    show_col_labels=True
)

fig = ax.get_figure().savefig("img2.png")




