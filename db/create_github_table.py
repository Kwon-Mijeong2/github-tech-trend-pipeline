from sqlalchemy import create_engine
from sqlalchemy import text

DB_URL = (
    "postgresql://admin:admin123"
    "@localhost:5432/github_db"
)

engine = create_engine(DB_URL)

with open(
    "sql/create_github_table.sql",
    "r",
    encoding="utf-8"
) as f:

    sql = f.read()

with engine.connect() as conn:

    conn.execute(text(sql))
    conn.commit()

print("테이블 생성 완료")