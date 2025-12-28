from datetime import datetime

from app.core.database import SessionLocal
from app.models import Topic, Source, Article


def seed():
    db = SessionLocal()

    # ---- SOURCES ----
    react_blog = Source(
        name="React Official Blog",
        base_url="https://react.dev",
        reputation_score=9,
        is_primary=True,
        is_active=True,
    )

    techcrunch = Source(
        name="TechCrunch",
        base_url="https://techcrunch.com",
        reputation_score=7,
        is_primary=False,
        is_active=True,
    )

    db.add_all([react_blog, techcrunch])
    db.commit()

    # ---- TOPIC ----
    topic = Topic(
        title="React got hacked",
        description="Investigation into alleged React security breach",
        slug="react-got-hacked",
    )

    db.add(topic)
    db.commit()
    db.refresh(topic)

    # ---- ARTICLES ----
    article_1 = Article(
        topic_id=topic.id,
        source_id=react_blog.id,
        title="Security update from React team",
        url="https://react.dev/blog/security-update",
        published_at=datetime.utcnow(),
        content="The React team confirmed there was no breach affecting user data.",
    )

    article_2 = Article(
        topic_id=topic.id,
        source_id=techcrunch.id,
        title="Reports claim possible React infrastructure breach",
        url="https://techcrunch.com/react-security-incident",
        published_at=datetime.utcnow(),
        content="Some reports suggest a possible breach, though details remain unclear.",
    )

    db.add_all([article_1, article_2])
    db.commit()

    db.close()
    print("✅ Dummy data inserted successfully")


if __name__ == "__main__":
    seed()
