from urllib.parse import urlparse
from sqlalchemy.orm import Session

from app.services.pipeline_service import search_and_extract
from app.models.source import Source
from app.models.topic import Topic
from app.models.article import Article

def slugify(text: str) -> str:
    return (
        text.lower()
        .strip()
        .replace(" ", "-")
    )

def get_base_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}".replace("www.", "")



def ingest_topic_if_new(db:Session,topic_title:str,limit:int = 5) -> dict:
    slug = slugify(topic_title)
    existing_topic = (db.query(Topic).filter(Topic.slug == slug).first())

    if existing_topic:
        return{
            "topic":topic_title,
            "slug":slug,
            "ingested":False,
            "reason":"Topic already existed"
        }
    
    topic = Topic(
        title = topic_title,
        slug = slug
    )
    db.add(topic)
    db.commit()
    db.refresh(topic)

    results = search_and_extract(topic_title,limit=limit)

    stored_articles = 0

    for item in results:
        url = item.get('url')
        title = item.get('title')
        content = item.get('text')

        if not url or not content:
            continue

        base_url = get_base_url(url)

        source = (
            db.query(Source)
            .filter(Source.base_url == base_url)
            .first()
        )

        if not source:
            source = Source(
                name = base_url.replace('https://',"").replace('http://',""),
                base_url = base_url,
                is_active = True
            )
            db.add(source)
            db.commit()
            db.refresh(source)

        existing_article = (
            db.query(Article)
            .filter(
                Article.source_id == source.id,
                Article.url == url
            )
            .first()
        )

        if existing_article:
            continue


        article = Article(
            topic_id = topic.id,
            source_id = source.id,
            title = title,
            url = url,
            content = content
        )
        db.add(article)
        db.commit()
        db.refresh(article)

        stored_articles+=1
        
    return {
            "topic":topic_title,
            "slug":slug,
            "ingested":True,
            "stored_articles":stored_articles,
            "total_found":len(results)
        }
