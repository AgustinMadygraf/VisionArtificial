# src/interfaces/http_interface.py
from abc import ABC, abstractmethod

class HTTPInterface(ABC):
    @abstractmethod
    def fetch_data(self, url, retries=5, timeout=10):
        pass

    def send_request(self, url):
        pass
