from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.domain.models import User
from src.users.infrastructure.persistence.models import UserORM

class SQLAlchemyUserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, user: User) -> None:
        user_orm = UserORM(
            email=user.email,
            is_active=user.is_active
        )
        self.session.add(user_orm)
        # We don't flush/refresh here to keep it pure if needed, 
        # but if we need the ID immediately:
        # await self.session.flush()
        # user.id = user_orm.id

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(
            select(UserORM).where(UserORM.email == email)
        )
        user_orm = result.scalars().first()
        if not user_orm:
            return None
            
        return User.from_primitives({
            "id": user_orm.id,
            "email": user_orm.email,
            "is_active": user_orm.is_active
        })
