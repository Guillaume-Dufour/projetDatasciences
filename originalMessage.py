from pandas import *
import re
from datetime import datetime


def month(str_month):
    values = {
        "january": "01",
        "february": "02",
        "march": "03",
        "april": "04",
        "may": "05",
        "june": "06",
        "july": "07",
        "august": "08",
        "september": "09",
        "october": "10",
        "november": "11",
        "december": "12"
    }

    return values.get(str_month.lower())


def hour(str_hour, part):
    hour_split = re.split(":", str_hour)

    hour = int(hour_split[0])

    if part.__contains__("P"):
        hour += 12
        hour %= 24

    hour_str = "0" + str(hour) if len(str(hour)) == 1 else str(hour)

    return hour_str + ":" + hour_split[1] + ":00"


def two_digit_month(month_str):
    return "0" + month_str if len(month_str) == 1 else month_str


df = read_csv("data/df3csv.csv", sep=',', low_memory=False)

df2 = df[df['content'].str.contains("Sent:")]
df3 = df2[df2['content'].str.contains("To:")]

all_date = []

nb = 0

"""for (index, row) in df3.iterrows():
    try:

        string_split = re.split("Sent: ", row['content'])
        string_split2 = re.split("To: ", string_split[1])

        date = string_split2[0][0:-1].strip()

        if len(date) < 45:
            all_date.append(date)

    except Exception:
        nb_error += 1"""


def calcul_time_reponse(content):

    nb_errors = 0

    try:
        string_split = re.split("Sent: ", content)

        string_split2 = re.split("To: ", string_split[1])

        date = string_split2[0][0:-1].strip()

        if len(date) < 45:
            if date.__contains__("/"):
                infos = re.split("[ /]", date)
                return infos[3] + "-" + two_digit_month(infos[1]) + "-" + infos[2] + " " + hour(infos[4], infos[5])
            else:
                infos = re.split(", | ", date)
                return infos[3] + "-" + month(infos[1]) + "-" + infos[2] + " " + hour(infos[4], infos[5])
    except Exception:
        nb_errors += 1


df3['time_response'] = df3['content'].apply(lambda line: calcul_time_reponse(line))

df3.to_csv("temp.csv", index=False)


df = read_csv("data/temp.csv", sep=',', low_memory=False)

df = df.dropna(subset=['time_response'])


def nb_seconds(values):
    diff = datetime.fromisoformat(values.Date) - datetime.fromisoformat(values.time_response)
    return diff.total_seconds()


df['time'] = df[['Date', 'time_response']].apply(lambda x: nb_seconds(x), axis=1)

df.to_csv("temp.csv", index=False)


"""for value in all_date:
    if value.__contains__("/"):
        print(value)"""

"""string_date = "Mon 9/24/2001 9:13 AM >"

infos = re.split("[ /]", string_date)

print(infos)"""

# print(infos[3] + "-" + two_digit_month(infos[1]) + "-" + infos[2] + " " + hour(infos[4], infos[5]))

"""date1 = "2000-10-17 09:26:00"
date3 = "2000-10-17 10:33:00"
date2 = infos[3] + "-" + month(infos[1]) + "-" + infos[2] + " " + hour(infos[4], infos[5])

diff = datetime.fromisoformat(date3) - datetime.fromisoformat(date1)
diff_in_s = diff.total_seconds()
minutes = divmod(diff_in_s, 60)[0]

print(diff_in_s)
print(minutes)"""
