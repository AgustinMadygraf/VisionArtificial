"""
src/interfaces/http_interface.py
This module defines an interface for HTTP operations, enforcing the implementation
of methods required for data fetching and sending HTTP requests.
"""

from abc import ABC, abstractmethod

class HTTPInterface(ABC):
    """
    Abstract base class that defines the interface for HTTP operations.
    """
    @abstractmethod
    def fetch_data(self, url, retries=5, timeout=10):
        """
        Abstract method to fetch data from a given URL.

        Args:
            url (str): The URL to fetch data from.
            retries (int, optional): Number of retry attempts. Defaults to 5.
            timeout (int, optional): Timeout duration in seconds. Defaults to 10.
        
        Returns:
            Any: The data retrieved from the URL.
        """
        pass

    def send_request(self, url):
        """
        Method to send a request to a given URL.

        Args:
            url (str): The URL to send the request to.
        
        Returns:
            Any: The response from the request.
        """
        pass
