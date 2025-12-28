from sqlalchemy import Column,Integer,String,Text,DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Topic(Base):
    __tablename__  = "topics"

    id = Column(Integer,primary_key=True,index = True)
    title = Column(String(255),nullable=False)
    description = Column(String(255),nullable=True)
    slug = Column(String(255),unique=True,index=True)

    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),server_onupdate=func.now())
    
