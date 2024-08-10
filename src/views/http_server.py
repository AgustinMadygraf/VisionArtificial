# src/views/http_server.py
import http.server
import json
import threading
import urllib.parse
from utils.server_utility import ServerUtility
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

class RouteHandler:
    def handle(self, handler, query_params):
        raise NotImplementedError("Each route handler must implement the handle method.")

class RootHandler(RouteHandler):
    def handle(self, handler, query_params):
        handler.path = '/static/index.html'
        return super(handler.__class__, handler).do_GET()

class LocalIPHandler(RouteHandler):
    def handle(self, handler, query_params):
        local_ip = ServerUtility.get_local_ip()
        response = {'ip': local_ip}
        handler.send_response(200)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps(response).encode('utf-8'))

class TestHandler(RouteHandler):
    def handle(self, handler, query_params):
        test_value = query_params.get('test', [None])[0]
        response = {'test': test_value}
        handler.send_response(200)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps(response).encode('utf-8'))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.routes = {
            '/': RootHandler(),
            '/local-ip': LocalIPHandler(),
            '/test': TestHandler(),
        }
        super().__init__(*args, **kwargs)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        handler = self.routes.get(parsed_path.path)
        if handler:
            handler.handle(self, query_params)
        else:
            logger.info(f"Handling GET request for {self.path}")
            super().do_GET()

class HTTPServer:
    def __init__(self, address, handler_class, ssl_config):
        self.address = address
        self.handler_class = handler_class
        self.ssl_config = ssl_config
        self.logger = logger

    def start(self):
        httpd = http.server.HTTPServer(self.address, self.handler_class)
        httpd.socket = self.ssl_config.get_ssl_context().wrap_socket(httpd.socket, server_side=True)
        self.logger.info(f"Servidor corriendo en https://{self.address[0]}:{self.address[1]}")

        http_thread = threading.Thread(target=httpd.serve_forever)
        http_thread.daemon = True
        http_thread.start()
