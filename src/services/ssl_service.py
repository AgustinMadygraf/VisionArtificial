# src/services/ssl_service.py ```python
import os
import ssl
from src.interfaces.ssl_interface import SSLInterface

class SSLService(SSLInterface):
    def get_ssl_context(self):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')
        return ssl_context

    def is_certificate_valid(self, certfile='server.crt', keyfile='server.key'):
        # Verificar si los archivos existen
        if not os.path.exists(certfile) or not os.path.exists(keyfile):
            return False
        
        try:
            # Crear un contexto SSL y cargar el certificado y la clave
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        except ssl.SSLError:
            return False
        
        return True
# ```