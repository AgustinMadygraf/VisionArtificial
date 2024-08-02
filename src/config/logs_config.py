import logging

class LoggerConfigurator:
    @staticmethod
    def get_logger():
        logger = logging.getLogger('server')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
        return logger

logger_configurator = LoggerConfigurator()
