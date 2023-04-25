import csv
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
)

cur = conn.cursor()
cur.execute("SELECT ccn FROM machine_links")
res = cur.fetchall()

res = [x[0] for x in res]

write = csv.writer(open("hospital_clean2.csv", "w"))

with open("hospital_clean.csv", "r") as file:
    read = list(csv.reader(file))
    write.writerow(read[0])
    for row in read[1:]:
        if int(row[2]) in res:
            write.writerow(row)
