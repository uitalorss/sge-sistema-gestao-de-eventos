from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession
from core.auth.deps import get_session
from schemas.organizador_schema import OrganizadorBaseSchema, OrganizadorSchema, OrganizadorUpdateSchema, OrganizadorEventoSchema, OrganizadorCreateSchema
from services.organizador_service import create_organizador, get_organizador, update_organizador, delete_organizador
from models.organizador_model import Organizador

router = APIRouter()

@router.post("/", response_model=OrganizadorSchema, status_code=status.HTTP_201_CREATED)
async def post(organizador: OrganizadorCreateSchema, db: AsyncSession = Depends(get_session)):
    return await create_organizador(organizador, db)

@router.get("/{organizador_id}", response_model=OrganizadorEventoSchema, status_code=status.HTTP_200_OK)
async def get(organizador_id: str, db: AsyncSession = Depends(get_session)):
    return await get_organizador(organizador_id, db)

@router.put("/{organizador_id}", response_model=OrganizadorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put(organizador_id: str, organizador: OrganizadorUpdateSchema, db: AsyncSession = Depends(get_session)):
    return await update_organizador(organizador_id, organizador, db)

@router.delete("/{organizador_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(organizador_id: str, db: AsyncSession = Depends(get_session)):
    return await delete_organizador(organizador_id, db)