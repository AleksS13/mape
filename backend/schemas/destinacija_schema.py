from pydantic import BaseModel
from datetime import date

class DestinacijaCreate(BaseModel):
    grad: str
    drzava: str
    datum_posjete: date
    lat: float
    lon: float
    putovanje_id: int

class DestinacijaRead(BaseModel):
    id: int
    grad: str
    drzava: str
    datum_posjete: date
    lat: float
    lon: float
    putovanje_id: int

    class Config:
        orm_mode = True
