from sqlmodel import Session, select
from models.putovanje import Putovanje
from schemas.putovanje_schema import PutovanjeCreate
from fastapi import HTTPException

def get_all_putovanja(session: Session):
    return session.exec(select(Putovanje)).all()

def create_putovanje(session: Session, data: PutovanjeCreate):
    if data.datum_od > data.datum_do:
        raise HTTPException(status_code=400, detail="Datum početka ne može biti nakon datuma završetka.")

    putovanje = Putovanje(
        naziv=data.naziv,
        datum_od=data.datum_od,
        datum_do=data.datum_do,
        tip_id=data.tip_id
    )
    session.add(putovanje)
    session.commit()
    session.refresh(putovanje)
    return putovanje

def update_putovanje(session: Session, putovanje_id: int, data: PutovanjeCreate):
    putovanje = session.get(Putovanje, putovanje_id)
    if not putovanje:
        raise HTTPException(status_code=404, detail="Putovanje ne postoji")
    
    putovanje.naziv = data.naziv
    putovanje.datum_od = data.datum_od
    putovanje.datum_do = data.datum_do
    putovanje.tip_id = data.tip_id

    session.commit()
    session.refresh(putovanje)
    return putovanje

def delete_putovanje(session: Session, putovanje_id: int):
    putovanje = session.get(Putovanje, putovanje_id)
    if not putovanje:
        raise HTTPException(status_code=404, detail="Putovanje ne postoji")
    
    session.delete(putovanje)
    session.commit()
    return {"message": "Putovanje obrisano"}
