import json
import os

def load_knowledge(path):
    if not os.path.exists(path):
        return {"questions": [], "characters": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_knowledge(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
