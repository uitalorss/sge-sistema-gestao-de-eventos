from fastapi import HTTPException, status, Response
import redis
import json
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from datetime import datetime

from uuid import UUID

from schemas.evento_schema import EventoBaseSchema, EventoUpdateSchema, EventoResponseSchema

from models.eventos_model import Evento

redis_db = redis.Redis(host='localhost', port=6379, db=0)

async def create_evento(evento: EventoBaseSchema, db: AsyncSession, usuario_id: UUID):
    data_inicio = datetime.strptime(evento.data_inicio, "%d/%m/%Y")
    novo_evento: Evento = Evento(nome=evento.nome, descricao=evento.descricao, data_inicio=data_inicio, capacidade=evento.capacidade, user_id=usuario_id)
    async with db as session:
        try:
            session.add(novo_evento)
            await session.commit()

            if redis_db.exists("eventos"):
                redis_db.delete("eventos")

            return novo_evento
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Favor verificar dados.")

async def get_todos_eventos(db: AsyncSession):
    if redis_db.get("eventos"):
        eventos_data = redis_db.get("eventos")
        eventos = json.loads(eventos_data)
        return eventos

    else:
        async with db as session:
            result = await session.execute(select(Evento))
            eventos_db = result.unique().scalars().all()
            eventos = [EventoResponseSchema.model_validate(evento).model_dump() for evento in eventos_db]
            for evento in eventos:
                evento["user_id"] = str(evento["user_id"]) 
                evento["data_inicio"] = str(evento["data_inicio"])
            
            redis_db.set("eventos", json.dumps(eventos))

            return eventos

async def get_evento(evento_id: int, db: AsyncSession):
    async with db as session:
        evento = await pegar_evento(evento_id, db)
        if evento is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado.")
        
        return evento
    
async def update_evento(evento_id: int, evento: EventoUpdateSchema, user_id: UUID, db: AsyncSession):
    async with db as session:
        update_evento = await pegar_evento(evento_id, db)
        if update_evento is None or update_evento.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado.")
        
        for field, value in evento.model_dump(exclude_unset=True).items():
            if field == "data_inicio":
                value = datetime.strptime(value, "%d/%m/%Y")
            setattr(update_evento, field, value)

        update_evento.atualizado_em = datetime.now()

        await session.commit()
        if redis_db.exists("eventos"):
            redis_db.delete("eventos")

        return update_evento
    
async def delete_evento(evento_id: int, db: AsyncSession, user_id: UUID):
    async with db as session:
        delete_evento = await pegar_evento(evento_id, db)
        if delete_evento is None or delete_evento.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado.")
        
        await session.delete(delete_evento)
        await session.commit()
        if redis_db.exists("eventos"):
            redis_db.delete("eventos")

        return Response(status_code=status.HTTP_204_NO_CONTENT)

async def pegar_evento(evento_id: int, db: AsyncSession):
    query = select(Evento).filter(Evento.id == evento_id)
    result = await db.execute(query)
    evento = result.scalars().unique().one_or_none()

    return evento
        