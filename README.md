# GitHub Tech Trend Pipeline

GitHub Trending 데이터를 수집하고 PostgreSQL에 적재한 후 Streamlit으로 시각화하는 데이터 파이프라인 프로젝트입니다.

## Tech Stack

- Python
- Requests
- BeautifulSoup
- Pandas
- PostgreSQL
- SQLAlchemy
- Streamlit
- Docker

## Architecture

GitHub Trending
↓
Crawler
↓
CSV
↓
PostgreSQL
↓
Streamlit Dashboard

## Features

- GitHub Trending 데이터 수집
- CSV 저장
- PostgreSQL 적재
- 언어별 기술 트렌드 분석
- Streamlit 대시보드 제공

## Run

```bash
pip install -r requirements.txt
