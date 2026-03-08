import time

user_last_request = {}

RATE_LIMIT_SECONDS = 3

def is_allowed(user_id):
    now = time.time()

    if user_id not in user_last_request:
        user_last_request[user_id] = now
        return True

    if now - user_last_request[user_id] >= RATE_LIMIT_SECONDS:
        user_last_request[user_id] = now
        return True

    return False