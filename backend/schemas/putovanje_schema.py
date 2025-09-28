from pydantic import BaseModel
from datetime import date

class PutovanjeCreate(BaseModel):
    naziv: str
    datum_od: date
    datum_do: date
    tip_id: int

class PutovanjeRead(BaseModel):
    id: int
    naziv: str
    datum_od: date
    datum_do: date
    tip_id: int

    class Config:
        orm_mode = True
