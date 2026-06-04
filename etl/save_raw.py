import os
from datetime import datetime

import pandas as pd


def save_raw_data(data):

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    today = datetime.now().strftime(
        "%Y%m%d"
    )

    file_path = (
        f"data/raw/github_trending_{today}.csv"
    )

    df = pd.DataFrame(data)

    df.to_csv(
        file_path,
        index=False,
        encoding="utf-8-sig"
    )

    print(
        f"저장 완료: {file_path}"
    )