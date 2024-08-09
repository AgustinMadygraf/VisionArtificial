import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config.get('database')
            )
            self.logger.info("Database connection established.")
            return connection
        except Error as e:
            self.logger.error(f"Error connecting to the database: {e}")
            return None
        
