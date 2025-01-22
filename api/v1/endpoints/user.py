from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_schema import CreateUserSchema, LoginUserSchema, UserResponseSchema
from models.user_model import User
from models.profile_model import PerfilEnum
from core.auth.deps import get_session, get_current_user
from services.user_service import create_user, login_user, get_user_data, update_profile, add_profile
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_user(
    user: CreateUserSchema,
    db: AsyncSession = Depends(get_session)
):
    return await create_user(user, db)

@router.post("/login", status_code=status.HTTP_200_OK)
async def post_login_user(
    user_data: LoginUserSchema,
    db: AsyncSession = Depends(get_session)
):
    token = await login_user(user_data, db)

    return JSONResponse(content={"access_token": token, "token-type": "bearer"}, status_code=status.HTTP_202_ACCEPTED)

@router.get("/", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_user(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    return await get_user_data(user_id=user.id, db=db)

@router.patch("/update-profile", status_code=status.HTTP_200_OK)
async def patch_current_profile(
    profile_to_update: PerfilEnum,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    return await update_profile(user_id=user.id, profile_to_update=profile_to_update, db=db)

@router.post("/create-profile", status_code=status.HTTP_201_CREATED)
async def post_add_profile(
    profile_to_add: PerfilEnum,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    return await add_profile(user_id=user.id, profile_to_add=profile_to_add, db=db)