from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from core.auth.deps import get_session

from schemas.participante_schema import ParticipanteBaseSchema, ParticipanteUpdateSchema, ParticipanteSchema, ParticipanteEventosSchema, ParticipanteCreateSchema
from schemas.inscricao_schema import InscricaoBaseSchema, InscricaoSchema
from services.participante_service import create_participante, get_participante, update_participante, delete_participante
from services.inscricao_service import create_inscricao, delete_inscricao

router = APIRouter()

@router.post("/", response_model=ParticipanteSchema, status_code=status.HTTP_201_CREATED)
async def post(participante: ParticipanteCreateSchema, db: AsyncSession = Depends(get_session)):
    return await create_participante(participante, db)

@router.post("/{participante_id}/inscricao", response_model=InscricaoSchema, status_code=status.HTTP_201_CREATED)
async def post_inscricao(participante_id: str, evento: InscricaoBaseSchema, db: AsyncSession = Depends(get_session)):
    return await create_inscricao(evento, participante_id, db)

@router.get("/{participante_id}", response_model=ParticipanteEventosSchema, status_code=status.HTTP_200_OK)
async def get(participante_id: str, db: AsyncSession = Depends(get_session)):
    return await get_participante(participante_id, db)

@router.put("/{participante_id}", response_model=ParticipanteSchema, status_code=status.HTTP_202_ACCEPTED)
async def put(participante_id: str, participante: ParticipanteUpdateSchema, db: AsyncSession = Depends(get_session)):
    return await update_participante(participante_id, participante, db)

@router.delete("/{participante_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(participante_id: str, db: AsyncSession = Depends(get_session)):
    return await delete_participante(participante_id, db)

@router.delete("/{participante_id}/inscricao/{evento_id}", status_code=status.HTTP_204_NO_CONTENT)
async def del_inscricao(participante_id: str, evento_id: int, db:AsyncSession = Depends(get_session)):
    return await delete_inscricao(evento_id, participante_id, db)