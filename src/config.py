from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/postgres"
    PROJECT_NAME: str = "FastAPI Project"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
