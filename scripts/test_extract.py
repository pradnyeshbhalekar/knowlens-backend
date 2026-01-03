from app.extractors.generic import extract_article

url = "https://www.bbc.com/news/articles/c8r38ne1x2mo"

article = extract_article(url)

print("Success:", article["success"])
print("Title:", article["title"])
print("Text preview:", article["text"])
