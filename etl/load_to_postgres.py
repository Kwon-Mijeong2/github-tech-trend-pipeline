from glob import glob
import os

import pandas as pd

from sqlalchemy import create_engine

DB_URL = (
    "postgresql://admin:admin123"
    "@localhost:5432/github_db"
)

engine = create_engine(DB_URL)

files = glob("data/raw/*.csv")

latest_file = max(
    files,
    key=os.path.getctime
)

df = pd.read_csv(latest_file)

df["collected_date"] = pd.Timestamp.now().date()

df.to_sql(
    "github_trending",
    engine,
    if_exists="append",
    index=False
)

print(
    f"{len(df)}건 적재 완료"
)