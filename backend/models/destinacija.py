from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Destinacija(SQLModel, table=True):
    __tablename__ = "destinacije"

    id: Optional[int] = Field(default=None, primary_key=True)
    grad: str
    drzava: str
    datum_posjete: date
    lat: float
    lon: float
    putovanje_id: int = Field(foreign_key="putovanja.id")
