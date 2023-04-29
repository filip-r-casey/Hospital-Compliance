import pandas as pd
from sqlalchemy import create_engine
import io

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()

df_features = pd.read_csv("./data/hospitals.csv")
df_links = pd.read_csv("./data/machine_readable_links.csv")
df_links["csv_headers"] = None

subset_features = df_features.loc[
    :,
    ["bed_count", "zip_code", "medicare_medicaid_eligible", "ccn"],
]
subset_features = subset_features.dropna()
subset_features = subset_features.drop_duplicates("ccn")

subset_links = df_links.loc[
    :,
    [
        "ccn",
        "state_or_region",
        "reporting_entity_name_common",
        "machine_readable_url",
        "csv_headers",
        "meets_standard",
    ],
]

subset_links["meets_standard"] = subset_links["meets_standard"].fillna(True)
subset_links = subset_links.dropna(
    subset=[
        "ccn",
        "state_or_region",
        "reporting_entity_name_common",
        "machine_readable_url",
        "meets_standard",
    ]
)
# subset_links = subset_links.drop_duplicates("ccn")

# subset_links.to_csv(output, sep="\t", header=False, index=False)
# output.seek(0)
# contents = output.getvalue()
# cur.copy_from(output, "machine_links", null="")  # null values become ''
# conn.commit()

cur.execute("SELECT ccn FROM machine_links")
res = cur.fetchall()

res = [x[0] for x in res]

subset_features = subset_features[subset_features["ccn"].isin(res)]

subset_features.to_csv(output, sep="\t", header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, "features", null="")  # null values become ''
conn.commit()

cur.close()
conn.close()
