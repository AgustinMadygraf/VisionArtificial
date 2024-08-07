import requests
import mysql.connector
from mysql.connector import Error
import re
from dotenv import load_dotenv
import os
import time
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

def fetch_esp_data(url, retries=5, timeout=10):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Attempt {attempt + 1} failed to fetch data from {url}: {e}")
            attempt += 1
            time.sleep(2 ** attempt)  # Exponential backoff before retrying
    logger.error(f"Failed to fetch data from {url} after {retries} attempts.")
    return None

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

def create_database_and_table(config, database_name, table_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password']
        )
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
        logger.info(f"Database '{database_name}' and table '{table_name}' created/existing.")
    except Error as e:
        logger.error(f"Error creating database or table: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def store_vueltas_to_db(vueltas, config, database_name, table_name):
    config_with_db = config.copy()
    config_with_db['database'] = database_name
    connection = None
    try:
        connection = mysql.connector.connect(**config_with_db)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO {table_name} (vueltas) VALUES (%s)", (vueltas,))
            connection.commit()
            logger.info("Value successfully inserted into the database.")
    except Error as e:
        logger.error(f"Error connecting to the database: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def main():
    create_database_and_table(db_config, database_name, table_name)
    
    html_content = fetch_esp_data(esp_url)
    if html_content:
        vueltas = extract_vueltas(html_content)
        if vueltas is not None:
            store_vueltas_to_db(vueltas, db_config, database_name, table_name)

if __name__ == '__main__':
    main()
