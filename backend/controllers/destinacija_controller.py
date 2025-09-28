from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import engine
from services.destinacija_service import (
    get_destinacije_service,
    create_destinacija_service,
    delete_all_destinacije_service
)
from schemas.destinacija_schema import DestinacijaCreate, DestinacijaRead

router = APIRouter(prefix="/destinacije", tags=["Destinacije"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/{putovanje_id}", response_model=list[DestinacijaRead])
def get_destinacije(putovanje_id: int, session: Session = Depends(get_session)):
    return get_destinacije_service(session, putovanje_id)

@router.post("/", response_model=DestinacijaRead)
def create_destinacija(data: DestinacijaCreate, session: Session = Depends(get_session)):
    return create_destinacija_service(session, data)

@router.delete("/brisanje_svih/{putovanje_id}")
def delete_all_destinacije(putovanje_id: int, session: Session = Depends(get_session)):
    return delete_all_destinacije_service(session, putovanje_id)
