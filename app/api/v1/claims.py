from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,HTTPException

from app.core.db_dependency import get_db
from app.models import Topic,Article,Claim,Source


router = APIRouter(prefix='/claims',tags=['Claims'])

@router.get('/by-topic/{topic_id}')
def get_claims_by_topic(topic_id:int,db:Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()

    if not topic:
        raise HTTPException(status_code=404,detail='Topic not found')
    
    rows = (
        db.query(
            Claim.id.label("claim_id"),
            Claim.text.label("claim_text"),
            Claim.normalized_text,
            Claim.article_id,
            Article.title.label("article_title"),
            Article.url.label("article_url"),
            Source.id.label("source_id"),
            Source.name.label("source_name"),
        )
        .join(Article, Claim.article_id == Article.id)
        .join(Source, Article.source_id == Source.id)
        .filter(Article.topic_id == topic_id)
        .order_by(Claim.id.asc())
        .all()
    )

    return{
        "topic":{
            "id": topic.id,
            "title":topic.title,
        },
        "total_claims":len(rows),
        "claims": [dict(r._mapping) for r in rows],
    }