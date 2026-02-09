from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db_session
from src.shared.infrastructure.sqlalchemy.uow import UnitOfWorkWrapper
from src.users.domain.repositories import UserRepository
from src.users.infrastructure.persistence.sqlalchemy_user_repository import SQLAlchemyUserRepository
from src.users.application.user_creator import UserCreator

def get_user_repository(
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> UserRepository:
    return SQLAlchemyUserRepository(session)

def get_user_creator(
    session: Annotated[AsyncSession, Depends(get_db_session)],
    repository: Annotated[UserRepository, Depends(get_user_repository)],
) -> UserCreator:
    use_case = UserCreator(repository)
    return UnitOfWorkWrapper(use_case, session)

UserCreatorProvider = Annotated[UserCreator, Depends(get_user_creator)]
