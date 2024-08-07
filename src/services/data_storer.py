# src/services/data_storer.py

from src.services.database_service import MySQLDatabaseService
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()

class DataStorer:
    def __init__(self, db_service):
        self.db_service = db_service

    def store_vueltas(self, vueltas, database_name, table_name):
        self.db_service.create_database_and_table(database_name, table_name)
        self.db_service.store_vueltas(vueltas, database_name, table_name)
