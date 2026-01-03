from fastapi import APIRouter,Query,Depends
# from app.services.pipeline_service import search_and_extract
from app.services.unified_search_service import unified_search
from app.core.db_dependency import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.get('/search',tags=['Search'])
def search(q:str = Query(...,min_length=5),limit: int = Query(5,ge=1,le=20),db:Session = Depends(get_db)):
    results = unified_search(db=db,topic_input=q,limit=limit)
    return {
        "results":results
    }