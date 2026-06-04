import requests

url = "https://github.com/trending"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers
)

print(response.status_code)
print(response.text[:500])