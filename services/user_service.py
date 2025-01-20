from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from schemas.user_schema import CreateUserSchema
from models.user_model import User
from models.profile_model import Profile
from core.auth.security import generate_hashed_password

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
