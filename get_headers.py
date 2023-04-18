import csv
import urllib3
import psycopg2


def get_headers(f):
    # f: csv file object
    # returns list of csv headers
    f.readline()
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames

    return headers


def parse_mrf(url):
    # url: link to machine readable file
    response = urllib3.urlopen(url)

    return get_headers(response)


dsn = {}

conn = psycopg2.connect(dsn)
cur = conn.cursor()

res = cur.execute(
    "SELECT ccn, machine_readable_url FROM machine_readable_links"
).fetchall()

for row in res:
    ccn = row[0]
    headers = parse_mrf(row[1])

    cur.execute(
        "UPDATE machine_readable_links SET csv_header=%s WHERE ccn=%s", (headers, ccn)
    )
    conn.commit()


cur.close()
conn.close()
