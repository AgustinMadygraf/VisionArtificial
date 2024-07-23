#ssl_config.py
import subprocess
import os
import ssl

class SSLConfig:
    def __init__(self, cert_file='server.crt', key_file='server.key'):
        self.cert_file = cert_file
        self.key_file = key_file

    def generate_self_signed_cert(self):
        """Genera un certificado autofirmado y una clave privada."""
        subprocess.run([
            'openssl', 'req', '-x509', '-newkey', 'rsa:4096',
            '-keyout', self.key_file, '-out', self.cert_file,
            '-days', '365', '-nodes',
            '-subj', '/CN=localhost'
        ], check=True)
        print(f"Certificado autofirmado generado: {self.cert_file}")
        print(f"Clave privada generada: {self.key_file}")

    def ensure_ssl_files(self):
        """Asegura que los archivos SSL existan, generándolos si es necesario."""
        if not (os.path.exists(self.cert_file) and os.path.exists(self.key_file)):
            print("Archivos SSL no encontrados. Generando nuevos...")
            self.generate_self_signed_cert()
        else:
            print("Archivos SSL encontrados.")

    def get_ssl_context(self):
        """Devuelve el contexto SSL configurado."""
        self.ensure_ssl_files()
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(self.cert_file, self.key_file)
        return context
