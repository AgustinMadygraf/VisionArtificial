#src/request_handler.py
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

url = 'http://192.168.0.184/ena_r'
session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))

try:
    response = session.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")