# src/config/network_config.py
import os
from dotenv import load_dotenv

load_dotenv()

NETWORK_CONFIG = {
    'websocket_host': os.getenv('WEBSOCKET_HOST', '0.0.0.0'),
    'websocket_port': int(os.getenv('WEBSOCKET_PORT', 8765)),
    'http_service_url': os.getenv('HTTP_SERVICE_URL', 'http://192.168.0.184')
}
