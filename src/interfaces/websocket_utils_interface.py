# src/interfaces/websocket_utils_interface.py
from abc import ABC, abstractmethod

class WebSocketUtilsInterface(ABC):
    @abstractmethod
    def initialize_websocket(self):
        pass

    @abstractmethod
    def send_websocket_message(self, message: str):
        pass
