# src/services/data_storer.py

from src.services.table_manager import TableManager
from src.services.data_inserter import DataInserter
from src.services.database_connection import DatabaseConnection

class DataStorer:
    def __init__(self, db_config, logger):
        self.connection = DatabaseConnection(db_config, logger).connect()
        self.logger = logger

    def store_vueltas(self, vueltas, database_name, table_name):
        table_manager = TableManager(self.connection, self.logger)
        table_manager.create_database_and_table(database_name, table_name)

        data_inserter = DataInserter(self.connection, self.logger)
        data_inserter.store_vueltas(vueltas, database_name, table_name)
