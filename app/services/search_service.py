import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from app.utils.url import normalize_ddg_url

DDG_URL = "https://duckduckgo.com/html/?q="

def search_duckduckgo(query: str, limit: int = 5) -> list[dict]:
    encoded_query = quote_plus(query)
    url = DDG_URL + encoded_query

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for a in soup.select("div.results a.result__a"):
        title = a.get_text(strip=True)
        link = normalize_ddg_url(a.get("href"))

        if not title or not link:
            continue

        results.append({
            "title": title,
            "url": link
        })

        if len(results) >= limit:
            break

    return results
