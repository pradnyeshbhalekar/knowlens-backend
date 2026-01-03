from sqlalchemy.orm import Session
from app.services.retrieval_service import get_articles_by_topic
from app.services.ingestion_service import ingest_topic_if_new
from app.models.topic import Topic

def slugify(text:str) -> str:
    return text.lower().strip().replace(" ","-")


def unified_search(db:Session,topic_input:str,limit:int = 5 ) -> dict :
    slug = slugify(topic_input)

    topic = (
        db.query(Topic).filter(Topic.slug == slug).first()
    )

    if not topic:
        ingestion_result = ingest_topic_if_new(db,topic_input,limit=limit)
        if not ingestion_result.get("ingested"):
            return {
                "topic":topic_input,
                "slug":slug,
                "ingested":False,
                "reason":"Failed to ingest topic"
            }
    
    retrieval_result = get_articles_by_topic(db,topic_input)


    return{
        "topic":retrieval_result['topic'],
        "slug":retrieval_result['slug'],
        "count":retrieval_result.get('count',0),
        "articles":retrieval_result.get("articles",[])
    }