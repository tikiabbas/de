import yaml
from typing import Dict, Any


class ConfigManager:
    """
    Configuration management utility
    Reflects Abbas's experience at Lingaro and Coca-Cola projects
    """

    @staticmethod
    def load_config(config_path: str) -> Dict[str, Any]:
        """
        Load configuration from YAML file
        Inspired by Abbas's work with dynamic ETL configurations
        """
        try:
            with open(config_path, "r") as config_file:
                return yaml.safe_load(config_file)
        except Exception as e:
            raise ValueError(f"Error loading configuration: {e}")
