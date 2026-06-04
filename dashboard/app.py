import pandas as pd
import streamlit as st

from sqlalchemy import create_engine

DB_URL = (
    "postgresql://admin:admin123"
    "@localhost:5432/github_db"
)

engine = create_engine(DB_URL)

df = pd.read_sql(
    "SELECT * FROM github_trending",
    engine
)

st.title(
    "GitHub Tech Trend Dashboard"
)

language_summary = (
    df.groupby("language")
      .agg(
          repo_count=("repository", "count"),
          total_stars=("stars", "sum")
      )
      .reset_index()
)



st.dataframe(df)

st.subheader(
    "Language Summary"
)

st.dataframe(
    language_summary
)

st.bar_chart(
    language_summary.set_index(
        "language"
    )["repo_count"]
)

top_repo = (
    df.sort_values(
        "stars",
        ascending=False
    )
    .head(10)
)

st.subheader(
    "Top Repositories"
)

st.dataframe(top_repo)