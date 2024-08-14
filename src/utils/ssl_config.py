"""
src/utils/ssl_config.py
This module provides SSL configuration utilities for setting up secure connections.
"""

import ssl
import subprocess
class SSLConfig:
    """
    Class responsible for configuring SSL context for secure connections.
    """
    def __init__(self, certfile='server.crt', keyfile='server.key',
                 csrfile='server.csr', configfile='openssl.cnf'):
        self.certfile = certfile
        self.keyfile = keyfile
        self.csrfile = csrfile
        self.configfile = configfile

    def get_ssl_context(self):
        """
        Get the SSL context, regenerating the certificate if necessary.
        
        Returns:
            ssl.SSLContext: The SSL context with the loaded certificate and key.
        """
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
        return context

    def generate_csr(self):
        """
        Generate a Certificate Signing Request (CSR).
        """
        subprocess.run([
            'openssl', 'req', '-new', '-key', self.keyfile, '-out', self.csrfile,
            '-config', self.configfile
        ], check=True)
        print('CSR generado con éxito.')

    def generate_self_signed_cert(self):
        """
        Generate a self-signed certificate.
        """
        subprocess.run([
            'openssl', 'req', '-new', '-x509', '-key', self.keyfile, '-out',
            self.certfile, '-days', '365', '-config', self.configfile
        ], check=True)
        print('Certificado autofirmado generado con éxito.')

    def is_certificate_valid(self):
        """
        Check if the certificate and key are valid.
        
        Returns:
            bool: True if the certificate and key are valid, False otherwise.
        """
        try:
            ssl_context = self.get_ssl_context()
            ssl_context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
            return True
        except ssl.SSLError as e:
            print(f'Error al validar el certificado: {e}')
            return False
