from fastapi import APIRouter
from .endpoints import organizador, evento, participante, auth, user

api_router = APIRouter()

api_router.include_router(organizador.router, prefix="/organizadores", tags=["Organizadores"])
api_router.include_router(evento.router, prefix="/eventos", tags=["Eventos"])
api_router.include_router(participante.router, prefix="/participantes", tags=["Participantes"])
api_router.include_router(auth.router, prefix="/login", tags=["Login"])
api_router.include_router(user.router, prefix="/users", tags=["Usuários"])