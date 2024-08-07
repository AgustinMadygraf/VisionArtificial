# src/store_data.py
import sys
import os

# Asegúrate de que el directorio `src` esté en el `PYTHONPATH`
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import re
from dotenv import load_dotenv
from src.services.database_service import MySQLDatabaseService
from src.services.http_service import HTTPService
from src.logs.config_logger import LoggerConfigurator

logger = LoggerConfigurator().configure()
# Cargar las variables de entorno desde el archivo .env
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

# Validar el nombre de la base de datos y la URL del ESPWROOM32 desde las variables de entorno
database_name = os.getenv('DB_NAME')
table_name = "vueltas_table"
esp_url = os.getenv('ESP_URL')

if not database_name or not esp_url:
    logger.error("DB_NAME or ESP_URL variables are missing in the environment.")
    raise EnvironmentError("DB_NAME or ESP_URL variables are missing.")

def extract_vueltas(html):
    try:
        match = re.search(r'Vueltas:\s*(\d+)', html)
        if match:
            return int(match.group(1))
        else:
            logger.info("Vueltas value not found in the response.")
            return None
    except re.error as e:
        logger.error(f"Error extracting data: {e}")
        return None

def main(db_service, http_service):
    db_service.create_database_and_table(database_name, table_name)
    
    html_content = http_service.fetch_data(esp_url)
    if html_content:
        vueltas = extract_vueltas(html_content)
        if vueltas is not None:
            db_service.store_vueltas(vueltas, database_name, table_name)

if __name__ == '__main__':
    db_service = MySQLDatabaseService(db_config, logger)
    http_service = HTTPService(logger)
    main(db_service, http_service)
