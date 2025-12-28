from app.services.search_service import search_duckduckgo

results = search_duckduckgo("react state management", limit=5)

print("Results:", results)
print("Count:", len(results))
