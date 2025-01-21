from fastapi import APIRouter, Depends, status, Security
from fastapi.responses import JSONResponse

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from core.auth.deps import get_session, get_current_user

from schemas.evento_schema import EventoBaseSchema, EventoUpdateSchema, EventoResponseSchema, EventoResponseSchemaCompleto
from services.evento_service import create_evento, get_evento, update_evento, delete_evento, get_todos_eventos

from models.organizador_model import Organizador
from models.profile_model import PerfilEnum

from utils.errors.error_responses import common_response_evento, generate_not_found_response, auth_responses

router = APIRouter()

@router.post("/", response_model=EventoResponseSchema, status_code=status.HTTP_201_CREATED, responses={**auth_responses, **common_response_evento})
async def post(
    evento: EventoBaseSchema,
    db: AsyncSession = Depends(get_session),
    user = Security(
        get_current_user,
        scopes=[PerfilEnum.ORGANIZADOR.value]
    )
):
    return await create_evento(evento=evento, db=db, usuario_id=user.id)

@router.get("/", response_model=List[EventoResponseSchema], status_code=status.HTTP_200_OK)
async def get_eventos(db: AsyncSession = Depends(get_session)):
    return await get_todos_eventos(db)

@router.get("/{evento_id}", response_model=EventoResponseSchemaCompleto, status_code=status.HTTP_200_OK, responses={**generate_not_found_response("Evento")})
async def get(evento_id: int, db: AsyncSession = Depends(get_session)):
    return await get_evento(evento_id, db)

@router.patch("/{evento_id}", response_model=EventoResponseSchema, status_code=status.HTTP_202_ACCEPTED, responses={**auth_responses, **generate_not_found_response("Evento")})
async def put(
    evento_id: int,
    evento: EventoUpdateSchema,
    db: AsyncSession = Depends(get_session),
    user = Security(
        get_current_user,
        scopes=[PerfilEnum.ORGANIZADOR.value]
    ),
):
    return await update_evento(evento_id=evento_id, evento=evento, db=db, user_id=user.id)

@router.delete("/{evento_id}", status_code=status.HTTP_204_NO_CONTENT, responses={**auth_responses, **generate_not_found_response("Evento")})
async def delete(
    evento_id: int,
    db: AsyncSession = Depends(get_session),
    user = Security(
        get_current_user,
        scopes=[PerfilEnum.ORGANIZADOR.value]
    ),
):
    return await delete_evento(evento_id=evento_id, db=db, user_id=user.id)