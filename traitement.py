from datetime import datetime
from pandas import *


def drop_duplicates(df):
    return df.drop_duplicates(subset=["Date", "From", "To"])


def filter_years(df):
    df = df.drop(df[df.Date < "2000-00-00 00:00:00"].index)
    df = df.drop(df[df.Date > "2003-00-00 00:00:00"].index)
    return df


def add_year_column(df):
    df['year'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%Y"), axis=1)
    return df


def add_month_column(df):
    df['month'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%B"), axis=1)
    return df


def add_weekday_column(df):
    df['weekDay'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%A"), axis=1)
    return df


def add_hour_column(df):
    df['hour'] = df.apply(lambda row: (datetime.fromisoformat(row.Date)).strftime("%H"), axis=1)
    return df


df = pandas.read_csv("data/data.csv", sep=",", low_memory=False)

df = drop_duplicates(df)
df = filter_years(df)
df = add_year_column(df)
df = add_month_column(df)
df = add_weekday_column(df)
df = add_hour_column(df)

df.to_csv("data/data_petit_constructed.csv", index=False)
