# src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Remove standard logging import if you had one
# import logging
# import sys

# Import Loguru logger and the setup function
from loguru import logger
from src.logger_config import setup_logging

# Import settings and routers
from src.config import settings
from src.routers import rest_endpoints, stream_endpoints

# --- CONFIGURE LOGGING ---
# Call the setup function BEFORE initializing FastAPI or doing anything else
# that might log. This ensures all logs use the new configuration.
setup_logging()

# --- FastAPI App Initialization ---
logger.info("Initializing FastAPI application...")
app = FastAPI(
    title="FastAPI Pub/Sub Example",
    description="Demonstrates REST and Streaming endpoints with Pub/Sub pattern.",
    version="1.0.0"
)

# --- CORS Middleware Configuration ---
logger.info(f"Configuring CORS with allowed origins: {settings.ALLOWED_ORIGINS}")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include Routers ---
logger.info("Including API routers...")
app.include_router(rest_endpoints.router, prefix="/api")
app.include_router(stream_endpoints.router, prefix="/api")

# --- Root Endpoint ---
@app.get("/")
async def root():
    """Basic root endpoint for health check or info."""
    logger.info("Root endpoint '/' accessed.")
    return {"message": "Welcome to the FastAPI Pub/Sub Example!"}

# --- Optional Startup/Shutdown Events ---
@app.on_event("startup")
async def startup_event():
    # Log using Loguru
    logger.info("Application startup sequence initiated.")
    # Example: Simulate connecting to a hypothetical database
    # logger.debug("Connecting to database...")
    # await asyncio.sleep(0.1) # Simulate async operation
    # logger.info("Database connection established (simulated).")
    logger.info("Application startup complete.")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down.")
    # Example: Simulate cleanup
    # logger.debug("Closing database connection...")
    # await asyncio.sleep(0.1) # Simulate async operation
    # logger.info("Database connection closed (simulated).")
    logger.info("Shutdown complete.")

# Uvicorn command remains the same:
# uvicorn src.main:app --reload --host 0.0.0.0 --port 8000