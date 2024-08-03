# src/logs/ExcludeHTTPLogsFilter.py
import logging

class ExcludeHTTPLogsFilter(logging.Filter):
    def filter(self, record):
        # Excluir mensajes DEBUG y mensajes que contienen "GET / HTTP/1.1" y similares
        if record.levelno == logging.DEBUG:
            return False
        return 'GET /' not in record.getMessage() and 'POST /' not in record.getMessage()
