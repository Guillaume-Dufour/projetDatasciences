import os
import re
from email.parser import Parser
from pandas import *
from datetime import datetime

print(datetime.now())

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
    date_split = re.split(" ", email['date'])
    date = date_split[3] + "-" + month(date_split[2]) + "-" + date_split[1] + " " + date_split[4]

    d["message-id"].append(email['message-id'])
    d["from"].append(email['from'])
    d["to"].append(email['to'])
    d["date"].append(date)
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


for (directory, subdirectory, files) in os.walk(rootdir):
    for name in files:
        path = directory.replace("\\", "/")
        path = path + "/" + name
        write_file_in_data(path)

df = pandas.DataFrame(data=d)

df.to_csv("big_data2.csv", index=True)

print(datetime.now())