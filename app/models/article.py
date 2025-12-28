from sqlalchemy import Column,String,Integer,Boolean,Text,ForeignKey,UniqueConstraint,DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer,primary_key=True,index=True)
    topic_id = Column(Integer,ForeignKey('topics.id',ondelete='CASCADE'))
    source_id = Column(Integer,ForeignKey('sources.id',ondelete='CASCADE'))

    title = Column(String(500),nullable=False)
    url = Column(String(500),nullable=False)
    published_at = Column(DateTime(timezone=True))
    content = Column(Text)

    created_at = Column(DateTime(timezone=True),server_default=func.now())

    __table_args__ = (
        UniqueConstraint("source_id","url",name="uq_source_url"),
    )