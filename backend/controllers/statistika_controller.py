from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import engine
from services.statistika_service import get_statistika

router = APIRouter(prefix="/statistika", tags=["Statistika"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/")
def statistika(session: Session = Depends(get_session)):
    return get_statistika(session)
