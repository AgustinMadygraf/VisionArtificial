"""
src/services/http_service.py
This module provides the HTTPService class which implements the HTTPInterface.
"""

import time
import requests
from src.interfaces.http_interface import HTTPInterface

class HTTPService(HTTPInterface):
    """
    HTTPService is responsible for making HTTP requests and handling retries.
    """

    def __init__(self, logger):
        self.logger = logger

    def fetch_data(self, url, retries=5, timeout=10):
        """
        Realiza una solicitud HTTP GET a la URL especificada y maneja las excepciones.
        """
        attempt = 0
        while attempt < retries:
            try:
                response = requests.get(url, timeout=timeout)
                response.raise_for_status()
                return response.text
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Attempt {attempt + 1} failed to fetch data from {url}: {e}")
                attempt += 1
                time.sleep(2 ** attempt)  # Exponential backoff before retrying
        self.logger.error(f"Failed to fetch data from {url} after {retries} attempts.")
        return None
