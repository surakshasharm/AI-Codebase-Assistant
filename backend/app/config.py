from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = "test_key"

settings = Settings()