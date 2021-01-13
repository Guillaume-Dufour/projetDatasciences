import pandas as pd

#faire en sorte qu'une personne ait pas 1000 adresses différentes

def construction_mail(row): #recree mail à partir csv job
    x = row.Name.split()
    print(x)
    mail = x[0] + "." + x[1] + "@enron.com"
    mail = mail.lower()
    return mail


def traitement_dataframe(): #récup nom /job
    dataFrame = pd.read_csv("data/data_job.csv", sep=",", low_memory=False)
    dataFrame = dataFrame.groupby(['Name', 'Note', 'JobLevel'])['strength'].sum().reset_index()
    dataFrame['Mail'] = dataFrame.apply(lambda x: construction_mail(x), axis=1)
    dataFrame.to_csv("data/data_constructed_job.csv", index=False)


traitement_dataframe()
