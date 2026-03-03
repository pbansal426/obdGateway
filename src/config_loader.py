import json
import os

def load_config():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, "config", "settings.json")

    with open(config_path, "r") as f:
        return json.load(f)