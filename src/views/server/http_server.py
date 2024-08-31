"""
src/views/server/http_server.py
Este módulo implementa un servidor HTTP con soporte SSL y manejo de rutas personalizado.
"""
import threading
import http.server
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
        try:
            self.logger.debug("Starting HTTP server with address: %s and handler: %s", self.address,
                              self.handler_class)
            httpd = http.server.HTTPServer(self.address, self.handler_class)
            ssl_context = self.ssl_config.get_ssl_context()
            httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
            self.logger.info("Servidor corriendo en https://%s:%s", self.address[0],
                             self.address[1])
            self.logger.info("Modo Test en https://%s:%s?test=True", self.address[0],
                             self.address[1])
            http_thread = threading.Thread(target=httpd.serve_forever)
            http_thread.daemon = True
            http_thread.start()
        except OSError as e:
            self.logger.error("OSError occurred: %s", e)
            raise
        except Exception as e:
            self.logger.error("Unexpected error occurred: %s", e)
            raise
