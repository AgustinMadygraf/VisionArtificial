# src/config/logger_config.py
import os
import json
import logging.config

def configure_logger():
    config_path = os.getenv('LOG_CFG', 'src/logs/logging.json')
    if os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

logger = configure_logger()
