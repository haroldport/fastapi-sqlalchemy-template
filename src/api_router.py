from fastapi import APIRouter
from src.users.infrastructure.api.controllers.controllers import router as user_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["Users"])
