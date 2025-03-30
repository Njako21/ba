# src/logger_config.py
import sys
import os
from loguru import logger

# Import settings from your config file
from src.config import settings

def setup_logging():
    """Configures the Loguru logger based on settings."""

    logger.remove()

    logger.add(
        sys.stderr,
        level=settings.LOG_LEVEL_CONSOLE.upper(),
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</> | <level>{level: <8}</> | <cyan>{name}</>:<cyan>{function}</>:<cyan>{line}</> - <level>{message}</>",
        colorize=True,
        enqueue=settings.LOG_ASYNC
    )

    # Construct the log directory path
    log_directory = settings.RESOLVED_LOG_DIR

    # Ensure the log directory exists
    try:
        os.makedirs(log_directory, exist_ok=True)
    except OSError as e:
        logger.error(f"Error creating log directory {log_directory}: {e}")
        return # Stop configuration if directory cannot be created

    # --- Define the filename pattern using time formatting ---
    # Example: logs/2025-03-30.log
    log_file_pattern = os.path.join(log_directory, "{time:YYYY-MM-DD}.log")
    # --- ---

    logger.info(f"Setting up file logging pattern: {log_file_pattern}") # Log the pattern being used

    logger.add(
        log_file_pattern, # <-- Use the pattern here
        level=settings.LOG_LEVEL_FILE.upper(),
        rotation=settings.LOG_ROTATION, # Rotate daily (at midnight)
        retention=settings.LOG_RETENTION, # Keep logs for specified duration
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        enqueue=settings.LOG_ASYNC,
        catch=True
    )

    logger.info("Logger configured successfully.")
    logger.info(f"Console log level: {settings.LOG_LEVEL_CONSOLE}")
    logger.info(f"File log level: {settings.LOG_LEVEL_FILE}")
    # logger.info(f"Log file path: {log_file_path}") # Path is now dynamic
    logger.info(f"Log directory: {log_directory}")
    logger.info(f"Log rotation: {settings.LOG_ROTATION}")
    logger.info(f"Log retention: {settings.LOG_RETENTION}")
    logger.info(f"Async logging: {settings.LOG_ASYNC}")