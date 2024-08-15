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
        
        self.logger.debug(f"Verificando la validez del certificado en '{certfile}' y la clave en '{keyfile}'.")
        
        if not self.is_certificate_valid(certfile, keyfile):
            self.logger.debug(f"El certificado o la clave no son válidos. Generando CSR en '{csrfile}'.")
            # Generar CSR y enviar a la CA para obtener un certificado firmado
            self.generate_csr(keyfile, csrfile)
        try:
            # Crear el contexto SSL y cargar el certificado y la clave
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            self.logger.debug("Contexto SSL creado y certificado/cadena de claves cargados correctamente.")
            return ssl_context
        except ssl.SSLError as e:
            self.logger.error(f"Error al cargar el certificado o la clave: {e}")
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
            self.logger.debug(f"Archivo de certificado '{certfile}' o clave '{keyfile}' no encontrado.")
            return False
        
        try:
            # Crear un contexto SSL y cargar el certificado y la clave
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            self.logger.debug("Certificado y clave verificados como válidos.")
            return True
        except ssl.SSLError as e:
            self.logger.error(f"Error al verificar el certificado y la clave: {e}")
            return False

    def generate_csr(self, keyfile, csrfile):
        """
        Generate a Certificate Signing Request (CSR) and self-signed certificate if needed.
        
        Args:
            keyfile (str): Path to the key file.
            csrfile (str): Path to the CSR file.
        """
        if not os.path.exists(keyfile):
            self.logger.error(f"Archivo de clave '{keyfile}' no encontrado. No se puede generar el CSR.")
            self.logger.debug("Intentando generar una nueva clave privada sin passphrase.")
            try:
                subprocess.run(['openssl', 'genpkey', '-algorithm', 'RSA', '-out', keyfile], check=True)
                self.logger.debug(f"Clave privada generada y guardada en '{keyfile}'.")
            except subprocess.CalledProcessError as e:
                self.logger.error(f"Error al generar la clave privada: {e}")
                raise FileNotFoundError(f"No se pudo generar el archivo de clave '{keyfile}'.")

        try:
            self.logger.debug(f"Generando CSR con el archivo de clave '{keyfile}' y guardándolo en '{csrfile}'.")
            subprocess.run([
                'openssl', 'req', '-new', '-key', keyfile, '-out', csrfile,
                '-config', 'openssl.cnf', '-batch'
            ], check=True)
            self.logger.debug("CSR generado con éxito.")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error al generar el CSR: {e}")
            self.logger.debug(f"Comando que falló: openssl req -new -key {keyfile} -out {csrfile} -config openssl.cnf")
            self.logger.debug("Verifique que los archivos 'server.key' y 'openssl.cnf' existan y estén correctamente configurados.")
            raise e

        # Verificar si el certificado existe, si no, generar uno autofirmado
        certfile = 'server.crt'
        if not os.path.exists(certfile):
            self.logger.debug(f"Certificado '{certfile}' no encontrado. Intentando generar un certificado autofirmado.")
            try:
                subprocess.run([
                    'openssl', 'req', '-x509', '-key', keyfile, '-out', certfile,
                    '-days', '365', '-config', 'openssl.cnf', '-batch'
                ], check=True)
                self.logger.debug(f"Certificado autofirmado generado y guardado en '{certfile}'.")
            except subprocess.CalledProcessError as e:
                self.logger.error(f"Error al generar el certificado autofirmado: {e}")
                raise FileNotFoundError(f"No se pudo generar el certificado '{certfile}'.")
