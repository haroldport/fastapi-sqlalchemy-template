from fastapi import FastAPI
from .config import settings
from .api_router import router as api_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
