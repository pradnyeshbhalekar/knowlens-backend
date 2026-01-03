from app.core.db_dependency import get_db
from app.services.retrieval_service import get_articles_by_topic

db = next(get_db())

result = get_articles_by_topic(
    db,
    "React State Management"
)

print("Found:", result["found"])
print("Count:", result.get("count"))

for article in result["articles"]:
    print("\n---")
    print(article["title"])
    print(article["url"])
