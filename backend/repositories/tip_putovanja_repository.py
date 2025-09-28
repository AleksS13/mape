from sqlmodel import Session, select
from models.tip_putovanja import TipPutovanja
from schemas.tip_putovanja_schema import TipPutovanjaCreate
from fastapi import HTTPException

def get_all_tipovi(session: Session):
    return session.exec(select(TipPutovanja)).all()

def create_tip(session: Session, tip_data: TipPutovanjaCreate):
    tip = TipPutovanja(naziv=tip_data.naziv)
    session.add(tip)
    session.commit()
    session.refresh(tip)
    return tip

def delete_tip(session: Session, tip_id: int):
    tip = session.get(TipPutovanja, tip_id)
    if not tip:
        raise HTTPException(status_code=404, detail="Tip putovanja ne postoji")
    
    # Ovdje bi kasnije dodali provjeru FK ako se koristi u putovanju
    session.delete(tip)
    session.commit()
    return {"message": "Tip obrisan"}
