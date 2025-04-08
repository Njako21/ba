# src/routers/rest_endpoints.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from src.util.logger_config import log

from src.util.response_formatter import format_api_response
from src.util.gitlab import validate_gitlab_token, get_user_repositories


router = APIRouter()

# --- GET Endpoints ---
@router.get("/get/model/data/repositories")
async def get_repositories(token: str):
    log(f"GET /get/model/data/repositories called with token: {token}")

    if not validate_gitlab_token(token):
        log("Invalid GitLab token provided.", level="error")
        raise HTTPException(status_code=401, detail="Invalid GitLab token.")

    repositories = get_user_repositories(token)
    if not repositories:
        log("No repositories found.", level="warning")
        raise HTTPException(status_code=404, detail="No repositories found.")

    return format_api_response(status="success", data=repositories)


@router.get("/get/model/data/repository/{repo_id}")
async def get_repository(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /get/model/data/repository/"}
    )


@router.get("/get/model/data/training/{repo_id}")
async def get_training(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /get/model/data/training/"}
    )


@router.get("/get/model/schedule/{repo_id}")
async def get_schedule(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /get/model/schedule/"}
    )


@router.get("/get/model/training/status/{repo_id}")
async def get_training_status(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /get/model/training/status/"}
    )


# --- POST Endpoints ---

@router.post("/post/model/start/training/{repo_id}")
async def post_training(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /post/model/start/training/"}
    )

@router.post("/post/model/stop/training/{repo_id}")
async def post_training(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /post/model/stop/training/"}
    )

@router.post("/post/model/change/schedule/{repo_id}")
async def post_schedule(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /post/model/change/schedule/"}
    )

@router.post("/post/model/set/schedule/{repo_id}")
async def post_schedule(repo_id: str):
    return format_api_response(
        status="error",
        data={"message": f"not implemented yet /post/model/set/schedule/"}
    )