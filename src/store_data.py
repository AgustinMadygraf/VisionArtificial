#src/store_data.py
import requests
import mysql.connector
from mysql.connector import Error
import re
from dotenv import load_dotenv
import os
import time

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos desde las variables de entorno
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Nombre de la base de datos y la tabla
database_name = os.getenv('DB_NAME')
table_name = "vueltas_table"

# URL del ESPWROOM32 desde la variable de entorno
esp_url = os.getenv('ESP_URL')

def fetch_esp_data(url, retries=5, timeout=10):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Intento {attempt + 1} fallido al obtener datos de {url}: {e}")
            attempt += 1
            time.sleep(2 ** attempt)  # Espera exponencial antes de reintentar
    print(f"Error: No se pudo obtener datos de {url} después de {retries} intentos.")
    return None

def extract_vueltas(html):
    try:
        match = re.search(r'Vueltas:\s*(\d+)', html)
        if match:
            return int(match.group(1))
        else:
            print("No se encontró el valor de 'Vueltas' en la respuesta.")
            return None
    except re.error as e:
        print(f"Error al extraer datos: {e}")
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
        print(f"Base de datos '{database_name}' y tabla '{table_name}' creadas/existentes.")
    except Error as e:
        print(f"Error al crear la base de datos o la tabla: {e}")
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
            print("Valor insertado correctamente en la base de datos.")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
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
