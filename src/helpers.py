import os, json


def load_dataset(name: str) -> any:
    filename = f"./src/data/{name}.json"
    if not os.path.exists(filename):
        print(f"Dataset {filename} not found!")
        return None
    
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
