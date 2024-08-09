# src/main.py
import os
import asyncio   #agregado
import schedule  #agregado
import time
from views.http_server import HTTPServer, MyHTTPRequestHandler
from views.websocket_server import WebSocketServer, WebSocketHandler, HTTPRequestHandler, MessageHandler
from utils.server_utility import ServerUtility
from services.http_service import HTTPService
from services.ssl_service import SSLService
from src.logs.config_logger import LoggerConfigurator

async def run_server():
    local_ip = ServerUtility.get_local_ip()
    ssl_service = SSLService()
    logger = LoggerConfigurator().configure()
    http_service = HTTPService(logger)
    http_request_handler = HTTPRequestHandler(http_service)
    message_handler = MessageHandler(http_request_handler)
    websocket_handler = WebSocketHandler(message_handler)

    http_server = HTTPServer((local_ip, 4443), MyHTTPRequestHandler, ssl_service)
    http_server.start()

    websocket_server = WebSocketServer(ssl_service, websocket_handler)
    await websocket_server.start()

if __name__ == '__main__':
    asyncio.run(run_server())