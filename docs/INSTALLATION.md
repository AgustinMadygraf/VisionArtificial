# Guía de Instalación y Configuración

Este documento proporciona instrucciones detalladas para la instalación y configuración del proyecto **Webcam Server Project**.

## Requisitos Previos

Antes de comenzar con la instalación, asegúrate de tener los siguientes requisitos previos:

- **Python 3.6 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **OpenSSL**: Necesario para la generación de certificados SSL. [Descargar OpenSSL](https://www.openssl.org/source/)
- **Navegador Moderno**: Que soporte ES6 módulos.

## Clonación del Repositorio

Primero, clona el repositorio del proyecto desde GitHub:

```bash
git clone https://github.com/AgustinMadygraf/IoTImageProc
cd IoTImageProc
```

## Instalación de Dependencias

Instala las dependencias necesarias para el proyecto. Si utilizas `pip`, puedes crear un entorno virtual e instalar las dependencias:

1. Crear un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Generación de Certificados SSL

El proyecto requiere certificados SSL para funcionar correctamente. Si no tienes certificados, puedes generarlos utilizando OpenSSL:

1. Generar una clave privada:

   ```bash
   openssl genrsa -out server.key 2048
   ```

2. Generar un certificado autofirmado:

   ```bash
   openssl req -new -x509 -key server.key -out server.crt -days 365
   ```

Coloca los archivos `server.key` y `server.crt` en el directorio raíz del proyecto.

## Configuración del Entorno

El proyecto utiliza un archivo `.env` para gestionar variables de entorno sensibles. Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:

```plaintext
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=nombre_de_tu_base_de_datos
ESP_URL=http://tu_direccion_ip
```

Asegúrate de reemplazar `tu_usuario`, `tu_contraseña`, `nombre_de_tu_base_de_datos` y `tu_direccion_ip` con los valores correctos para tu entorno.

## Ejecución del Servidor

Para iniciar el servidor, ejecuta el siguiente comando:

```bash
python src/main.py
```

El servidor estará disponible en `https://<TU_DIRECCION_IP>:4443`.

## Resolución de Problemas Comunes

- **Error al conectar a la base de datos**: Verifica que las credenciales y el nombre de la base de datos en el archivo `.env` sean correctos.
- **Certificados SSL no encontrados**: Asegúrate de que los archivos `server.key` y `server.crt` estén en el directorio raíz del proyecto y que los nombres sean correctos.

## Contacto

Si encuentras algún problema durante la instalación o configuración, por favor contacta al equipo de desarrollo en [agustin.mtto.madygraf@gmail.com](mailto:agustin.mtto.madygraf@gmail.com).