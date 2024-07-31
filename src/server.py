import http.server
import os
import socket
import asyncio
import websockets
from ssl_config import SSLConfig
from logs.config_logger import logger_configurator
import json

# Obtener el logger configurado
logger = logger_configurator.get_logger()

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/local-ip':
            self.handle_local_ip()
            return
        logger.info(f"Handling GET request for {self.path}")
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def handle_local_ip(self):
        local_ip = get_local_ip()
        response = {'ip': local_ip}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

def get_local_ip():
    """Obtiene la dirección IP local de la máquina."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Esto no necesita conectarse realmente a un host, solo inicializar la conexión
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception as e:
        ip = '127.0.0.1'
        logger.error(f"Error obtaining local IP: {e}")
    finally:
        s.close()
    logger.info(f"Local IP obtained: {ip}")
    return ip

async def websocket_handler(websocket, path):
    async for message in websocket:
        logger.info(f"Received console.log message: {message}")

def run_server():
    # Obtener la dirección IP local
    local_ip = get_local_ip()
    
    # Configuración del servidor HTTP
    server_address = (local_ip, 4443)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)

    # Configuración SSL
    ssl_config = SSLConfig()
    httpd.socket = ssl_config.get_ssl_context().wrap_socket(httpd.socket, server_side=True)

    logger.info(f"Servidor corriendo en https://{server_address[0]}:{server_address[1]}/?t=500")

    # Iniciar el servidor HTTP en un hilo separado
    import threading
    http_thread = threading.Thread(target=httpd.serve_forever)
    http_thread.daemon = True
    http_thread.start()

    # Iniciar el servidor WebSocket
    start_websocket_server(local_ip, ssl_config)

def start_websocket_server(local_ip, ssl_config):
    async def main():
        ssl_context = ssl_config.get_ssl_context()
        async with websockets.serve(websocket_handler, local_ip, 8765, ssl=ssl_context):
            await asyncio.Future()  # Run forever

    asyncio.run(main())

if __name__ == '__main__':
    # Cambiar al directorio donde están los archivos web
    web_dir = '.'  # Cambia esto al directorio correcto
    os.chdir(web_dir)
    run_server()