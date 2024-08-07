# src/services/ssl_service.py
import ssl
from src.interfaces.ssl_interface import SSLInterface

class SSLService(SSLInterface):
    def get_ssl_context(self):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')
        return ssl_context
