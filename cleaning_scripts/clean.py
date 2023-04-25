import csv

with open("mrl_clean.csv", "r") as file:
    exists = []
    write = csv.writer(open("mrl_clean2.csv", "w"))
    for row in list(csv.reader(file)):
        if row[0] not in exists:
            exists.append(row[0])
            write.writerow(row)
