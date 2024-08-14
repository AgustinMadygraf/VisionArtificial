"""
src/utils/ssl_config.py
This module provides SSL configuration utilities for setting up secure connections.
"""

import ssl

class SSLConfig:
    """
    Class responsible for configuring SSL context for secure connections.
    """
    def __init__(self, certfile='server.crt', keyfile='server.key'):
        """
        Initialize the SSLConfig with the paths to the certificate and key files.

        Args:
            certfile (str): Path to the SSL certificate file.
            keyfile (str): Path to the SSL key file.
        """
        self.certfile = certfile
        self.keyfile = keyfile

    def get_ssl_context(self):
        """
        Create and configure an SSL context for a TLS server.

        Returns:
            ssl.SSLContext: Configured SSL context.
        """
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
        return ssl_context
