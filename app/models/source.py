from sqlalchemy import Column,String,Integer,Boolean,DateTime
from sqlalchemy.sql import func
from app.core.db import Base

class Source(Base):
    __tablename__ = 'sources'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),nullable=False)
    baseurl = Column(String(500),nullable=False)

    reputation_score = Column(Integer)
    is_primary = Column(Boolean,default=False)
    is_active = Column(Boolean,default=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())