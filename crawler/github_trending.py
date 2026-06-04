import requests
from bs4 import BeautifulSoup

URL = "https://github.com/trending"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    URL,
    headers=headers
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

repos = soup.select("article.Box-row")

repos_data = []

for repo in repos[:5]:

    repo_name = (
        repo.select_one("h2 a")
        .text
        .strip()
        .replace("\n", "")
        .replace(" ", "")
    )

    description_tag = repo.select_one("p")

    description = (
        description_tag.text.strip()
        if description_tag
        else ""
    )

    language_tag = repo.select_one(
    '[itemprop="programmingLanguage"]'
    )

    language = (
        language_tag.text.strip()
        if language_tag
        else "Unknown"
    )
    
    star_tag = repo.select(
    "a.Link--muted"
    )

    stars = 0

    if len(star_tag) > 0:
        stars = int(
            star_tag[0]
            .text
            .strip()
            .replace(",", "")
        )

    repos_data.append(
        {
            "repository": repo_name,
            "language": language,
            "stars": stars
        }
    )

    print(
        repo_name,
        language,
        stars
    )

    from etl.save_raw import save_raw_data

    save_raw_data(repos_data)