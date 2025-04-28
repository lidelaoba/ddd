import json
import os
import time
from datetime import datetime

class Auth:
    def __init__(self):
        self.keys_file = "keys.json"
        self._load_keys()

    def _load_keys(self):
        if not os.path.exists(self.keys_file):
            self.keys = {}
            self._save_keys()
        else:
            with open(self.keys_file, 'r') as f:
                self.keys = json.load(f)

    def _save_keys(self):
        with open(self.keys_file, 'w') as f:
            json.dump(self.keys, f)

    def verify_key(self, key: str) -> bool:
        if key not in self.keys:
            return False
        
        key_data = self.keys[key]
        if key_data.get("expired", False):
            return False

        expire_time = key_data.get("expire_time")
        if expire_time and datetime.fromtimestamp(expire_time) < datetime.now():
            self.keys[key]["expired"] = True
            self._save_keys()
            return False

        return True

    def add_key(self, key: str, expire_days: int = 30):
        expire_time = time.time() + (expire_days * 24 * 60 * 60)
        self.keys[key] = {
            "expire_time": expire_time,
            "expired": False
        }
        self._save_keys()

    def remove_key(self, key: str):
        if key in self.keys:
            del self.keys[key]
            self._save_keys() 