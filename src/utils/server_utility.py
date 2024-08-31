"""
src/utils/server_utility.py
This module provides utility functions for server operations.
"""

import socket
import os
from dotenv import load_dotenv
from src.logs.config_logger import LoggerConfigurator

# Load environment variables from .env file
load_dotenv()

logger = LoggerConfigurator().configure()

class ServerUtility:
    """
    Utility class for server-related operations.
    """
    # pylint: disable=too-few-public-methods
    @staticmethod
    def get_ip():
        """Obtiene la dirección IP"""
        ip = ServerUtility.get_local_ip()
        return ip

    @staticmethod
    def get_ip_from_env():
        """Obtiene la IP del entorno (DB_HOST) del archivo .env."""
        ip_env = os.getenv('DB_HOST', '127.0.0.1')
        logger.info("IP from environment (DB_HOST): %s", ip_env)
        return ip_env

    @staticmethod
    def get_local_ip():
        """Obtiene la dirección IP local de la máquina."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except socket.error as e:
            ip = '127.0.0.1'
            logger.error("Error obtaining local IP: %s", e)
        finally:
            s.close()
        logger.info("Local IP obtained: %s", ip)
        return ip
