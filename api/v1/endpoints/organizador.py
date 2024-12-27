from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession
from core.auth.deps import get_session, get_current_user
from schemas.organizador_schema import OrganizadorBaseSchema, OrganizadorSchema, OrganizadorUpdateSchema, OrganizadorEventoSchema, OrganizadorCreateSchema
from services.organizador_service import create_organizador, get_organizador, update_organizador, delete_organizador
from models.organizador_model import Organizador
from utils.errors.error_responses import common_response, auth_responses, generate_not_found_response

router = APIRouter()

@router.post("/", response_model=OrganizadorSchema, status_code=status.HTTP_201_CREATED, responses={**auth_responses, **common_response})
async def post(organizador: OrganizadorCreateSchema, db: AsyncSession = Depends(get_session)):
    return await create_organizador(organizador, db)

@router.get("/", response_model=OrganizadorEventoSchema, status_code=status.HTTP_200_OK, responses={**auth_responses, **generate_not_found_response("Organizador")})
async def get(db: AsyncSession = Depends(get_session), usuario_logado: Organizador = Depends(get_current_user)):
    return await get_organizador(organizador_id=usuario_logado.id, db=db)

@router.put("/", response_model=OrganizadorSchema, status_code=status.HTTP_202_ACCEPTED, responses={**auth_responses, **generate_not_found_response("Organizador")})
async def put(organizador: OrganizadorUpdateSchema, db: AsyncSession = Depends(get_session), usuario_logado: Organizador = Depends(get_current_user)):
    return await update_organizador(organizador_id=usuario_logado.id, organizador=organizador, db=db)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, responses={**auth_responses, **generate_not_found_response("Organizador")})
async def delete(db: AsyncSession = Depends(get_session), usuario_logado: Organizador = Depends(get_current_user)):
    return await delete_organizador(organizador_id=usuario_logado.id, db=db)