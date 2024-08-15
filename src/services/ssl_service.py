"""
src/services/ssl_service.py
Servicio para gestionar el contexto SSL y los certificados.
"""
import os
import ssl
import subprocess
from src.interfaces.ssl_interface import SSLInterface
from src.logs.config_logger import LoggerConfigurator

class SSLService(SSLInterface):
    """
    Service for managing SSL context and certificates.
    """
    def __init__(self):
        self.logger = LoggerConfigurator().configure()

    def get_ssl_context(self):
        """
        Get the SSL context, regenerating the certificate if necessary.
        
        Returns:
            ssl.SSLContext: The SSL context with the loaded certificate and key.
        """
        certfile = 'server.crt'
        keyfile = 'server.key'
        csrfile = 'server.csr'
        self.logger.debug("Verificando la validez del certificado en '%s' y la clave en '%s'.",
                          certfile, keyfile)
        if not self.is_certificate_valid(certfile, keyfile):
            self.logger.debug("""El certificado o la clave no son válidos.
                            Generando CSR en '%s'.", csrfile""")
            # Generar CSR y enviar a la CA para obtener un certificado firmado
            self.generate_csr(keyfile, csrfile)
        try:
            # Crear el contexto SSL y cargar el certificado y la clave
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            self.logger.debug("""Contexto SSL creado y certificado/cadena
                              de claves cargados correctamente.""")
            return ssl_context
        except ssl.SSLError as e:
            self.logger.error("Error al cargar el certificado o la clave: %s", e)
            raise e

    def is_certificate_valid(self, certfile='server.crt', keyfile='server.key'):
        """
        Check if the certificate and key are valid.
        
        Args:
            certfile (str): Path to the certificate file.
            keyfile (str): Path to the key file.
        
        Returns:
            bool: True if the certificate and key are valid, False otherwise.
        """
        # Verificar si los archivos existen
        if not os.path.exists(certfile) or not os.path.exists(keyfile):
            self.logger.debug("""Archivo de certificado '%s' o clave '%s'
                              no encontrado.""", certfile, keyfile)
            return False
        try:
            # Crear un contexto SSL y cargar el certificado y la clave
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            self.logger.debug("Certificado y clave verificados como válidos.")
            return True
        except ssl.SSLError as e:
            self.logger.error("Error al verificar el certificado y la clave: %s", e)
            return False

    def generate_csr(self, keyfile, csrfile):
        """
        Generate a Certificate Signing Request (CSR) and self-signed certificate if needed.
        
        Args:
            keyfile (str): Path to the key file.
            csrfile (str): Path to the CSR file.
        """
        if not os.path.exists(keyfile):
            self.logger.error("""Archivo de clave '%s' no encontrado.
                              No se puede generar el CSR.""", keyfile)
            self.logger.debug("Intentando generar una nueva clave privada sin passphrase.")
            try:
                subprocess.run(['openssl', 'genpkey', '-algorithm', 'RSA', '-out',
                                keyfile], check=True)
                self.logger.debug("Clave privada generada y guardada en '%s'.", keyfile)
            except subprocess.CalledProcessError as e:
                self.logger.error("Error al generar la clave privada: %s", e)
                raise FileNotFoundError(f"""No se pudo generar el archivo de
                                        clave '{keyfile}'.""") from e

        try:
            self.logger.debug("""Generando CSR con el archivo de clave '%s' y
                              guardándolo en '%s'.""", keyfile, csrfile)
            subprocess.run([
                'openssl', 'req', '-new', '-key', keyfile, '-out', csrfile,
                '-config', 'openssl.cnf', '-batch'
            ], check=True)
            self.logger.debug("CSR generado con éxito.")
        except subprocess.CalledProcessError as e:
            self.logger.error("Error al generar el CSR: %s", e)
            self.logger.debug("""Comando que falló: openssl req -new -key %s -out %s
                              -config openssl.cnf""", keyfile, csrfile)
            self.logger.debug("""Verifique que los archivos 'server.key' y 'openssl.cnf'
                              existan y estén correctamente configurados.""")
            raise e

        # Verificar si el certificado existe, si no, generar uno autofirmado
        certfile = 'server.crt'
        if not os.path.exists(certfile):
            self.logger.debug("""Certificado '%s' no encontrado. Intentando generar un
                              certificado autofirmado.""", certfile)
            try:
                subprocess.run([
                    'openssl', 'req', '-x509', '-key', keyfile, '-out', certfile,
                    '-days', '365', '-config', 'openssl.cnf', '-batch'
                ], check=True)
                self.logger.debug("Certificado autofirmado generado y guardado en '%s'.", certfile)
            except subprocess.CalledProcessError as e:
                self.logger.error("Error al generar el certificado autofirmado: %s", e)
                raise FileNotFoundError(f"No se pudo generar el certificado '{certfile}'.") from e
