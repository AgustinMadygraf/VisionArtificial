# src/views/http_server.py
import http.server
import json
import threading
import urllib.parse
from utils.server_utility import ServerUtility
from logs.config_logger import logger_configurator

logger = logger_configurator.get_logger()

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.path = '/static/index.html'
        elif parsed_path.path == '/local-ip':
            self.handle_local_ip()
            return
        elif 'test' in query_params:
            self.handle_test(query_params['test'][0])
            return

        logger.info(f"Handling GET request for {self.path}")
        return super().do_GET()

    def handle_local_ip(self):
        local_ip = ServerUtility.get_local_ip()
        response = {'ip': local_ip}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def handle_test(self, test_value):
        response = {'test': test_value}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

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
