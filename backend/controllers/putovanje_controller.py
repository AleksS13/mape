from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import engine
from services.putovanje_service import (
    get_putovanja_service,
    create_putovanje_service,
    update_putovanje_service,
    delete_putovanje_service
)
from schemas.putovanje_schema import PutovanjeCreate, PutovanjeRead

router = APIRouter(prefix="/putovanja", tags=["Putovanja"])

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/", response_model=list[PutovanjeRead])
def get_putovanja(session: Session = Depends(get_session)):
    return get_putovanja_service(session)

@router.post("/", response_model=PutovanjeRead)
def create_putovanje(data: PutovanjeCreate, session: Session = Depends(get_session)):
    return create_putovanje_service(session, data)

@router.put("/{putovanje_id}", response_model=PutovanjeRead)
def update_putovanje(putovanje_id: int, data: PutovanjeCreate, session: Session = Depends(get_session)):
    return update_putovanje_service(session, putovanje_id, data)

@router.delete("/{putovanje_id}")
def delete_putovanje(putovanje_id: int, session: Session = Depends(get_session)):
    return delete_putovanje_service(session, putovanje_id)
