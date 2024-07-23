import http.server
import os
import socket
from ssl_config import SSLConfig
from logs.config_logger import logger_configurator

# Obtener el logger configurado
logger = logger_configurator.get_logger()

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        logger.info(f"Handling GET request for {self.path}")
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

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

def run_server():
    # Obtener la dirección IP local
    local_ip = get_local_ip()
    
    # Configuración del servidor
    server_address = (local_ip, 4443)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)

    # Configuración SSL
    ssl_config = SSLConfig()
    httpd.socket = ssl_config.get_ssl_context().wrap_socket(httpd.socket, server_side=True)

    logger.info(f"Servidor corriendo en https://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

if __name__ == '__main__':
    # Cambiar al directorio donde están los archivos web
    web_dir = '.'  # Cambia esto al directorio correcto
    os.chdir(web_dir)
    run_server()
