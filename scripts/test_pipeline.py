from app.services.pipeline_service import search_and_extract

results = search_and_extract("Epstein files", limit=5)

print("Articles found:", len(results))

for i, article in enumerate(results, start=1):
    print(f"\n--- Article {i} ---")
    print("Title:", article.get("title"))
    print("URL:", article.get("url"))

    text = article.get("text")
    if not text:
        print("Text preview: <NO TEXT EXTRACTED>")
    else:
        print("Text preview:", text[:300])
