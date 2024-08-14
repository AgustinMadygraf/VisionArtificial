"""
Servicio para gestionar el contexto SSL y los certificados.
"""
import os
import ssl
import subprocess
from src.interfaces.ssl_interface import SSLInterface

class SSLService(SSLInterface):
    """
    Service for managing SSL context and certificates.
    """
    def get_ssl_context(self):
        """
        Get the SSL context, regenerating the certificate if necessary.
        
        Returns:
            ssl.SSLContext: The SSL context with the loaded certificate and key.
        """
        certfile = 'server.crt'
        keyfile = 'server.key'
        csrfile = 'server.csr'
        if not self.is_certificate_valid(certfile, keyfile):
            # Generar CSR y enviar a la CA para obtener un certificado firmado
            self.generate_csr(keyfile, csrfile)
        # Crear el contexto SSL y cargar el certificado y la clave
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        return ssl_context

    def is_certificate_valid(self, certfile='server.crt', keyfile='server.key'):
        """
        Check if the certificate and key are valid.
        
        Args:
            certfile (str): Path to the certificate file.
            keyfile (str): Path to the key file.
        
        Returns:
            bool: True if the certificate and key are valid, False otherwise.
        """
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

    def generate_csr(self, keyfile, csrfile):
        """
        Generate a Certificate Signing Request (CSR).
        
        Args:
            keyfile (str): Path to the key file.
            csrfile (str): Path to the CSR file.
        """
        subprocess.run([
            'openssl', 'req', '-new', '-key', keyfile, '-out', csrfile,
            '-config', 'openssl.cnf'
        ],check=True)
        print('CSR generado con éxito.')
