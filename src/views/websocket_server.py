# src/views/websocket_server.py
import asyncio
import websockets
import requests
import socket
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK
from logs.config_logger import logger_configurator

logger = logger_configurator.get_logger()

class WebSocketServer:
    def __init__(self, address, ssl_config):
        self.address = address
        self.ssl_config = ssl_config
        self.failed_attempts = 0
        self.max_attempts = 5

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
        except ConnectionClosedError as e:
            logger.error(f"WebSocket connection closed with error: {e}")
        except ConnectionClosedOK:
            logger.info("WebSocket connection closed normally.")
        except Exception as e:
            logger.error(f"Unhandled exception in WebSocket handler: {e}")

    def send_http_request(self, url):
        if self.failed_attempts >= self.max_attempts:
            logger.warning(f"Maximum failed attempts reached. Stopping requests to {url}.")
            return

        try:
            response = requests.get(url)
            response.raise_for_status()
            logger.debug(f"Sent HTTP GET to {url}, status code: {response.status_code}")
            self.failed_attempts = 0  # Reset the counter on a successful request
        except requests.exceptions.RequestException as e:
            self.failed_attempts += 1
            logger.error(f"Failed to connect to {url}: {str(e).split(':')[0]} (Attempt {self.failed_attempts})")

    async def start(self):
        ssl_context = self.ssl_config.get_ssl_context()
        try:
            async with websockets.serve(self.handler, self.address[0], 8765, ssl=ssl_context, ping_interval=None):
                logger.info(f"WebSocket server started at wss://{self.address[0]}:{8765}")
                await asyncio.Future()  # Run forever
        except Exception as e:
            logger.error(f"Failed to start WebSocket server: {e}")
