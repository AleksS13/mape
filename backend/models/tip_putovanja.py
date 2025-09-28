from sqlmodel import SQLModel, Field
from typing import Optional

class TipPutovanja(SQLModel, table=True):
    __tablename__ = "tipovi_putovanja"

    id: Optional[int] = Field(default=None, primary_key=True)
    naziv: str