from pydantic import BaseModel
from datetime import datetime


class TopicOut(BaseModel):
    id : int
    title : str
    description : str
    slug : str
    created_at : datetime

    class Config:
        from_attributes = True

