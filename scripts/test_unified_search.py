from app.core.db_dependency import get_db
from app.services.unified_search_service import unified_search

db = next(get_db())

result = unified_search(
    db,
    "Python async await",
    limit=5
)

print("Count:", result["count"])
for article in result["articles"]:
    print("\n---")
    print(article["title"])
    print(article["url"])
