"""
src/main.py
Módulo principal del servidor de mensajería. 
Inicializa y ejecuta el servidor HTTP y WebSocket.
"""
import asyncio
from views.http_server import HTTPServer, MyHTTPRequestHandler
from views.websocket_server import WebSocketServer, WebSocketHandler, HTTPHandler, MessageHandler
from utils.server_utility import ServerUtility
from services.http_service import HTTPService
from services.ssl_service import SSLService
from logs.config_logger import LoggerConfigurator

async def run_server():
    """Inicializa y ejecuta el servidor HTTP y WebSocket."""    
    local_ip = ServerUtility.get_local_ip()
    ssl_service = SSLService()
    logger = LoggerConfigurator().configure()
    http_service = HTTPService(logger)
    http_request_handler = HTTPHandler(http_service)
    message_handler = MessageHandler(http_request_handler)
    websocket_handler = WebSocketHandler(message_handler)

    http_server = HTTPServer((local_ip, 4443), MyHTTPRequestHandler, ssl_service)
    http_server.start()

    websocket_server = WebSocketServer(ssl_service, websocket_handler)
    await websocket_server.start()

if __name__ == '__main__':
    asyncio.run(run_server())
