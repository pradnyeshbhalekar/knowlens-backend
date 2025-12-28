from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.core.db_dependency import get_db
from app.models.topic import Topic
from app.schemas.topic import TopicOut

router = APIRouter(prefix='/topics',tags=['Topics'])


@router.get('/',response_model=list[TopicOut])
def get_topic(db:Session = Depends(get_db)):
    return db.query(Topic).order_by(Topic.created_at.desc()).all()

@router.get('/{topic_id}',response_model=TopicOut)
def get_topics(topic_id: int,db:Session = Depends(get_db)):
    topic =  db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        return HTTPException(status_code=404,detail="Topic not found")
    return topic

