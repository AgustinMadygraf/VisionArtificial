# src/services/http_service.py
import requests
import time
from src.interfaces.http_interface import HTTPInterface

class HTTPService(HTTPInterface):
    def __init__(self, logger):
        self.logger = logger

    def fetch_data(self, url, retries=5, timeout=10):
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
