from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.exc import IntegrityError
from schemas.user_schema import CreateUserSchema, LoginUserSchema
from models.user_model import User
from models.profile_model import Profile
from core.auth.security import generate_hashed_password, verify_password
from core.auth.auth import create_access_token

async def create_user(user: CreateUserSchema, db: AsyncSession):
    new_user: User = User(nome=user.nome, email=user.email, senha=generate_hashed_password(user.senha), telefone=user.telefone)
    async with db as session:
        try:
            session.add(new_user)
            await session.flush()
            for perfil_item in user.perfil:
                new_perfil: Profile = Profile(usuario_id=new_user.id, tipo_perfil=perfil_item)
                session.add(new_perfil)
            
            await session.commit()

            return new_user
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Favor verificar dados.")
        
async def login_user(user_data: LoginUserSchema, db: AsyncSession):
    async with db as session:
        query = select(User).options(selectinload(User.perfil)).filter(User.email == user_data.email)
        result = await session.execute(query)
        user = result.scalars().unique().one_or_none()

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário e/ou senha incorretos.")
        
        if not verify_password(user_data.senha, user.senha):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário e/ou senha incorretos.")
        
        profile_priority = {
            "ORGANIZADOR": 1,
            "PARTICIPANTE": 2,
        }

        high_access_profile = min(user.perfil, key=lambda profile: profile_priority.get(profile.tipo_perfil, float("inf")))
        return create_access_token(sub=str(user.id), data_type=high_access_profile.tipo_perfil)


