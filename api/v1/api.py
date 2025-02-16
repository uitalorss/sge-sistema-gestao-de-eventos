from fastapi import APIRouter

from .endpoints import evento, inscricao, user

api_router = APIRouter()

api_router.include_router(evento.router, prefix="/eventos", tags=["Eventos"])
api_router.include_router(
    inscricao.router, prefix="/inscricao", tags=["Inscrições"]
)
api_router.include_router(user.router, prefix="/users", tags=["Usuários"])
