from app.core.database import SessionLocal
from app.models import Claim
from app.services.claims_ingestion import ingest_claims_for_article


def main():
    db = SessionLocal()

    # IMPORTANT: known-good article with real content
    ARTICLE_ID = 3  # change only if needed

    inserted_first = ingest_claims_for_article(db, ARTICLE_ID)
    print("Inserted claims (first run):", inserted_first)
    assert inserted_first > 0, "No claims inserted on first run"

    inserted_second = ingest_claims_for_article(db, ARTICLE_ID)
    print("Inserted claims (second run):", inserted_second)
    assert inserted_second == 0, "Idempotency broken"

    claims = (
        db.query(Claim)
        .filter(Claim.article_id == ARTICLE_ID)
        .all()
    )

    print("\nClaims stored in DB:")
    for c in claims:
        print("-", c.text)

    print("\n✅ Claim ingestion pipeline is working correctly.")


if __name__ == "__main__":
    main()
