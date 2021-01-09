import pandas as pd
import re

def contructionMail (row):
    x = row.Name.split()
    print(x)
    mail = x[0]+"."+x[1]+"@enron.com"
    mail = mail.lower()
    return mail

def traitementDataFrame ():
    dataFrame = pd.read_csv("data/data_job.csv", sep=",", low_memory=False)
    dataFrame = dataFrame.groupby(['Name', 'Note', 'JobLevel'])['strength'].sum().reset_index()
    dataFrame['Mail'] = dataFrame.apply(lambda x: contructionMail(x),
                                        axis=1)
    print(dataFrame)
    dataFrame.to_csv("data/data_constructed_job.csv", index=False)

pattern = re.compile("^[a-z]+.[a-z]+@enron.com$")
df = pd.read_csv("data/data_complete.csv", sep=",", low_memory=False)
df = df.drop(df[pattern.match(df.to)].index)
df.to_csv("data/data_entreprise_only.csv")
