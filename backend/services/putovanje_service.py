from sqlmodel import Session
from schemas.putovanje_schema import PutovanjeCreate
from repositories.putovanje_repository import (
    get_all_putovanja,
    create_putovanje,
    update_putovanje,
    delete_putovanje
)

def get_putovanja_service(session: Session):
    return get_all_putovanja(session)

def create_putovanje_service(session: Session, data: PutovanjeCreate):
    return create_putovanje(session, data)

def update_putovanje_service(session: Session, putovanje_id: int, data: PutovanjeCreate):
    return update_putovanje(session, putovanje_id, data)

def delete_putovanje_service(session: Session, putovanje_id: int):
    return delete_putovanje(session, putovanje_id)
