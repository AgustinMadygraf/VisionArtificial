"""
src/services/ssl_service.py
This module provides services for managing SSL context and certificates.
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
        
        # Verificar si el certificado es válido
        if not self.is_certificate_valid(certfile, keyfile):
            # Regenerar el certificado usando OpenSSLCertificateProvider
            provider = OpenSSLCertificateProvider()
            provider.generate_certificate(certfile, keyfile)
        
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

class OpenSSLCertificateProvider:
    """
    Provider for generating SSL certificates using OpenSSL.
    """
    def generate_certificate(self, certfile, keyfile):
        """
        Generate a new SSL certificate and key using OpenSSL.
        
        Args:
            certfile (str): Path to the certificate file.
            keyfile (str): Path to the key file.
        """
        # Comandos para generar el certificado y la clave usando OpenSSL
        subprocess.run([
            'openssl', 'req', '-x509', '-newkey', 'rsa:4096', '-keyout', keyfile,
            '-out', certfile, '-days', '365', '-nodes', '-subj', '/CN=localhost'
        ], check=True)
