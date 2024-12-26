from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from core.auth.deps import get_session, get_current_user

from schemas.participante_schema import ParticipanteBaseSchema, ParticipanteUpdateSchema, ParticipanteSchema, ParticipanteEventosSchema, ParticipanteCreateSchema
from schemas.inscricao_schema import InscricaoBaseSchema, InscricaoSchema
from services.participante_service import create_participante, get_participante, update_participante, delete_participante
from services.inscricao_service import create_inscricao, delete_inscricao
from models.participante_model import Participante

from utils.errors.exception_docs import post_inscricao_errors, delete_inscricao, participante_not_found, integrity_error

router = APIRouter()

@router.post("/", response_model=ParticipanteSchema, status_code=status.HTTP_201_CREATED, responses=integrity_error)
async def post(participante: ParticipanteCreateSchema, db: AsyncSession = Depends(get_session)):
    return await create_participante(participante, db)

@router.post("/inscricao", response_model=InscricaoSchema, status_code=status.HTTP_201_CREATED, responses=post_inscricao_errors)
async def post_inscricao(evento: InscricaoBaseSchema, db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await create_inscricao(evento=evento, participante_id=usuario_logado.id, db=db)

@router.get("/", response_model=ParticipanteEventosSchema, status_code=status.HTTP_200_OK, responses=participante_not_found)
async def get(db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await get_participante(participante_id=usuario_logado.id, db=db)

@router.put("/", response_model=ParticipanteSchema, status_code=status.HTTP_202_ACCEPTED, responses=participante_not_found)
async def put(participante: ParticipanteUpdateSchema, db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await update_participante(participante_id=usuario_logado.id, participante=participante, db=db)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, responses=participante_not_found)
async def delete(db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await delete_participante(participante_id=usuario_logado.id, db=db)

@router.delete("/inscricao/{evento_id}", status_code=status.HTTP_204_NO_CONTENT, responses=delete_inscricao)
async def del_inscricao(evento_id: int, db:AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await delete_inscricao(evento_id=evento_id, participante_id=usuario_logado.id, db=db)