from src.users.domain.models import User
from src.users.domain.repositories import UserRepository

class UserCreator:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, email: str) -> User:
        existing_user = await self.repository.get_by_email(email)
        if existing_user:
            raise ValueError(f"User with email {email} already exists")
        
        user = User(id=None, email=email)
        await self.repository.add(user)
        return user
