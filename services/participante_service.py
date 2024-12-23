from fastapi import HTTPException, status, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from uuid import UUID
from core.auth.auth import create_access_token
from core.auth.security import generate_hashed_password, verify_password
from schemas.participante_schema import ParticipanteBaseSchema, ParticipanteUpdateSchema, ParticipanteSchema, ParticipanteCreateSchema
from schemas.auth_schema import LoginSchema
from models.participante_model import Participante

async def create_participante(participante: ParticipanteCreateSchema, db: AsyncSession):
    novo_participante: Participante = Participante(nome=participante.nome, email=participante.email, telefone=participante.telefone, senha=generate_hashed_password(participante.senha))
    async with db as session:
        try:
            session.add(novo_participante)
            await session.commit()

            return novo_participante
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email informado já cadastrado.")
        
async def get_participante(participante_id: str, db: AsyncSession):
    async with db as session:
        query = select(Participante).filter(Participante.id == UUID(participante_id))
        result = await session.execute(query)
        participante = result.scalars().unique().one_or_none()

        if participante is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participante não encontrado.")
        
        return participante
    
async def update_participante(participante_id: str, participante: ParticipanteUpdateSchema, db: AsyncSession):
    async with db as session:
        query = select(Participante).filter(Participante.id == UUID(participante_id))
        result = await session.execute(query)
        update_participante = result.scalars().unique().one_or_none()

        if update_participante is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participante não encontrado.")
        
        if participante.nome:
            update_participante.nome = participante.nome

        if participante.email:
            update_participante.email = participante.email

        if participante.telefone:
            update_participante.telefone = participante.telefone

        await session.commit()

        return update_participante
    
async def delete_participante(participante_id: str, db: AsyncSession):
    async with db as session:
        query = select(Participante).filter(Participante.id == UUID(participante_id))
        result = await session.execute(query)
        delete_participante = result.scalars().unique().one_or_none()

        if delete_participante is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participante não encontrado.")

        await session.delete(delete_participante)
        await session.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
async def login_participante(login_data: LoginSchema, db: AsyncSession):
    async with db as session:
        query = select(Participante).filter(Participante.email == login_data.email)
        result = await session.execute(query)
        organizador = result.scalars().unique().one_or_none()

        if organizador is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário e/ou senha incorretos.")
        
        if not verify_password(login_data.senha, organizador.senha):
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário e/ou senha incorretos.")
        
        organizador_id = str(organizador.id)

        return create_access_token(organizador_id)