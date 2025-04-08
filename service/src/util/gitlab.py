import requests
from dotenv import load_dotenv
from src.util.logger_config import log
import os

load_dotenv()
gitlab_url = os.getenv("GITLAB_URL", "http://localhost")
def validate_gitlab_token(token):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{gitlab_url}/api/v4/user", headers=headers)
        return response.status_code == 200
    except requests.RequestException as e:
        log(f"Error validating token: {e}", level="error")
        return 
    
def get_user_repositories(token):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{gitlab_url}/api/v4/projects", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            log(f"Failed to fetch repositories: {response.status_code} - {response.text}", level="error")
            return []
    except requests.RequestException as e:
        log(f"Error fetching repositories: {e}", level="error")
        return []