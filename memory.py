chat_memory = {}

def get_user_memory(user_id):
    if user_id not in chat_memory:
        chat_memory[user_id] = []
    return chat_memory[user_id]

def reset_memory(user_id):
    chat_memory[user_id] = []