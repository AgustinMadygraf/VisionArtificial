# src/utils/server_utility.py
import socket
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

class ServerUtility:
    @staticmethod
    def get_local_ip():
        """Obtiene la dirección IP local de la máquina."""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        except Exception as e:
            ip = '127.0.0.1'
            logger.error(f"Error obtaining local IP: {e}")
        finally:
            s.close()
        logger.info(f"Local IP obtained: {ip}")
        return ip
