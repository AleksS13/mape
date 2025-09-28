from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Putovanje(SQLModel, table=True):
    __tablename__ = "putovanja"

    id: Optional[int] = Field(default=None, primary_key=True)
    naziv: str
    datum_od: date
    datum_do: date
    tip_id: int = Field(foreign_key="tipovi_putovanja.id")

   
