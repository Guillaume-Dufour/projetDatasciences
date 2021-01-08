from pandas import *
import re

csv_mail = "data/data_constructed.csv"
csv_job = "data/data_job.csv"

df_mail = read_csv(csv_mail, sep=",", low_memory=False)
df_job = pandas.read_csv(csv_job, sep=",", low_memory=False)

d = {
    "job_sender": [],
    "job_receiver": []
}

for index, row in df_mail.iterrows():

    if index % 1000 == 0:
        print(index)

    if str(row['to']) != "nan" and str(row['from'] != "nan"):

        from_name = re.split("@", str(row["from"]))

        list_receiver = re.split(",", str(row["to"]))

        for receiver in list_receiver:
            to_name = re.split("@", receiver)

            df_from = df_job[df_job["Email"].str.contains(from_name[0])]["JobLevel"].values
            df_to = df_job[df_job["Email"].str.contains(to_name[0])]["JobLevel"].values

            if df_from.size != 0 and df_to.size != 0:
                d["job_sender"].append(df_from[0])
                d["job_receiver"].append(df_to[0])

df = pandas.DataFrame(data=d)

df.to_csv("data/data_annova_sender_receiver.csv", index=False)

print("Fin")
