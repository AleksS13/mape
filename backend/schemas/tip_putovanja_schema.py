from pydantic import BaseModel

class TipPutovanjaCreate(BaseModel):
    naziv: str

class TipPutovanjaRead(BaseModel):
    id: int
    naziv: str

    class Config:
        orm_mode = True
