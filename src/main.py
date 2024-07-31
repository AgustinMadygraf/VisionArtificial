import os
from server.http_server import HTTPServer
from server.websocket_server import WebSocketServer
from config.ssl_config import SSLConfig
from server.server_utility import ServerUtility
from server.http_server import MyHTTPRequestHandler

def run_server():
    local_ip = ServerUtility.get_local_ip()
    ssl_config = SSLConfig()

    http_server = HTTPServer((local_ip, 4443), MyHTTPRequestHandler, ssl_config)
    http_server.start()

    websocket_server = WebSocketServer((local_ip, 8765), ssl_config)
    websocket_server.start()

if __name__ == '__main__':
    web_dir = '.'
    os.chdir(web_dir)
    run_server()
