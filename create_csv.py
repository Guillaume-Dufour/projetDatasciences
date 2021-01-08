import os
import re
from email.parser import Parser
from pandas import *
import time

debut = time.process_time()

rootdir = "maildir"

d = {
    "message-id": [],
    "from": [],
    "to": [],
    "date": [],
    "subject": [],
    "x-origin": [],
    "content": []
}


def write_file_in_data(filename):
    with open(filename, "r") as file:
        data = file.read()

    email = Parser().parsestr(data)
    date_str = parse_date(email['date'])
    """date_split = re.split(" ", email['date'])
    date = date_split[3] + "-" + month(date_split[2]) + "-" + two_digit_string(date_split[1]) + " " + date_split[4]"""

    d["message-id"].append(email['message-id'])
    d["from"].append(email['from'])
    d["to"].append(email['to'])
    d["date"].append(date_str)
    d["subject"].append(email['subject'])
    d["x-origin"].append(email['x-origin'])
    d["content"].append(email.get_payload().strip())


def month(str_month):
    values = {
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12"
    }

    return values.get(str_month.lower())


def two_digit_string(string):
    return "0" + string if len(string) == 1 else string


def parse_date(raw_date):
    date_split = re.split("\\(", raw_date)
    elements = re.split(" ", date_split[0])

    decalage = int(elements[5][0:-2])

    time_split = re.split(":", elements[4])
    hour = (int(time_split[0]) - decalage) % 24

    return elements[3] + "-" + month(elements[2]) + "-" + two_digit_string(elements[1]) + " " + two_digit_string(
        str(hour)) + ":" + time_split[1] + ":" + time_split[2]


for (directory, subdirectory, files) in os.walk(rootdir):
    for name in files:
        path = directory.replace("\\", "/")
        path = path + "/" + name
        write_file_in_data(path)

df = pandas.DataFrame(data=d)

df.to_csv("data_complete_V2.csv", index=True)

fin = time.process_time()

print("Temps d'exécution : " + str(fin - debut))
