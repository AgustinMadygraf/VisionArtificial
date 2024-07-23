import http.server
import ssl
import os
import subprocess


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


def generate_self_signed_cert(cert_file, key_file):
    """Genera un certificado autofirmado y una clave privada."""
    subprocess.run([
        'openssl', 'req', '-x509', '-newkey', 'rsa:4096',
        '-keyout', key_file, '-out', cert_file,
        '-days', '365', '-nodes',
        '-subj', '/CN=localhost'
    ], check=True)
    print(f"Certificado autofirmado generado: {cert_file}")
    print(f"Clave privada generada: {key_file}")


def ensure_ssl_files(cert_file, key_file):
    """Asegura que los archivos SSL existan, generándolos si es necesario."""
    if not (os.path.exists(cert_file) and os.path.exists(key_file)):
        print("Archivos SSL no encontrados. Generando nuevos...")
        generate_self_signed_cert(cert_file, key_file)
    else:
        print("Archivos SSL encontrados.")


def run_server():
    # Configuración del servidor
    server_address = ('localhost', 4443)  # Puedes cambiar el puerto si lo deseas
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)

    # Asegurar que los archivos SSL existan
    cert_file = 'server.crt'
    key_file = 'server.key'
    ensure_ssl_files(cert_file, key_file)

    # Configuración SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(cert_file, key_file)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print(f"Servidor corriendo en https://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()


if __name__ == '__main__':
    # Cambiar al directorio donde están los archivos web
    web_dir = '.'  # Cambia esto al directorio correcto
    os.chdir(web_dir)
    run_server()