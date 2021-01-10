from pandas import *
import re
from datetime import datetime
import numpy as np
from utils import month
from utils import two_digit_string

data_csv = "data/data_constructed.csv"


def create_response_csv(csv_in):
    substring = "-Original Message-"

    df = pandas.read_csv(csv_in, sep=",", low_memory=False)
    df = df.dropna(subset=['content'])
    df2 = df[df['content'].str.contains(substring)]

    df2.to_csv("data_response.csv", index=False)


def hour(str_hour, part):
    hour_split = re.split(":", str_hour)

    hour = int(hour_split[0])

    if part.__contains__("P"):
        hour += 12
        hour %= 24

    hour_str = "0" + str(hour) if len(str(hour)) == 1 else str(hour)

    return hour_str + ":" + hour_split[1] + ":00"


def calcul_data_response(content):
    nb_errors = 0

    try:
        string_split = re.split("Sent: ", content)

        string_split2 = re.split("To: ", string_split[1])

        date = string_split2[0][0:-1].strip()

        if len(date) < 45:
            if date.__contains__("/"):
                infos = re.split("[ /]", date)
                return infos[3] + "-" + two_digit_string(infos[1]) + "-" + two_digit_string(infos[2]) + " " + hour(
                    infos[4], infos[5])
            else:
                infos = re.split(", | ", date)
                return infos[3] + "-" + month(infos[1]) + "-" + two_digit_string(infos[2]) + " " + hour(infos[4],
                                                                                                        infos[5])
    except Exception:
        nb_errors += 1


def insert_date_original_message_response(csv_in):
    df = pandas.read_csv(csv_in, sep=",", low_memory=False)

    df["date_original_message"] = df["content"].apply(lambda line: calcul_data_response(line))

    df.to_csv("data/data_response_V2.csv", index=False)


def nb_seconds(date_end, date_begin):
    nb_errors = 0

    try:
        diff = datetime.fromisoformat(date_end) - datetime.fromisoformat(date_begin)
        return diff.total_seconds()
    except Exception:
        nb_errors += 1


def calcul_time_response_csv(csv_in):
    df = pandas.read_csv(csv_in, sep=",", low_memory=False)
    df = df.dropna(subset=['date_original_message'])
    df['time_response'] = df.apply(lambda row: nb_seconds(row.date, row.date_original_message), axis=1)
    df.to_csv("data/data_time_response.csv", index=False)


def filter_time_response(df):
    return df[df["time_response"] >= 0]


csv_mail = "data/data_time_response.csv"
csv_job = "data/data_job.csv"

df_job = pandas.read_csv(csv_job, sep=",", low_memory=False)
df_mail = pandas.read_csv(csv_mail, sep=",", low_memory=False)

df_mail = filter_time_response(df_mail)

d = {
    "job_answerer": [],
    "time_response": []
}

for index, row in df_mail.iterrows():

    if str(row['from'] != "nan"):
        from_name = re.split("@", str(row["from"]))

        df_from = df_job[df_job["Email"].str.contains(from_name[0])]["JobLevel"].values

        if from_name[1] != "enron.com":
            df_from = np.append(df_from, "Extern")

        if df_from.size != 0:
            d["time_response"].append(row["time_response"])
            d["job_answerer"].append(df_from[0])

df_res = pandas.DataFrame(data=d)

df_res.to_csv("data/data_annova_job_time_response.csv", index=False)
