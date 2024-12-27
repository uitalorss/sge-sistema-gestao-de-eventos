from fastapi import HTTPException, status, Response

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from uuid import UUID

from schemas.inscricao_schema import InscricaoBaseSchema
from models.participante_evento_model import ParticipanteEvento
from services.evento_service import get_evento


async def create_inscricao(evento: InscricaoBaseSchema, participante_id: UUID, db: AsyncSession):
    async with db as session:
        evento_exists = await get_evento(evento_id=evento.evento_id, db=db)
        
        if len(evento_exists.participantes) == evento_exists.capacidade:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Evento com capacidade esgotada.") 

        query = select(ParticipanteEvento).filter(and_(ParticipanteEvento.evento_id == evento.evento_id, ParticipanteEvento.participante_id == participante_id))
        result = await session.execute(query)
        is_available_inscricao = result.scalars().unique().one_or_none()

        if is_available_inscricao is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário já cadastrado em evento.")

        nova_inscricao: ParticipanteEvento = ParticipanteEvento(evento_id=evento.evento_id, participante_id=participante_id)
        session.add(nova_inscricao)
        await session.commit()

        return nova_inscricao

async def delete_inscricao(evento_id: int, participante_id: UUID, db: AsyncSession):
    async with db as session:
        query = select(ParticipanteEvento).filter(and_(ParticipanteEvento.evento_id == evento_id, ParticipanteEvento.participante_id == participante_id))
        result = await session.execute(query)
        inscricao = result.scalars().unique().one_or_none()

        if inscricao is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inscrição de participante não encontrada.")

        await session.delete(inscricao)
        await session.commit()