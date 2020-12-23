from matplotlib import pyplot
from pandas import *
from matplotlib import *
from datetime import datetime

def dropLine (csvIn, csvOut) :
    df = pandas.read_csv(csvIn, sep=',', low_memory=False)
    df = df.drop_duplicates(subset=["Date", "From", "To"])
    df = df.drop(df[df.Date < "2000-00-00 00:00:00"].index)
    df = df.drop(df[df.Date > "2003-00-00 00:00:00"].index)
    df.to_csv(csvOut, index=False)

def dropColumn (csvIn, csvOut) :
    df = pandas.read_csv(csvIn, sep=',', low_memory=False)
    for x in range(1, 13):
        df = df.drop(columns=['Cat_' + str(x) + '_weight'])
        for y in range(1, 3):
            df = df.drop(columns=['Cat_' + str(x) + '_level_' + str(y)])
    df.to_csv(csvOut, index=False)

def addYear (csvIn, csvOut) :
    df = pandas.read_csv(csvIn, sep=',', low_memory=False)
    df['year'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%Y"), axis=1)
    df.to_csv(csvOut, index=False)

def addHour (csvIn, csvOut) :
    df = pandas.read_csv(csvIn, sep=',', low_memory=False)
    df['hour'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%H"), axis=1)
    df.to_csv(csvOut, index=False)

def addWeekDay (csvIn, csvOut) :
    df = pandas.read_csv(csvIn, sep=',', low_memory=False)
    df['weekDay'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%A"), axis=1)
    df.to_csv(csvOut, index=False)


