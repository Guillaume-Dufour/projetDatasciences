from pandas import *

df = pandas.read_csv("data.csv", sep=',', low_memory=False)


#combien les colonnes weights sont remplies
def compter_weight(i):
    dataframe = df.groupby(by=['Cat_'+str(i)+'_weight'], dropna=False).count()
    print(dataframe)

#idem pour la colonne level
def compter_level(i, j):
    dataframe = df.groupby(by=['Cat_'+str(i)+'_level_'+str(j)], dropna=False).count()
    print(dataframe)


for x in range(1, 13): #13 exclu
    for y in range(1, 3):
        compter_level(x, y)
""""""
df2 = df.drop_duplicates(subset=["Date", "From", "To"]) #supprime les doublons

df2.to_csv('dataV2.csv', index=False) #écrire dans le csv les données sans doublons
""""""

from datetime import datetime
x = datetime.fromisoformat("2000-08-22 14:44:00") #converti date en datetime

print(x.strftime("%A")) #donne le jour en lettres de la date
print(x.weekday()) #donne le jour de la date en chiffre
