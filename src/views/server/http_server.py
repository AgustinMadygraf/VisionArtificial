"""
src/views/server/http_server.py
Este módulo implementa un servidor HTTP con soporte SSL y manejo de rutas personalizado.
"""
import threading
import http.server
import ssl
from src.logs.config_logger import LoggerConfigurator
from src.utils.ssl_config import SSLConfig

logger = LoggerConfigurator().configure()

class HTTPServer:
    """
    HTTP server with SSL support.
    """
    def __init__(self, address, handler_class, ssl_config: SSLConfig):
        self.address = address
        self.handler_class = handler_class
        self.ssl_config = ssl_config
        self.logger = logger

    def start(self):
        """
        Start the server.
        """
        self.logger.debug("Initializing HTTP server with address: %s and handler: %s", self.address, self.handler_class)
        try:
            self.logger.debug("Creating HTTPServer instance")
            httpd = http.server.HTTPServer(self.address, self.handler_class)
            self.logger.debug("HTTPServer instance created successfully")

            self.logger.debug("Getting SSL context")
            ssl_context = self.ssl_config.get_ssl_context()
            self.logger.debug("SSL context obtained successfully")

            self.logger.debug("Wrapping socket with SSL context")
            httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
            self.logger.debug("Socket wrapped with SSL context successfully")

            self.logger.info("Servidor corriendo en https://%s:%s", self.address[0], self.address[1])
            self.logger.info("Modo Test en https://%s:%s?test=True", self.address[0], self.address[1])

            self.logger.debug("Starting HTTP server thread")
            http_thread = threading.Thread(target=httpd.serve_forever)
            http_thread.daemon = True
            http_thread.start()
            self.logger.debug("HTTP server thread started successfully")

        except OSError as e:
            self.logger.error("OSError occurred: %s", e)
            if e.errno == 10049:
                self.logger.error("Invalid address: %s", self.address)
            raise
        except ssl.SSLError as e:
            self.logger.error("SSLError occurred: %s", e)
            raise
        except Exception as e:
            self.logger.error("Unexpected error occurred: %s", e)
            raise
