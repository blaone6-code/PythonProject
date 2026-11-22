import os
import yaml

class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def get(self, key_path: str, default=None):
        keys = key_path.split(".")
        value = self.config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value