from pydantic_settings import BaseSettings

"""Gets config safely"""

class Settings(BaseSettings):
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
