import os
import re
from email.parser import Parser
from pandas import *
from utils import month
from utils import two_digit_string

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

    d["message-id"].append(email['message-id'])
    d["from"].append(email['from'])
    d["to"].append(email['to'])
    d["date"].append(date_str)
    d["subject"].append(email['subject'])
    d["x-origin"].append(email['x-origin'])
    d["content"].append(email.get_payload().strip())


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

df.to_csv("data/data_complete.csv", index=True)
