from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base


class TopicConfidence(Base):
    __tablename__ = "topic_confidence"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(
        Integer,
        ForeignKey("topics.id", ondelete="CASCADE"),
        unique=True,
    )

    score = Column(Integer)  # 0–100
    summary = Column(Text)

    last_calculated = Column(DateTime(timezone=True), server_default=func.now())
