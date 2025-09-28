from sqlmodel import Session
from schemas.destinacija_schema import DestinacijaCreate
from repositories.destinacija_repository import (
    get_destinacije_for_putovanje,
    create_destinacija,
    delete_all_destinacije_for_putovanje
)
from models.putovanje import Putovanje
from fastapi import HTTPException

def get_destinacije_service(session: Session, putovanje_id: int):
    return get_destinacije_for_putovanje(session, putovanje_id)

def create_destinacija_service(session: Session, data: DestinacijaCreate):
    putovanje = session.get(Putovanje, data.putovanje_id)
    if not putovanje:
        raise HTTPException(status_code=404, detail="Putovanje ne postoji")

    if not (putovanje.datum_od <= data.datum_posjete <= putovanje.datum_do):
        raise HTTPException(status_code=400, detail="Datum posjete nije u rasponu datuma putovanja")
    
    return create_destinacija(session, data)

def delete_all_destinacije_service(session: Session, putovanje_id: int):
    return delete_all_destinacije_for_putovanje(session, putovanje_id)
