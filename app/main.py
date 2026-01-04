from fastapi import FastAPI
from app.api.v1.topics import router as topic_routers
from app.api.v1.search import router as search_routers 
# article endpoint //here//
from app.api.v1.claims import router as claim_routers


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


app = FastAPI(title="Knowlens")

# v1
app.include_router(topic_routers,prefix='/api/v1')
app.include_router(search_routers,prefix='/api/v1')
# article //here//
app.include_router(claim_routers,prefix='/api/v1')
@app.get("/")
def read_root():
    return {"message": "FastAPI is working"}
