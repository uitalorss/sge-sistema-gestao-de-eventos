from fastapi import HTTPException, status, Response

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from datetime import datetime

from uuid import UUID

from schemas.evento_schema import EventoBaseSchema, EventoUpdateSchema, EventoResponseSchema

from models.eventos_model import Evento

async def create_evento(evento: EventoBaseSchema, db: AsyncSession, organizador_id: UUID):
    data_inicio = datetime.strptime(evento.data_inicio, "%d/%m/%Y")
    novo_evento: Evento = Evento(nome=evento.nome, descricao=evento.descricao, data_inicio=data_inicio, capacidade=evento.capacidade, organizador_id=organizador_id)
    async with db as session:
        try:
            session.add(novo_evento)
            await session.commit()

            return novo_evento
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Favor verificar dados.")

async def get_todos_eventos(db: AsyncSession):
    async with db as session:
        result = await session.execute(select(Evento))
        eventos = result.unique().scalars().all()
        return [EventoResponseSchema.model_validate(evento) for evento in eventos]

async def get_evento(evento_id: int, db: AsyncSession):
    async with db as session:
        query = select(Evento).filter(Evento.id == evento_id)
        result = await session.execute(query)
        evento = result.scalars().unique().one_or_none()

        if evento is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado.")
        
        return evento
    
async def update_evento(evento_id: int, evento: EventoUpdateSchema, organizador_id: UUID, db: AsyncSession):
    async with db as session:
        query = select(Evento).filter(and_(Evento.id == evento_id, Evento.organizador_id == organizador_id))
        result = await session.execute(query)
        update_evento = result.scalars().unique().one_or_none()

        if update_evento is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado.")
        
        if evento.nome:
            update_evento.nome = evento.nome

        if evento.descricao:
            update_evento.descricao = evento.descricao
        
        if evento.data_inicio:
            update_evento.data_inicio = evento.data_inicio

        if evento.capacidade:
            update_evento.capacidade = evento.capacidade

        update_evento.atualizado_em = datetime.now()

        await session.commit()

        return update_evento
    
async def delete_evento(evento_id: int, db: AsyncSession, organizador_id: UUID):
    async with db as session:
        query = select(Evento).filter(and_(Evento.id == evento_id, Evento.organizador_id == organizador_id))
        result = await session.execute(query)
        delete_evento = result.scalars().unique().one_or_none()

        if delete_evento is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado.")
        
        await session.delete(delete_evento)
        await session.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)