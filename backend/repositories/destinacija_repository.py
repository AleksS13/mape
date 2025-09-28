from sqlmodel import Session, select
from models.destinacija import Destinacija
from schemas.destinacija_schema import DestinacijaCreate
from fastapi import HTTPException

def get_destinacije_for_putovanje(session: Session, putovanje_id: int):
    return session.exec(
        select(Destinacija).where(Destinacija.putovanje_id == putovanje_id)
    ).all()

def create_destinacija(session: Session, data: DestinacijaCreate):
    # Validacija datuma se radi u servisu
    destinacija = Destinacija(
        grad=data.grad,
        drzava=data.drzava,
        datum_posjete=data.datum_posjete,
        lat=data.lat,
        lon=data.lon,
        putovanje_id=data.putovanje_id
    )
    session.add(destinacija)
    session.commit()
    session.refresh(destinacija)
    return destinacija

def delete_all_destinacije_for_putovanje(session: Session, putovanje_id: int):
    destinacije = session.exec(
        select(Destinacija).where(Destinacija.putovanje_id == putovanje_id)
    ).all()

    for d in destinacije:
        session.delete(d)
    session.commit()
    return {"message": f"Obrisano {len(destinacije)} destinacija"}
