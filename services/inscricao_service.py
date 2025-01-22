from uuid import UUID

from fastapi import HTTPException, Response, status
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.inscricao_model import Inscricao
from schemas.inscricao_schema import InscricaoBaseSchema
from services.evento_service import get_evento


async def create_inscricao(
    evento: InscricaoBaseSchema, user_id: UUID, db: AsyncSession
):
    async with db as session:
        evento_exists = await get_evento(evento_id=evento.evento_id, db=db)

        if len(evento_exists.participantes) == evento_exists.capacidade:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Evento com capacidade esgotada.",
            )

        query = select(Inscricao).filter(
            and_(
                Inscricao.evento_id == evento.evento_id,
                Inscricao.user_id == user_id,
            )
        )
        result = await session.execute(query)
        is_available_inscricao = result.scalars().unique().one_or_none()

        if is_available_inscricao is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Usuário já cadastrado em evento.",
            )

        nova_inscricao: Inscricao = Inscricao(
            evento_id=evento.evento_id, user_id=user_id
        )
        session.add(nova_inscricao)
        await session.commit()

        return nova_inscricao


async def delete_inscricao(evento_id: int, user_id: UUID, db: AsyncSession):
    async with db as session:
        query = select(Inscricao).filter(
            and_(
                Inscricao.evento_id == evento_id, Inscricao.user_id == user_id
            )
        )
        result = await session.execute(query)
        inscricao = result.scalars().unique().one_or_none()

        if inscricao is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Inscrição de participante não encontrada.",
            )

        await session.delete(inscricao)
        await session.commit()
