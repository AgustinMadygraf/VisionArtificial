"""
src/utils/server_utility.py
This module provides utility functions for server operations.
"""

import socket
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

class ServerUtility:
    """
    Utility class for server-related operations.
    """

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

    @staticmethod
    def dummy_method():
        """A dummy method to avoid too-few-public-methods warning."""
        pass