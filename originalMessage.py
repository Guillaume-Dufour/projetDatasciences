from pandas import *
import re
from datetime import datetime

df = read_csv("df3csv.csv", sep=',', low_memory=False)

df2 = df[df['content'].str.contains("Sent:")]
df3 = df2[df2['content'].str.contains("To:")]

all_date = []

nb_error = 0

nb = 0

for (index, row) in df3.iterrows():
    try:

        string_split = re.split("Sent: ", row['content'])
        string_split2 = re.split("To: ", string_split[1])

        date = string_split2[0][0:-1].strip()

        if len(date) < 40:
            all_date.append(date)

    except Exception:
        nb_error += 1

"""for value in all_date:
    if not value.__contains__("/"):
        print(value)"""

"""string_date = "Tuesday, November 13, 2001 4:17 PM"

infos = re.split(", | ", string_date)"""


"""def month(str_month):
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

    return str(hour) + ":" + hour_split[1] + ":00"


date1 = "2000-10-17 09:26:00"
date3 = "2000-10-17 10:33:00"
date2 = infos[3] + "-" + month(infos[1]) + "-" + infos[2] + " " + hour(infos[4], infos[5])

diff = datetime.fromisoformat(date3) - datetime.fromisoformat(date1)
diff_in_s = diff.total_seconds()
minutes = divmod(diff_in_s, 60)[0]

print(diff_in_s)
print(minutes)"""


