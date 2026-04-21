"""
app/config.py — Centralised configuration loaded from .env
"""
import logging
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Application settings — values are read from the .env file."""

    app_title: str = "SGOD API"
    app_version: str = "1.0.0"
    app_env: str = "development"
    host: str = "127.0.0.1"
    port: int = 8000
    allowed_origins: str = "http://localhost:3000,http://localhost:3001"
    log_level: str = "INFO"

    @property
    def origins_list(self) -> list[str]:
        """Parse comma-separated ALLOWED_ORIGINS into a Python list."""
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """Return a cached singleton of Settings."""
    return Settings()


def setup_logging(level: str = "INFO") -> None:
    """Configure root logger with a consistent format."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(name)s — %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
