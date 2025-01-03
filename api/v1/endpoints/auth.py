from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from core.auth.deps import get_session
from schemas.auth_schema import LoginSchema, LoginResponseSchema
from services.organizador_service import login_organizador
from services.participante_service import login_participante
from utils.errors.error_responses import login_responses

router = APIRouter()

@router.post("/", status_code=status.HTTP_202_ACCEPTED, response_model=LoginResponseSchema, responses=login_responses)
async def login(login_data: LoginSchema, db: AsyncSession = Depends(get_session)):
    token = await login_organizador(login_data, db) if login_data.auth_type == "Organizador" else await login_participante(login_data, db)

    return JSONResponse(content={"access_token": token, "token-type": "bearer"}, status_code=status.HTTP_202_ACCEPTED)