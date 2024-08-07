# src/interfaces/canvas_utils_interface.py
from abc import ABC, abstractmethod

class CanvasUtilsInterface(ABC):
    @abstractmethod
    def draw_vertical_line(self, context, pos, color='yellow'):
        pass

    @abstractmethod
    def draw_horizontal_line(self, context, pos, color='green'):
        pass

    @abstractmethod
    def draw_center_ruler(self, context, color='blue', line_length=10, spacing=10):
        pass
