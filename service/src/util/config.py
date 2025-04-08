# src/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional
import os

class Settings(BaseSettings):
    """Loads and validates application settings from environment variables."""
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    # --- App Settings ---
    ALLOWED_ORIGINS: List[str] = ["http://localhost:8080"]

    # --- Logging Settings ---
    LOG_LEVEL_CONSOLE: str = "INFO"
    LOG_LEVEL_FILE: str = "INFO"
    LOG_ROTATION: str = "00:00" # Default to midnight rotation
    LOG_RETENTION: str = "7 days"
    # LOG_FILE_NAME: str = "app.log" # <-- Removed
    LOG_DIR: str = "logs"
    LOG_ASYNC: bool = True

    # --- Removed LOG_FILE_PATH property ---
    # The full path is now dynamic due to date formatting

    # --- Helper property for Log Directory Path ---
    @property
    def RESOLVED_LOG_DIR(self) -> str:
        """Constructs the absolute path to the log directory."""
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(project_root, self.LOG_DIR)

# Create a single instance to be imported elsewhere
settings = Settings()