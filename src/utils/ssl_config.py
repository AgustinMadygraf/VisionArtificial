"""
src/utils/ssl_config.py
This module provides SSL configuration utilities for setting up secure connections.
"""

import ssl

class SSLConfig:
    """
    Class responsible for configuring SSL context for secure connections.
    """
    def get_ssl_context(self):
        """
        Create and configure an SSL context for a TLS server.

        Returns:
            ssl.SSLContext: Configured SSL context.
        """
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')
        return ssl_context
