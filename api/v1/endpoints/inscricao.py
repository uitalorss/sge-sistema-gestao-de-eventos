from fastapi import APIRouter, Depends, Security, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.auth.deps import get_current_user, get_session
from models.profile_model import PerfilEnum
from models.user_model import User
from schemas.inscricao_schema import InscricaoBaseSchema, InscricaoSchema
from services.inscricao_service import create_inscricao, delete_inscricao
from utils.errors.error_responses import (
    auth_responses,
    inscricao_responses,
    not_found_inscricao_response,
)

router = APIRouter()


@router.post(
    "/",
    response_model=InscricaoSchema,
    status_code=status.HTTP_201_CREATED,
    responses={**auth_responses, **inscricao_responses},
)
async def post_inscricao(
    evento: InscricaoBaseSchema,
    db: AsyncSession = Depends(get_session),
    user: User = Security(
        get_current_user, scopes=[PerfilEnum.PARTICIPANTE.value]
    ),
):
    return await create_inscricao(evento=evento, user_id=user.id, db=db)


@router.delete(
    "/{evento_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={**auth_responses, **not_found_inscricao_response},
)
async def del_inscricao(
    evento_id: int,
    db: AsyncSession = Depends(get_session),
    user: User = Security(
        get_current_user, scopes=[PerfilEnum.PARTICIPANTE.value]
    ),
):
    return await delete_inscricao(evento_id=evento_id, user_id=user.id, db=db)
