"""
src/main.py
Módulo principal del servidor de mensajería. 
Inicializa y ejecuta el servidor HTTP y WebSocket.
"""
import asyncio
from src.views.websocket_server import WebSocketServer, WebSocketHandler, HTTPHandler, MessHandler
from src.utils.server_utility import ServerUtility
from src.services.http_service import HTTPService
from src.services.ssl_service import SSLService
from src.views.server.request_handler import MyHTTPRequestHandler
from src.views.server.http_server import HTTPServer
from src.logs.config_logger import LoggerConfigurator

# Configuración del logger al inicio del script
logger = LoggerConfigurator().configure()
logger.debug("Logger configurado correctamente al inicio del servidor.")

async def run_server():
    """Inicializa y ejecuta el servidor HTTP y WebSocket."""
    puerto = 8080
    local_ip = ServerUtility.get_ip()
    ssl_service = SSLService()
    http_service = HTTPService(logger)
    http_request_handler = HTTPHandler(http_service)
    message_handler = MessHandler(http_request_handler)
    websocket_handler = WebSocketHandler(message_handler)

    http_server = HTTPServer((local_ip, puerto), MyHTTPRequestHandler, ssl_service)
    http_server.start()

    websocket_server = WebSocketServer(ssl_service, websocket_handler)
    await websocket_server.start()

if __name__ == '__main__':
    asyncio.run(run_server())
