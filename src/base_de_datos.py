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
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

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

def store_vueltas_to_db(vueltas, config):
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO vueltas_table (vueltas) VALUES (%s)", (vueltas,))
            connection.commit()
            print("Valor insertado correctamente en la base de datos.")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    html_content = fetch_esp_data(esp_url)
    if html_content:
        vueltas = extract_vueltas(html_content)
        if vueltas is not None:
            store_vueltas_to_db(vueltas, db_config)

if __name__ == '__main__':
    main()
