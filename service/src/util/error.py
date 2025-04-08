import src.util.logger_config as log

def error(msg):
    log(msg, level="error")
    return {"message": msg}
