from fastapi import HTTPException, status, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from uuid import UUID

from schemas.organizador_schema import OrganizadorBaseSchema, OrganizadorSchema, OrganizadorUpdateSchema
from models.organizador_model import Organizador

async def create_organizador(organizador: OrganizadorBaseSchema, db: AsyncSession):
    novo_organizador: Organizador = Organizador(nome=organizador.nome, email=organizador.email, telefone=organizador.telefone)
    print(novo_organizador)
    async with db as session:
        try:
            session.add(novo_organizador)
            await session.commit()

            return novo_organizador
        except IntegrityError:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Dados informados são inválidos")
        
async def get_organizador(organizador_id: str, db: AsyncSession):
    async with db as session:
        query = select(Organizador).filter(Organizador.id == UUID(organizador_id))
        result = await session.execute(query)
        organizador = result.scalars().unique().one_or_none()

        if organizador is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Organizador não encontrado")
        
        return organizador
    
async def update_organizador(organizador_id: str, organizador: OrganizadorUpdateSchema, db: AsyncSession):
    async with db as session:
        query = select(Organizador).filter(Organizador.id == UUID(organizador_id))
        result = await session.execute(query)
        update_organizador = result.scalars().unique().one_or_none()

        if update_organizador is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Organizador não encontrado")
        
        if organizador.nome:
            update_organizador.nome = organizador.nome

        if organizador.email:
            update_organizador.email = organizador.email

        if organizador.telefone:
            update_organizador.telefone = organizador.telefone
    
        await session.commit()

        return update_organizador
    
async def delete_organizador(organizador_id: str, db: AsyncSession):
    async with db as session:
        query = select(Organizador).filter(Organizador.id == UUID(organizador_id))
        result = await session.execute(query)
        delete_organizador = result.scalars().unique().one_or_none()

        if delete_organizador is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organizador não encontrado")
        
        await session.delete(delete_organizador)
        await session.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)


