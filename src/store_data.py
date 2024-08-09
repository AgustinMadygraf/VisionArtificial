# src/store_data.py

import sys
import os
from dotenv import load_dotenv
from src.logs.config_logger import LoggerConfigurator
from src.services.data_extractor import DataExtractor
from src.services.data_processor import DataProcessor
from src.services.data_storer import DataStorer, MySQLDatabaseService

# Asegúrate de que el directorio `src` esté en el `PYTHONPATH`
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

logger = LoggerConfigurator().configure()
load_dotenv()

# Validar la configuración de la base de datos desde las variables de entorno
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

if not all(db_config.values()):
    logger.error("Database configuration variables are missing in the environment.")
    raise EnvironmentError("Database configuration variables are missing.")

database_name = os.getenv('DB_NAME')
table_name = "vueltas_table"
esp_url = os.getenv('ESP_URL')

if not database_name or not esp_url:
    logger.error("DB_NAME or ESP_URL variables are missing in the environment.")
    raise EnvironmentError("DB_NAME or ESP_URL variables are missing.")

def main():
    data_extractor = DataExtractor(esp_url)
    data_processor = DataProcessor()
    db_service = MySQLDatabaseService(db_config, logger)
    data_storer = DataStorer(db_service)
    
    html_content = data_extractor.fetch_data()
    if html_content:
        vueltas = data_processor.extract_vueltas(html_content)
        if vueltas is not None:
            data_storer.store_vueltas(vueltas, database_name, table_name)

if __name__ == '__main__':
    main()
