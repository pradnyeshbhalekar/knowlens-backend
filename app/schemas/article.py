from pydantic import BaseModel
from datetime import datetime

class ArticleOut(BaseModel):
    id:int
    title:str
    url:str
    published_at:str
    content:str
    source_id:str
    topic_id:str