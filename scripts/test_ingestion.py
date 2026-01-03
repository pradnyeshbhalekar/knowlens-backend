from app.core.db_dependency import get_db
from app.services.ingestion_service import ingest_topic_if_new

db = next(get_db())

result = ingest_topic_if_new(
    db,
    "React State Management",
    limit=5
)

print(result)
