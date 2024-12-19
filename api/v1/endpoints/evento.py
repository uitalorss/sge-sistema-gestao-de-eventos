from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from core.auth.deps import get_session

from schemas.evento_schema import EventoBaseSchema, EventoSchema, EventoUpdateSchema, EventoResponseSchema
from services.evento_service import create_evento, get_evento, update_evento, delete_evento

router = APIRouter()

@router.post("/", response_model=EventoResponseSchema, status_code=status.HTTP_201_CREATED)
async def post(evento: EventoBaseSchema, db: AsyncSession = Depends(get_session)):
    return await create_evento(evento, db)

@router.get("/{evento_id}", response_model=EventoResponseSchema, status_code=status.HTTP_200_OK)
async def get(evento_id: int, db: AsyncSession = Depends(get_session)):
    return await get_evento(evento_id, db)

@router.put("/{evento_id}", response_model=EventoResponseSchema, status_code=status.HTTP_202_ACCEPTED)
async def put(evento_id: int, evento: EventoUpdateSchema, db: AsyncSession = Depends(get_session)):
    return await update_evento(evento_id, evento, db)

@router.delete("/{evento_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(evento_id: int, db: AsyncSession = Depends(get_session)):
    return await delete_evento(evento_id, db)