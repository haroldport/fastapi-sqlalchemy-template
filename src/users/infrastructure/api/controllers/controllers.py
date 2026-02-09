from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel, EmailStr
from src.users.infrastructure.api.dependencies import UserCreatorProvider

router = APIRouter()

class CreateUserRequest(BaseModel):
    email: EmailStr

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(
    request: CreateUserRequest,
    user_creator: UserCreatorProvider
):
    try:
        await user_creator.execute(email=request.email)
        return Response(status_code=status.HTTP_201_CREATED)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
