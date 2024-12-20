from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from core.auth.deps import get_session

from schemas.participante_schema import ParticipanteBaseSchema, ParticipanteUpdateSchema, ParticipanteSchema, ParticipanteEventosSchema
from services.participante_service import create_participante, get_participante, update_participante, delete_participante

router = APIRouter()

@router.post("/", response_model=ParticipanteSchema, status_code=status.HTTP_201_CREATED)
async def post(organizador: ParticipanteBaseSchema, db: AsyncSession = Depends(get_session)):
    return await create_participante(organizador, db)

@router.get("/{organizador_id}", response_model=ParticipanteEventosSchema, status_code=status.HTTP_200_OK)
async def get(organizador_id: str, db: AsyncSession = Depends(get_session)):
    return await get_participante(organizador_id, db)

@router.put("/{organizador_id}", response_model=ParticipanteSchema, status_code=status.HTTP_202_ACCEPTED)
async def put(organizador_id: str, organizador: ParticipanteUpdateSchema, db: AsyncSession = Depends(get_session)):
    return await update_participante(organizador_id, organizador, db)

@router.delete("/{organizador_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(organizador_id: str, db: AsyncSession = Depends(get_session)):
    return await delete_participante(organizador_id, db)