"""
src/config/network_config.py
This module defines the network configuration for the server, including the WebSocket
"""

import os
from dotenv import load_dotenv

load_dotenv()

NETWORK_CONFIG = {
    'websocket_host': os.getenv('WEBSOCKET_HOST', '0.0.0.0'),
    'websocket_port': int(os.getenv('WEBSOCKET_PORT', '8765')),
    'http_service_url': os.getenv('HTTP_SERVICE_URL', 'http://192.168.0.184'),
    'ssl_cert_path': os.getenv('SSL_CERT_PATH', './server.crt'),
    'ssl_key_path': os.getenv('SSL_KEY_PATH', './server.key')
}
