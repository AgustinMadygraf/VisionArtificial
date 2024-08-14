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
        Abstract method to be implemented by subclasses to provide an SSL context.

        Returns:
            ssl.SSLContext: An SSL context for secure connections.
        """
        print ("get_ssl_context")
