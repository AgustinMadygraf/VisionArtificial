from mysql.connector import Error

class DataInserter:
    def __init__(self, connection, logger):
        self.connection = connection
        self.logger = logger

    def store_vueltas(self, vueltas, database_name, table_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO {table_name} (vueltas) VALUES (%s)", (vueltas,))
            self.connection.commit()
            self.logger.info("Value successfully inserted into the database.")
        except Error as e:
            self.logger.error(f"Error inserting data into the table: {e}")
        finally:
            cursor.close()
