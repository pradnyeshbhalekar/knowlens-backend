from sqlalchemy.orm import Session
from app.models.topic import Topic
from app.models.article import Article

def slugify(text: str) -> str:
    return text.lower().strip().replace(' ',"-")

def get_articles_by_topic(db:Session,topic_input:str)-> dict:
    slug = slugify(topic_input)
    
    topic = (
        db.query(Topic).filter(Topic.slug == slug).first()
    )


    if not topic:
        return {
            "topic": topic_input,
            "slug": slug,
            "found": False,
            "articles":[]        
            }
    
    articles = (
        db.query(Article)
        .filter(Article.topic_id == topic.id).order_by(Article.created_at.desc())
        .all()
    )

    results = []
    for article in articles:
        results.append({
            "id":article.id,
            "title":article.title,
            "url":article.url,
            "content":article.content,
            "created_at":article.created_at
        })
    return({
        "topic":topic.title,
        "slug":topic.slug,
        "found":True,
        "count":len(results),
        "articles":results
    })