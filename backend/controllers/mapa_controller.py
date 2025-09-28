from fastapi import APIRouter
from typing import List
from models.destinacija import Destinacija
from services.mapa_service import get_sve_destinacije

router = APIRouter(prefix="/mape", tags=["mape"])

@router.get("/", response_model=List[Destinacija])
def lista_destinacija():
    return get_sve_destinacije()
