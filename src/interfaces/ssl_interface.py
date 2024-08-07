# src/interfaces/ssl_interface.py
from abc import ABC, abstractmethod

class SSLInterface(ABC):
    @abstractmethod
    def get_ssl_context(self):
        pass
