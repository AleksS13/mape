from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import engine
from services.tip_putovanja_service import (
    get_tipovi_service,
    create_tip_service,
    delete_tip_service
)
from schemas.tip_putovanja_schema import TipPutovanjaCreate, TipPutovanjaRead

router = APIRouter(prefix="/tipovi", tags=["Tipovi putovanja"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/", response_model=list[TipPutovanjaRead])
def get_tipovi(session: Session = Depends(get_session)):
    return get_tipovi_service(session)

@router.post("/", response_model=TipPutovanjaRead)
def create_tip(tip_data: TipPutovanjaCreate, session: Session = Depends(get_session)):
    return create_tip_service(session, tip_data)

@router.delete("/{tip_id}")
def delete_tip(tip_id: int, session: Session = Depends(get_session)):
    return delete_tip_service(session, tip_id)
