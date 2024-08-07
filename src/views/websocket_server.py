# src/views/websocket_server.py
import asyncio
import requests
from websockets import serve
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK
from src.config.network_config import NETWORK_CONFIG
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

class WebSocketServer:
    def __init__(self, ssl_service, handler):
        self.address = (NETWORK_CONFIG['websocket_host'], NETWORK_CONFIG['websocket_port'])
        self.ssl_service = ssl_service
        self.handler = handler

    async def start(self):
        ssl_context = self.ssl_service.get_ssl_context()
        try:
            async with serve(self.handler.handle, self.address[0], self.address[1], ssl=ssl_context, ping_interval=None):
                logger.info(f"WebSocket server started at wss://{self.address[0]}:{self.address[1]}")
                await asyncio.Future()  # Run forever
        except Exception as e:
            logger.error(f"Failed to start WebSocket server: {e}")

class WebSocketHandler:
    def __init__(self, message_handler):
        self.message_handler = message_handler

    async def handle(self, websocket, path):
        try:
            async for message in websocket:
                logger.info(f"Received message: {message}")
                await self.message_handler.process_message(message)
        except ConnectionClosedError as e:
            logger.error(f"WebSocket connection closed with error: {e}")
        except ConnectionClosedOK:
            logger.info("WebSocket connection closed normally.")
        except Exception as e:
            logger.error(f"Unhandled exception in WebSocket handler: {e}")

class HTTPRequestHandler:
    def __init__(self, http_service, max_attempts=5):
        self.http_service = http_service
        self.failed_attempts = 0
        self.max_attempts = max_attempts

    def send_request(self, url):
        if self.failed_attempts >= self.max_attempts:
            logger.warning(f"Maximum failed attempts reached. Stopping requests to {url}.")
            return

        try:
            self.http_service.send_request(url)
            self.failed_attempts = 0  # Reset the counter on a successful request
        except requests.exceptions.RequestException as e:
            self.failed_attempts += 1
            logger.error(f"Failed to connect to {url}: {str(e).split(':')[0]} (Attempt {self.failed_attempts})")

class MessageHandler:
    def __init__(self, http_request_handler, tolerance=10):
        self.http_request_handler = http_request_handler
        self.tolerance = tolerance

    async def process_message(self, message):
        try:
            message_as_int = int(message[25:])
            upper_threshold = self.tolerance
            lower_threshold = -self.tolerance

            if message_as_int > upper_threshold:
                self.http_request_handler.send_request('http://192.168.0.184/ena_f')
            elif message_as_int < lower_threshold:
                self.http_request_handler.send_request('http://192.168.0.184/ena_r')
        except ValueError:
            logger.error("Failed to convert message to integer")
