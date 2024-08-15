"""
src/views/http_server.py
This module implements an HTTP server with SSL support and custom route handling.
"""

import http.server
import json
import threading
import urllib.parse
import ssl
from src.logs.config_logger import LoggerConfigurator
from src.views.handlers.route_handler import RouteHandler
from src.utils.ssl_config import SSLConfig
from src.views.handlers.local_ip_handler import LocalIPHandler

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
            handler.path = '/static/test.html'        
        else:
            handler.path = '/static/index.html'
        return super(handler.__class__, handler).do_GET()

# Registry for managing route handlers
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

route_registry = RouteRegistry()

# Register default routes
route_registry.register_route('/', RootHandler())
route_registry.register_route('/local-ip', LocalIPHandler())

# Concrete SSL configuration implementation
class DefaultSSLConfig(SSLConfig):
    """
    Default SSL configuration implementation.
    """
    def __init__(self, certfile, keyfile):
        super().__init__(certfile, keyfile)
        self.certfile = certfile
        self.keyfile = keyfile

    def get_ssl_context(self):
        """
        Get the SSL context.
        """
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
        return context

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

class HTTPServer:
    """
    HTTP server with SSL support.
    """
    def __init__(self, address, handler_class, ssl_config: SSLConfig):
        self.address = address
        self.handler_class = handler_class
        self.ssl_config = ssl_config
        self.logger = logger

    def start(self):
        """
        Start the server.
        """
        httpd = http.server.HTTPServer(self.address, self.handler_class)
        ssl_context = self.ssl_config.get_ssl_context()
        httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
        self.logger.info("Servidor corriendo en https://%s:%s", self.address[0], self.address[1])

        http_thread = threading.Thread(target=httpd.serve_forever)
        http_thread.daemon = True
        http_thread.start()
