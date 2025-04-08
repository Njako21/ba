# run.py
import uvicorn
from src.util.logger_config import log, setup_logging
from dotenv import load_dotenv
import os

load_dotenv() 

setup_logging()

if __name__ == "__main__":
    ENVport = int(os.getenv("PORT", 8000))
    ENVrunmode = os.getenv("RUN_MODE", "prod")
    ENVhost = os.getenv("HOST", "localhost")

    logMode = "info"
    reloadMode = False
    if ENVrunmode == "dev":
        reloadMode = True
        logMode = "debug"

    log("Starting Uvicorn server...")
    uvicorn.run(
        "src.main:app",
        host=ENVhost,
        port=ENVport,
        reload=reloadMode,
        log_level=logMode
    )