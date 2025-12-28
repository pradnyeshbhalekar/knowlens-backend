from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class ClaimComparison(Base):
    __tablename__ = 'claim_comparsion'
    id = Column(Integer,primary_key=True,index=True)

    claim_a_id = Column(Integer,ForeignKey('claims.id',ondelete='CASCADE'))
    claim_b_id = Column(Integer,ForeignKey('claims.id',ondelete='CASCADE'))

    relation = Column(String(20))
    confidence = Column(Float)
    created_at = Column(DateTime(timezone=True),server_default=func.now())