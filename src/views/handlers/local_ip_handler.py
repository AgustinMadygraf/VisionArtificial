"""
src/views/handlers/local_ip_handler.py
Este archivo se ocupa de manejar las solicitudes de la ruta de IP local.
"""
import json
from src.views.handlers.route_handler import RouteHandler
from src.utils.server_utility import ServerUtility

class LocalIPHandler(RouteHandler):
    """
    Handler for the local IP route.
    """
    def handle(self, handler, query_params):
        """
        Handle the local IP route request.
        """
        local_ip = ServerUtility.get_local_ip()
        response = {'ip': local_ip}
        handler.send_response(200)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps(response).encode('utf-8'))
