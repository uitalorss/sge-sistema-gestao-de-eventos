from fastapi import APIRouter
from .endpoints import organizador

api_router = APIRouter()

api_router.include_router(organizador.router, prefix="/organizadores", tags=["Organizadores"])
