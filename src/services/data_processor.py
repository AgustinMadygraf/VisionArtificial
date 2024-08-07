# src/services/data_processor.py

import re
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

class DataProcessor:
    @staticmethod
    def extract_vueltas(html):
        try:
            match = re.search(r'Vueltas:\s*(\d+)', html)
            if match:
                return int(match.group(1))
            else:
                logger.info("Vueltas value not found in the response.")
                return None
        except re.error as e:
            logger.error(f"Error extracting data: {e}")
            return None
