import asyncio
import subprocess
import requests
from websockets import serve
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK
from src.config.network_config import NETWORK_CONFIG
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

def get_pid_using_port(port):
    try:
        result = subprocess.check_output(f"netstat -ano | findstr :{port}", shell=True).decode()
        if result:
            lines = result.strip().split("\n")
            for line in lines:
                if f":{port}" in line:
                    return int(line.strip().split()[-1])
    except subprocess.CalledProcessError as e:
        return None
    return None

def kill_process(pid):
    try:
        subprocess.check_output(f"taskkill /PID {pid} /F", shell=True)
        logger.info(f"Successfully terminated process with PID {pid}.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to terminate process with PID {pid}. Error: {e}")

class WebSocketServer:
    """
    Clase responsable de iniciar y manejar un servidor WebSocket.

    Principios SOLID aplicados:
    - Responsabilidad Única (SRP): Esta clase tiene la única responsabilidad de gestionar el servidor WebSocket.
    - Inversión de Dependencias (DIP): Depende de una abstracción para el servicio SSL y el manejador de mensajes.
    """
    def __init__(self, ssl_service, handler):
        """
        Inicializa el servidor WebSocket.

        Args:
            ssl_service: Servicio SSL para manejar la configuración SSL.
            handler: Manejador de mensajes para procesar los mensajes recibidos.
        """
        self.address = (NETWORK_CONFIG['websocket_host'], NETWORK_CONFIG['websocket_port'])
        self.ssl_service = ssl_service
        self.handler = handler

    async def start(self):
        """
        Inicia el servidor WebSocket y lo configura para ejecutarse indefinidamente.
        """
        ssl_context = self.ssl_service.get_ssl_context()
        port = self.address[1]
        pid = get_pid_using_port(port)
        if pid:
            logger.info(f"Port {port} is being used by PID {pid}. Terminating the process...")
            kill_process(pid)
            await asyncio.sleep(2)  # Wait for a moment to ensure the port is released

        try:
            async with serve(self.handler.handle, self.address[0], self.address[1], ssl=ssl_context, ping_interval=None):
                logger.info(f"WebSocket server started at wss://{self.address[0]}:{self.address[1]}")
                await asyncio.Future()  # Ejecutar indefinidamente
        except Exception as e:
            logger.error(f"Failed to start WebSocket server: {e}")

class WebSocketHandler:
    """
    Clase responsable de manejar las conexiones y mensajes WebSocket.

    Principios SOLID aplicados:
    - Responsabilidad Única (SRP): Maneja las conexiones y mensajes WebSocket.
    """
    def __init__(self, message_handler):
        """
        Inicializa el manejador WebSocket.

        Args:
            message_handler: Manejador de mensajes para procesar los mensajes recibidos.
        """
        self.message_handler = message_handler

    async def handle(self, websocket, path):
        """
        Maneja las conexiones WebSocket y procesa los mensajes recibidos.

        Args:
            websocket: Conexión WebSocket.
            path: Ruta del WebSocket.
        """
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

class HTTPHandler:
    """
    Clase responsable de enviar solicitudes HTTP y manejar intentos fallidos.

    Principios SOLID aplicados:
    - Responsabilidad Única (SRP): Maneja el envío de solicitudes HTTP.
    """
    def __init__(self, http_service, max_attempts=5):
        """
        Inicializa el manejador de solicitudes HTTP.

        Args:
            http_service: Servicio HTTP para enviar las solicitudes.
            max_attempts: Número máximo de intentos en caso de fallo.
        """
        self.http_service = http_service
        self.failed_attempts = 0
        self.max_attempts = max_attempts

    def send_request(self, url):
        """
        Envía una solicitud HTTP a la URL especificada y maneja los intentos fallidos.

        Args:
            url (str): URL a la que se enviará la solicitud.
        """
        if self.failed_attempts >= self.max_attempts:
            logger.warning(f"Maximum failed attempts reached. Stopping requests to {url}.")
            return

        try:
            self.http_service.send_request(url)
            self.failed_attempts = 0  # Reinicia el contador en caso de éxito
        except requests.exceptions.RequestException as e:
            self.failed_attempts += 1
            logger.error(f"Failed to connect to {url}: {str(e).split(':')[0]} (Attempt {self.failed_attempts})")

class MessageHandler:
    """
    Clase responsable de procesar los mensajes recibidos a través de WebSocket.

    Principios SOLID aplicados:
    - Responsabilidad Única (SRP): Procesa los mensajes recibidos.
    """
    def __init__(self, http_request_handler, tolerance=10):
        """
        Inicializa el manejador de mensajes.

        Args:
            http_request_handler: Manejador de solicitudes HTTP para enviar solicitudes basadas en los mensajes.
            tolerance: Umbral de tolerancia para determinar la acción a tomar.
        """
        self.http_request_handler = http_request_handler
        self.tolerance = tolerance

    async def process_message(self, message):
        """
        Procesa un mensaje recibido y envía una solicitud HTTP basada en el contenido del mensaje.

        Args:
            message (str): Mensaje recibido.
        """
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
