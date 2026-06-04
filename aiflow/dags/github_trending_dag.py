from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="github_trending_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    crawl_task = BashOperator(
        task_id="crawl_github",
        bash_command=(
            "cd C:/Users/SAMSUNG/github-tech-trend-pipeline "
            "&& python -m crawler.github_trending"
        )
    )