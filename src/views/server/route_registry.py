"""
src/views/server/route_registry.py
Este módulo implementa un registro de rutas para manejar las rutas de los controladores.
"""

class RouteRegistry:
    """
    Registry for managing route handlers.
    """
    def __init__(self):
        self.routes = {}

    def register_route(self, path, handler):
        """
        Register a route with a handler.
        """
        self.routes[path] = handler

    def get_handler(self, path):
        """
        Get the handler for a given route.
        """
        return self.routes.get(path, None)
