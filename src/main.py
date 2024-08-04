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

async def run_store_data():
    while True:
        print("")
        print('Storing data...')
        print("")
        #os.system('python src/store_data.py')
        await asyncio.sleep(300)  # Espera de 300 segundos

async def run_main():
    await asyncio.gather(
        run_server(),
        run_store_data()
    )