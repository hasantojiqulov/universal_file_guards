from pydantic import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    ADMIN_IDS: list[int] = []
    STORAGE_PATH: str = "/tmp/ufs_files"
    MAX_FILE_SIZE_MB: int = 50
    CLAMD_HOST: str = "clamav"
    CLAMD_PORT: int = 3310
    MONGO_URI: str = "mongodb://mongo:27017"
    DB_NAME: str = "ufs"
    ENV: str = "production"

    class Config:
        env_file = ".env"

settings = Settings()
