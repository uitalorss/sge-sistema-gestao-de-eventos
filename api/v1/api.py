from fastapi import APIRouter
from .endpoints import organizador, evento

api_router = APIRouter()

api_router.include_router(organizador.router, prefix="/organizadores", tags=["Organizadores"])
api_router.include_router(evento.router, prefix="/eventos", tags=["Eventos"])
