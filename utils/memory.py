import json
import os

HISTORY_FILE = "chat_history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def add_to_history(user, assistant):
    history = load_history()
    
    history.append({"user": user, "assistant": assistant})
    
    save_history(history)


def get_history_text():
    history = load_history()
    
    formatted = []
    for item in history:
        formatted.append(f"User: {item['user']}")
        formatted.append(f"Assistant: {item['assistant']}")
    
    return "\n".join(formatted)