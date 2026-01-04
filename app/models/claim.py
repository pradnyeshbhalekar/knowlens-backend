from sqlalchemy import Column,ForeignKey,Integer,DateTime,Text,Boolean,Date
from sqlalchemy.sql import func
from app.core.database import Base

class Claim(Base):
    __tablename__ = 'claims'

    id = Column(Integer,primary_key=True,index=True)
    article_id = Column(Integer,ForeignKey('articles.id',ondelete='CASCADE'))

    text = Column(Text,nullable=False)
    claim_type = Column(Text,nullable = True)
    event_date = Column(Date,nullable=True)
    normalized_text = Column(Text,index=True)
    is_verified = Column(Boolean,default=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())