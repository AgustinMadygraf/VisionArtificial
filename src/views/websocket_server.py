"""
src/views/websocket_server.py
This module implements a WebSocket server with SSL support and message handling.
"""
import asyncio
import subprocess
import requests
from websockets.server import serve
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK
from src.config.network_config import NETWORK_CONFIG
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

def get_pid_using_port(port):
    """
    Get the PID of the process using the specified port.

    Args:
        port (int): The port number.

    Returns:
        int: The PID of the process using the port, or None if not found.
    """
    try:
        result = subprocess.check_output(
            f"netstat -ano | findstr :{port}", shell=True
        ).decode()
        if result:
            lines = result.strip().split("\n")
            for line in lines:
                if f":{port}" in line:
                    return int(line.strip().split()[-1])
    except subprocess.CalledProcessError:
        return None
    return None

def kill_process(pid):
    """
    Kill the process with the specified PID.

    Args:
        pid (int): The PID of the process to kill.
    """
    try:
        subprocess.check_output(f"taskkill /PID {pid} /F", shell=True)
        logger.info("Successfully terminated process with PID %d.", pid)
    except subprocess.CalledProcessError as error:
        logger.error("Failed to terminate process with PID %d. Error: %s", pid, error)

class WebSocketServer:
    """
    Class responsible for starting and managing a WebSocket server.

    SOLID Principles Applied:
    - Single Responsibility Principle (SRP): This class 
    is responsible for managing the WebSocket server.
    - Dependency Inversion Principle (DIP): Depends on 
    abstractions for SSL service and message handler.
    """
    def __init__(self, ssl_service, handler):
        """
        Initialize the WebSocket server.

        Args:
            ssl_service: SSL service for handling SSL configuration.
            handler: Message handler for processing received messages.
        """
        self.address = (
            NETWORK_CONFIG['websocket_host'],
            NETWORK_CONFIG['websocket_port']
        )
        self.ssl_service = ssl_service
        self.handler = handler

    async def start(self):
        """
        Start the WebSocket server and configure it to run indefinitely.
        """
        ssl_context = self.ssl_service.get_ssl_context()
        port = self.address[1]
        pid = get_pid_using_port(port)
        if pid:
            logger.info(
                "Port %d is being used by PID %d. Terminating the process...",
                port, pid
            )
            kill_process(pid)
            await asyncio.sleep(2)  # Wait for a moment to ensure the port is released

        try:
            async with serve(
                self.handler.handle, self.address[0], self.address[1],
                ssl=ssl_context, ping_interval=None
            ):
                logger.info(
                    "WebSocket server started at wss://%s:%d",
                    self.address[0], self.address[1]
                )
                await asyncio.Future()  # Run indefinitely
        except (OSError, asyncio.TimeoutError) as error:
            logger.error("Failed to start WebSocket server: %s", error)

class WebSocketHandler:
    """
    Class responsible for handling WebSocket connections and messages.

    SOLID Principles Applied:
    - Single Responsibility Principle (SRP): Handles WebSocket connections and messages.
    """
    def __init__(self, message_handler):
        """
        Initialize the WebSocket handler.

        Args:
            message_handler: Message handler for processing received messages.
        """
        self.message_handler = message_handler

    async def handle(self, websocket, _):
        """
        Handle WebSocket connections and process received messages.

        Args:
            websocket: WebSocket connection.
            path: Unused WebSocket path.
        """
        try:
            async for message in websocket:
                logger.info("Received message: %s", message)
                await self.message_handler.process_message(message)
        except ConnectionClosedError as error:
            logger.error("WebSocket connection closed with error: %s", error)
        except ConnectionClosedOK:
            logger.info("WebSocket connection closed normally.")
        except (OSError, asyncio.TimeoutError) as error:
            logger.error("Unhandled exception in WebSocket handler: %s", error)

class HTTPHandler:
    """
    Class responsible for sending HTTP requests and handling failed attempts.

    SOLID Principles Applied:
    - Single Responsibility Principle (SRP): Handles sending HTTP requests.
    """
    def __init__(self, http_service, max_attempts=5):
        """
        Initialize the HTTP request handler.

        Args:
            http_service: HTTP service for sending requests.
            max_attempts: Maximum number of attempts in case of failure.
        """
        self.http_service = http_service
        self.failed_attempts = 0
        self.max_attempts = max_attempts

    def send_request(self, url):
        """
        Send an HTTP request to the specified URL and handle failed attempts.

        Args:
            url (str): URL to send the request to.
        """
        if self.failed_attempts >= self.max_attempts:
            logger.warning(
                "Maximum failed attempts reached. Stopping requests to %s.", url
            )
            return

        try:
            self.http_service.send_request(url)
            self.failed_attempts = 0  # Reset the counter on success
        except requests.exceptions.RequestException as error:
            self.failed_attempts += 1
            logger.error(
                "Failed to connect to %s: %s (Attempt %d)",
                url, str(error).split(':', maxsplit=1)[0], self.failed_attempts
            )

class MessageHandler:
    """
    Class responsible for processing messages received via WebSocket.

    SOLID Principles Applied:
    - Single Responsibility Principle (SRP): Processes received messages.
    """
    def __init__(self, http_request_handler, tolerance=10):
        """
        Initialize the message handler.

        Args:
            http_request_handler: HTTP request handler for sending requests based on messages.
            tolerance: Tolerance threshold for determining the action to take.
        """
        self.http_request_handler = http_request_handler
        self.tolerance = tolerance

    async def process_message(self, message):
        """
        Process a received message and send an HTTP request based on the message content.

        Args:
            message (str): Received message.
        """
        try:
            message_as_int = int(message[25:])
            upper_threshold = self.tolerance
            lower_threshold = -self.tolerance

            if message_as_int > upper_threshold:
                self.http_request_handler.send_request(
                    'http://192.168.0.184/ena_f'
                )
            elif message_as_int < lower_threshold:
                self.http_request_handler.send_request(
                    'http://192.168.0.184/ena_r'
                )
        except ValueError:
            logger.error("Failed to convert message to integer")
