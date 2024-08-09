# src/services/table_manager.py
from mysql.connector import Error

class TableManager:
    def __init__(self, connection, logger):
        self.connection = connection
        self.logger = logger

    def create_database_and_table(self, database_name, table_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            cursor.execute(f"USE {database_name}")
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    vueltas INT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.connection.commit()
            self.logger.info(f"Database '{database_name}' and table '{table_name}' created/existing.")
        except Error as e:
            self.logger.error(f"Error creating database or table: {e}")
        finally:
            cursor.close()
