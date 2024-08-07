# src/interfaces/db_interface.py
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def create_database_and_table(self, database_name, table_name):
        pass

    @abstractmethod
    def store_vueltas(self, vueltas, database_name, table_name):
        pass
