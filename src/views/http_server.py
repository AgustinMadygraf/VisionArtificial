"""
src/views/http_server.py
This module implements an HTTP server with SSL support and custom route handling.
"""

import http.server
import threading
import ssl
from src.logs.config_logger import LoggerConfigurator
from src.utils.ssl_config import SSLConfig



logger = LoggerConfigurator().configure()

# Concrete SSL configuration implementation
class DefaultSSLConfig(SSLConfig):
    """
    Default SSL configuration implementation.
    """
    def __init__(self, certfile, keyfile):
        super().__init__(certfile, keyfile)
        self.certfile = certfile
        self.keyfile = keyfile

    def get_ssl_context(self):
        """
        Get the SSL context.
        """
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
        return context
