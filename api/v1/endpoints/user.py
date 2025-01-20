from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_schema import UserSchema, CreateUserSchema, LoginUserSchema
from core.auth.deps import get_session
from services.user_service import create_user, login_user
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_user(user: CreateUserSchema, db: AsyncSession = Depends(get_session)):
    return await create_user(user, db)

@router.post("/login", status_code=status.HTTP_200_OK)
async def post_login_user(user_data: LoginUserSchema, db: AsyncSession = Depends(get_session)):
    return await login_user(user_data, db)