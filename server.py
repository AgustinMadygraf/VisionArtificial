#server.py
import http.server
import os
from ssl_config import SSLConfig

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    # Configuración del servidor
    server_address = ('localhost', 4443)  # Puedes cambiar el puerto si lo deseas
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)

    # Configuración SSL
    ssl_config = SSLConfig()
    httpd.socket = ssl_config.get_ssl_context().wrap_socket(httpd.socket, server_side=True)

    print(f"Servidor corriendo en https://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

if __name__ == '__main__':
    # Cambiar al directorio donde están los archivos web
    web_dir = '.'  # Cambia esto al directorio correcto
    os.chdir(web_dir)
    run_server()