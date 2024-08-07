# src/services/database_service.py

import mysql.connector
from mysql.connector import Error
from src.interfaces.db_interface import DatabaseInterface
from src.config.database_config import DATABASE_CONFIG

class MySQLDatabaseService(DatabaseInterface):
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def connect(self):
        return mysql.connector.connect(
            host=self.config['host'],
            user=self.config['user'],
            password=self.config['password'],
            database=self.config.get('database', DATABASE_CONFIG['database'])
        )

    def create_database_and_table(self, database_name, table_name):
        connection = None
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            cursor.execute(f"USE {database_name}")
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    vueltas INT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            connection.commit()
            self.logger.info(f"Database '{database_name}' and table '{table_name}' created/existing.")
        except Error as e:
            self.logger.error(f"Error creating database or table: {e}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def store_vueltas(self, vueltas, database_name, table_name):
        config_with_db = self.config.copy()
        config_with_db['database'] = database_name
        connection = None
        try:
            connection = mysql.connector.connect(**config_with_db)
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(f"INSERT INTO {table_name} (vueltas) VALUES (%s)", (vueltas,))
                connection.commit()
                self.logger.info("Value successfully inserted into the database.")
        except Error as e:
            self.logger.error(f"Error connecting to the database: {e}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
