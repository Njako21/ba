from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.util.logger_config import log

from src.util.config import settings
from src.routers import rest_endpoints, stream_endpoints

from src.util.response_formatter import format_api_response

# --- FastAPI App Initialization ---
log("Initializing FastAPI application...")
app = FastAPI(
    title="The api",
    description="api for the project",
    version="1.0.0"
)

# --- CORS Middleware Configuration ---
log(f"Configuring CORS with allowed origins: {settings.ALLOWED_ORIGINS}")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include Routers ---
log("Including API routers...")
app.include_router(rest_endpoints.router, prefix="/api")
app.include_router(stream_endpoints.router, prefix="/api")

# --- Root Endpoint ---
@app.get("/")
async def root():
    log("Root endpoint '/' accessed.")
    return format_api_response(
        status="success",
        data={"message": "WELCOME go to /docs for API documentation."}
    )

@app.on_event("startup")
async def startup_event():
    log("Application startup sequence initiated.")
    log("Application startup complete.")


@app.on_event("shutdown")
async def shutdown_event():
    log("Application shutting down.")
    log("Shutdown complete.")
