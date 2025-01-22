from fastapi import APIRouter
from .endpoints import inscricao, organizador, evento, user

api_router = APIRouter()

api_router.include_router(organizador.router, prefix="/organizadores", tags=["Organizadores"])
api_router.include_router(evento.router, prefix="/eventos", tags=["Eventos"])
api_router.include_router(inscricao.router, prefix="/inscricao", tags=["Inscrições"])
api_router.include_router(user.router, prefix="/users", tags=["Usuários"])