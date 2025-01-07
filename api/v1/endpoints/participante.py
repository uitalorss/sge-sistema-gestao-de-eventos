from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession
from core.auth.deps import get_session, get_current_user

from schemas.participante_schema import ParticipanteUpdateSchema, ParticipanteSchema, ParticipanteEventosSchema, ParticipanteCreateSchema
from schemas.inscricao_schema import InscricaoBaseSchema, InscricaoSchema
from services.participante_service import create_participante, get_participante, update_participante, delete_participante
from services.inscricao_service import create_inscricao, delete_inscricao
from models.participante_model import Participante

from utils.errors.error_responses import auth_responses, generate_not_found_response, common_response, inscricao_responses, not_found_inscricao_response

router = APIRouter()

@router.post("/", response_model=ParticipanteSchema, status_code=status.HTTP_201_CREATED, responses={**common_response})
async def post(participante: ParticipanteCreateSchema, db: AsyncSession = Depends(get_session)):
    return await create_participante(participante, db)

@router.post("/inscricao", response_model=InscricaoSchema, status_code=status.HTTP_201_CREATED, responses={**auth_responses, **inscricao_responses})
async def post_inscricao(evento: InscricaoBaseSchema, db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await create_inscricao(evento=evento, participante_id=usuario_logado.id, db=db)

@router.get("/", response_model=ParticipanteEventosSchema, status_code=status.HTTP_200_OK, responses={**auth_responses, **generate_not_found_response("Participante")})
async def get(db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await get_participante(participante_id=usuario_logado.id, db=db)

@router.patch("/", response_model=ParticipanteSchema, status_code=status.HTTP_202_ACCEPTED, responses={**auth_responses, **generate_not_found_response("Participante")})
async def patch(participante: ParticipanteUpdateSchema, db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await update_participante(participante_id=usuario_logado.id, participante=participante, db=db)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, responses={**auth_responses, **generate_not_found_response("Participante")})
async def delete(db: AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await delete_participante(participante_id=usuario_logado.id, db=db)

@router.delete("/inscricao/{evento_id}", status_code=status.HTTP_204_NO_CONTENT, responses={**auth_responses, **not_found_inscricao_response})
async def del_inscricao(evento_id: int, db:AsyncSession = Depends(get_session), usuario_logado: Participante = Depends(get_current_user)):
    return await delete_inscricao(evento_id=evento_id, participante_id=usuario_logado.id, db=db)