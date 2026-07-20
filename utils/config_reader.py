import logging

import yaml

logger = logging.getLogger(__name__)


class ConfigReader:
    _config = None  # cached after first read
    _config_path = "config/config.yml"

    @staticmethod
    def read_config():
        if ConfigReader._config is None:
            try:
                with open(ConfigReader._config_path, "r") as file:
                    ConfigReader._config = yaml.safe_load(file)
            except FileNotFoundError:
                logger.error("Config file not found: %s", ConfigReader._config_path)
                raise
        return ConfigReader._config