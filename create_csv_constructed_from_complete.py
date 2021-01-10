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


csv_in = "data/data_complete.csv"

dataframe = pandas.read_csv(csv_in, sep=",", low_memory=False)

dataframe = drop_duplicates(dataframe)
dataframe = filter_years(dataframe)
dataframe = add_year_column(dataframe)
dataframe = add_month_column(dataframe)
dataframe = add_weekday_column(dataframe)
dataframe = add_hour_column(dataframe)

dataframe.to_csv("data/data_constructed.csv", index=False)
