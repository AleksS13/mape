from sqlmodel import Session, select
from database import engine
from models.destinacija import Destinacija

def get_sve_destinacije():
    with Session(engine) as session:
        statement = select(Destinacija)
        results = session.exec(statement).all()
        return results
