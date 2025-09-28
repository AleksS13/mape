from sqlmodel import Session, select
from models.putovanje import Putovanje
from models.destinacija import Destinacija
from collections import Counter

def get_statistika(session: Session):
    # Ukupan broj putovanja
    ukupno_putovanja = session.exec(select(Putovanje)).all()
    broj_putovanja = len(ukupno_putovanja)
    
    # Ukupan broj destinacija
    ukupno_destinacija = session.exec(select(Destinacija)).all()
    broj_destinacija = len(ukupno_destinacija)
    
    # Broj destinacija po drzavi
    drzave = [d.drzava for d in ukupno_destinacija]
    broj_po_drzavi = dict(Counter(drzave))
    
    return {
        "broj_putovanja": broj_putovanja,
        "broj_destinacija": broj_destinacija,
        "destinacije_po_drzavi": broj_po_drzavi
    }
