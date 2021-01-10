import threading
import re
from pandas import *
import numpy as np


class ThreadCSV(threading.Thread):

    def __init__(self, df_mail, df_job, begin, end, number):
        threading.Thread.__init__(self)

        self.df_mail = df_mail
        self.df_job = df_job
        self.begin = begin
        self.end = end
        self.number = number

    def run(self):

        nb_errors = 0

        d = {
            "job_sender": [],
            "job_receiver": []
        }

        for index, row in self.df_mail.iterrows():

            try:

                if self.begin <= index < self.end:

                    if index % 1000 == 0:
                        print(self.number, index)

                    if 8 <= int(row['hour']) <= 20:

                        if str(row['to']) != "nan" and str(row['from'] != "nan"):

                            from_name = re.split("@", str(row["from"]))

                            list_receiver = re.split(",", str(row["to"]))

                            for receiver in list_receiver:
                                to_name = re.split("@", receiver)

                                df_from = self.df_job[self.df_job["Email"].str.contains(from_name[0])][
                                    "JobLevel"].values

                                if from_name[1] != "enron.com":
                                    df_from = np.append(df_from, "Extern")

                                df_to = self.df_job[self.df_job["Email"].str.contains(to_name[0])]["JobLevel"].values

                                if to_name[1] != "enron.com":
                                    df_to = np.append(df_to, "Extern")

                                if df_from.size != 0 and df_to.size != 0:
                                    d["job_sender"].append(df_from[0])
                                    d["job_receiver"].append(df_to[0])
            except Exception:
                nb_errors += 1
                print(nb_errors)

        df = pandas.DataFrame(data=d)

        df.to_csv("data_afc_job_job/data_afc_job_job" + str(self.number) + ".csv", index=False)


csv_mail = "data/data_constructed.csv"
csv_job = "data/data_job.csv"

df_mail = pandas.read_csv(csv_mail, sep=",", low_memory=False)
df_job = pandas.read_csv(csv_job, sep=",", low_memory=False)

threads = []

debut = 0
fin = 25000

for i in range(0, 10):
    threads.append(ThreadCSV(df_mail, df_job, debut, fin, i+1))
    debut += 25000
    fin += 25000


for t in threads:
    t.start()