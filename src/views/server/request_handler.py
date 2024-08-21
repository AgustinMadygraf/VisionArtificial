"""
src/views/server/request_handler.py
Este módulo implementa un manejador de solicitudes HTTP con soporte SSL 
y manejo de rutas personalizadas.
"""
import http.server
import urllib.parse
from src.logs.config_logger import LoggerConfigurator
from src.views.server.route_registry import RouteRegistry
from src.views.handlers.local_ip_handler import LocalIPHandler
from src.views.handlers.route_handler import RouteHandler

logger = LoggerConfigurator().configure()


# Specific handlers for different routes
class RootHandler(RouteHandler):
    """
    Handler for the root route.
    """
    def handle(self, handler, query_params):
        """
        Handle the root route request.
        """
        camara = query_params.get('test', [None])[0]
        if camara:
            handler.path = '/static/photo.html'
        else:
            handler.path = '/static/camara.html'
        return super(handler.__class__, handler).do_GET()


route_registry = RouteRegistry()
# Register default routes
route_registry.register_route('/', RootHandler())
route_registry.register_route('/local-ip', LocalIPHandler())

# HTTP request handler class
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom HTTP request handler.
    """
    def do_GET(self):
        """
        Handle GET requests.
        """
        if not self.handle_custom_routes():
            logger.info("Handling GET request for %s", self.path)
            super().do_GET()

    def handle_custom_routes(self):
        """
        Handle custom routes.
        """
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        handler = route_registry.get_handler(parsed_path.path)
        if handler:
            handler.handle(self, query_params)
            return True
        return False
