# run.py
import uvicorn
import logging

if __name__ == "__main__":
    logging.info("Starting Uvicorn server...")
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True, # Enable auto-reload for development
        log_level="info" # Match log level in main.py if desired
    )