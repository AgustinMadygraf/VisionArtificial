"""
src/interfaces/ssl_interface.py
This module defines an interface for SSL configuration, enforcing the implementation
of methods required to create and manage SSL contexts.
"""

from abc import ABC, abstractmethod

class SSLInterface(ABC):
    """
    Abstract base class that defines the interface for SSL configuration.
    """
    @abstractmethod
    def get_ssl_context(self):
        """
        Get the SSL context, regenerating the certificate if necessary.
        
        Returns:
            ssl.SSLContext: The SSL context with the loaded certificate and key.
        """
        print ("get_ssl_context")

    @abstractmethod
    def is_certificate_valid(self, certfile, keyfile):
        """
        Check if the certificate and key are valid.
        
        Args:
            certfile (str): Path to the certificate file.
            keyfile (str): Path to the key file.
        
        Returns:
            bool: True if the certificate and key are valid, False otherwise.
        """
        print ("is_certificate_valid")

    @abstractmethod
    def generate_csr(self, keyfile, csrfile):
        """
        Generate a Certificate Signing Request (CSR).
        
        Args:
            keyfile (str): Path to the key file.
            csrfile (str): Path to the CSR file.
        """
        print ("generate_csr")
