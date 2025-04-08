from src.util.error import error

def format_api_response(status_code=400, status="error", data=None):
    if status.lower() == "success":
        status_code = 200

    if data is None:
        data = {}

    if status.lower() == "error":
        data = error(data)

    return {
        "statusCode": status_code,
        "status": status,
        "data": data
    }