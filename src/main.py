# src/main.py
import os
import asyncio
from views.http_server import HTTPServer
from views.websocket_server import WebSocketServer
from views.http_server import MyHTTPRequestHandler
from utils.ssl_config import SSLConfig
from utils.server_utility import ServerUtility

async def run_server():
    local_ip = ServerUtility.get_local_ip()
    ssl_config = SSLConfig()

    http_server = HTTPServer((local_ip, 4443), MyHTTPRequestHandler, ssl_config)
    http_server.start()

    websocket_server = WebSocketServer((local_ip, 8765), ssl_config)
    await websocket_server.start()  # Await the coroutine

if __name__ == '__main__':
    web_dir = '.'
    os.chdir(web_dir)
    asyncio.run(run_server())  # Use asyncio.run to execute the async function
