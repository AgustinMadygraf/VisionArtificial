# Base interface for handlers
class RouteHandler:
    """
    Base class for route handlers.
    """
    # pylint: disable=unused-argument
    def handle(self, handler, query_params):
        """
        Handle the request.
        """
        raise NotImplementedError("Each route handler must implement the handle method.")