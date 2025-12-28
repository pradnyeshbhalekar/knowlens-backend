from fastapi import FastAPI
from app.api.v1.topics import router as topic_routers


from app.core.database import engine, Base


from app.models import (
    Topic,
    Article,
    Claim,
    ClaimComparison,
    TopicConfidence,
    Source,
)

Base.metadata.create_all(bind=engine)

# --- FastAPI app ---
app = FastAPI(title="Knowlens")
app.include_router(topic_routers,prefix='/api/v1')

@app.get("/")
def read_root():
    return {"message": "FastAPI is working"}
