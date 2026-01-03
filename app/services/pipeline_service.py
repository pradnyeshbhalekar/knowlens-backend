from app.services.search_service import search_duckduckgo
from app.extractors.generic import extract_article
from app.utils.url import normalize_ddg_url

def search_and_extract(query:str,limit: int =5) -> list[dict]:
    search_results = search_duckduckgo(query,limit=limit)

    final_results = []

    for result in search_results:
        raw_url = result.get('url')
        title = result.get('title')

        if not raw_url:
            continue

        url = normalize_ddg_url(raw_url)

        article = extract_article(url)

        final_results.append({
            "title":title,
            "url":url,
            "text":article["text"] 
        })
    return final_results