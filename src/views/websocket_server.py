#src/views/websocket_server.py
import asyncio
import websockets
import requests
from logs.config_logger import logger_configurator

logger = logger_configurator.get_logger()

class WebSocketServer:
    def __init__(self, address, ssl_config):
        self.address = address
        self.ssl_config = ssl_config

    async def handler(self, websocket, path):
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

    def send_http_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            logger.info(f"Sent HTTP GET to {url}")
            logger.debug(f"Response status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"HTTP request to {url} failed: {e}")

    def start(self):
        async def main():
            ssl_context = self.ssl_config.get_ssl_context()
            async with websockets.serve(self.handler, self.address[0], 8765, ssl=ssl_context):
                await asyncio.Future()  # Run forever

        asyncio.run(main())
