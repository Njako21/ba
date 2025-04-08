# src/logger_config.py
import sys
import os
from loguru import logger

# Import settings from your config file
from src.util.config import settings

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
        log(f"Error creating log directory {log_directory}: {e}", level="error")
        return # Stop configuration if directory cannot be created

    # --- Define the filename pattern using time formatting ---
    # Example: logs/2025-03-30.log
    log_file_pattern = os.path.join(log_directory, "{time:YYYY-MM-DD}.log")
    # --- ---

    log(f"Setting up file logging pattern: {log_file_pattern}") # Log the pattern being used

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

    log("Logger configured successfully.")
    log(f"Console log level: {settings.LOG_LEVEL_CONSOLE}")
    log(f"File log level: {settings.LOG_LEVEL_FILE}")
    # logger.info(f"Log file path: {log_file_path}") # Path is now dynamic
    log(f"Log directory: {log_directory}")
    log(f"Log rotation: {settings.LOG_ROTATION}")
    log(f"Log retention: {settings.LOG_RETENTION}")
    log(f"Async logging: {settings.LOG_ASYNC}")

def log(message, level="info"):
    if level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    elif level == "debug":
        logger.debug(message)
    else:
        logger.info(message)