# src/views/websocket_server.py
import asyncio
import websockets
import requests
import socket
from logs.config_logger import logger_configurator

logger = logger_configurator.get_logger()

class WebSocketServer:
    def __init__(self, address, ssl_config):
        self.address = address
        self.ssl_config = ssl_config

    async def handler(self, websocket, path):
        try:
            async for message in websocket:
                logger.info(f"Received message: {message}")
                try:
                    message_as_int = int(message[25:])
                    tolerancia = 10
                    upper_threshold = tolerancia
                    lower_threshold = -tolerancia

                    if message_as_int > upper_threshold:
                        self.send_http_request('http://192.168.0.184/ena_f')
                    elif message_as_int < lower_threshold:
                        self.send_http_request('http://192.168.0.184/ena_r')
                except ValueError:
                    logger.error("Failed to convert message to integer")
        except websockets.exceptions.ConnectionClosedError as e:
            logger.error(f"WebSocket connection closed: {e}")
        except Exception as e:
            logger.error(f"Unhandled exception in WebSocket handler: {e}")

    def send_http_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            logger.debug(f"Sent HTTP GET to {url}, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to connect to {url}: {str(e).split(':')[0]}")  # Simplify the error message

    def start(self):
        async def main():
            ssl_context = self.ssl_config.get_ssl_context()
            try:
                server = await websockets.serve(self.handler, self.address[0], 8765, ssl=ssl_context)
                # Set the reuse address option
                server.sockets[0].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                await asyncio.Future()  # Run forever
            except Exception as e:
                logger.error(f"Failed to start WebSocket server: {e}")

        asyncio.run(main())
