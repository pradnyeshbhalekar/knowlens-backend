from sqlalchemy.orm import Session
from app.extractors.claim_normalizer import normalize_claim
from app.models import Article,Claim
from app.services.claims_extractor_llm import extract_claims_from_text


def ingest_claims_for_article(db:Session,article_id:int) -> int:
    article = db.query(Article).filter(Article.id == article_id).first()
    
    if not article or not article.content:
        return 0
    
    existing_count = (
        db.query(Claim)
        .filter(Claim.article_id == article_id).count()
    )

    if existing_count > 0:
        return 0
    
    extracted_claims = extract_claims_from_text(article.content)

    inserted = 0

    for claim_text in extracted_claims:
        normalized = normalize_claim(claim_text)

        exists = (
            db.query(Claim).filter(Claim.article_id == article_id,Claim.normalized_text == normalized).first()
        )

        if exists:
            continue

        claim = Claim(
            article_id = article_id,
            text = claim_text,
            normalized_text = normalized,
            is_verified = None
        )

        db.add(claim)
        inserted += 1

    if inserted > 0:
        db.commit()
    return inserted