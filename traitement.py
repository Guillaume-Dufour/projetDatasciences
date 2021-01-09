from datetime import datetime
from pandas import *

df = pandas.read_csv("data/data_complete.csv", sep=',', low_memory=False)

def drop_duplicates(df):
    return df.drop_duplicates(subset=["date", "from", "to"])


def filter_years(df):
    df = df.drop(df[df.date < "1999-00-00 00:00:00"].index)
    df = df.drop(df[df.date > "2003-00-00 00:00:00"].index)
    return df


def add_year_column(df):
    df['year'] = df.apply(lambda row: (datetime.fromisoformat(row.date)).strftime("%Y"), axis=1)
    return df


def add_month_column(df):
    df['month'] = df.apply(lambda row: (datetime.fromisoformat(row.date)).strftime("%B"), axis=1)
    return df


def add_weekday_column(df):
    df['weekDay'] = df.apply(lambda row: (datetime.fromisoformat(row.date)).strftime("%A"), axis=1)
    return df


def add_hour_column(df):
    df['hour'] = df.apply(lambda row: (datetime.fromisoformat(row.date)).strftime("%H"), axis=1)
    return df

df = filter_years(df)
df = drop_duplicates(df)
add_hour_column(df)
add_weekday_column(df)
add_month_column(df)
add_year_column(df)
df.to_csv("data_constructed.csv", index = False)
