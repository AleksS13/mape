from sqlmodel import Session
from repositories.tip_putovanja_repository import (
    get_all_tipovi,
    create_tip,
    delete_tip
)
from schemas.tip_putovanja_schema import TipPutovanjaCreate

def get_tipovi_service(session: Session):
    return get_all_tipovi(session)

def create_tip_service(session: Session, tip_data: TipPutovanjaCreate):
    return create_tip(session, tip_data)

def delete_tip_service(session: Session, tip_id: int):
    return delete_tip(session, tip_id)
