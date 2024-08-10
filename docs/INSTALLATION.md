# Guía de Instalación y Configuración

Este documento proporciona instrucciones detalladas para la instalación y configuración del proyecto **Visión Artificial e Ingesta de Datos**.

## Requisitos Previos

Antes de comenzar con la instalación, asegúrate de cumplir con los siguientes requisitos previos:

- **Python 3.6 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **OpenSSL**: Necesario para la generación de certificados SSL. [Descargar OpenSSL](https://www.openssl.org/source/)
- **Navegador Moderno**: Que soporte módulos ES6.
- **Git**: Necesario para clonar el repositorio.

## Clonación del Repositorio

Primero, clona el repositorio del proyecto desde GitHub:

```bash
git clone https://github.com/AgustinMadygraf/VisionArtificial
cd VisionArtificial
```

## Instalación de Dependencias

El proyecto depende de varias bibliotecas de Python, que se gestionan a través de `pipenv` y un archivo `Pipfile`. A continuación, se explica cómo instalar estas dependencias:

1. **Instalación de dependencias usando `setup.py`**:

   El archivo `setup.py` proporcionado automatiza la instalación y actualización de las dependencias necesarias.

   ```bash
   python setup.py
   ```

   Este script actualizará `pip`, instalará las dependencias listadas en el `Pipfile`, y verificará que todas las dependencias estén correctamente instaladas.

2. **Verificación de la instalación de `pipenv`**:

   El script `setup.py` también se asegura de que `pipenv` esté actualizado y sincronizado con los archivos `Pipfile` y `Pipfile.lock`. Si `pipenv` no está instalado o necesita actualización, el script lo maneja automáticamente.

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

El proyecto utiliza un archivo `.env` para gestionar variables de entorno sensibles. Este archivo debe configurarse correctamente para que el sistema funcione de manera óptima.

1. **Cambia el nombre del archivo `EXAMPLE.env` a `.env`**:

   En el directorio raíz del proyecto, modifica un archivo llamado `EXAMPLE.env` 

   ```plaintext
   DB_HOST=Tu_host
   DB_NAME=Nombre_de_tu_base_de_datos
   DB_USER=Tu_usuario
   DB_PASSWORD=Tu_contraseña
   ESP_URL=Tu_url
   PYTHONPATH="C:\AppServ\www\VisionArtificial;C:\AppServ\www\VisionArtificial\src"
   ```

   Asegúrate de reemplazar `Tu_host`, `Nombre_de_tu_base_de_datos`, `Tu_usuario`, `Tu_contraseña` y `Tu_url` con los valores correctos para tu entorno.

## Ejecución del Servidor

Para iniciar el servidor, sigue estos pasos:

1. **Iniciar el servidor**:

   Puedes ejecutar el servidor utilizando el archivo `VisionArtificial.bat` o mediante el acceso directo creado en tu escritorio. Alternativamente, puedes iniciar el servidor manualmente:

   ```bash
   python run.py
   ```

   El servidor estará disponible en `https://<TU_DIRECCION_IP>:4443`.

## Ejecución del Sistema de Ingesta de Datos

El proyecto incluye un componente para la ingesta y procesamiento de datos a partir de una fuente externa (configurada a través de `ESP_URL`). Para ejecutar este sistema:

1. **Ejecutar el script de ingesta de datos**:

   ```bash
   python src/store_data.py
   ```

   Este script conectará a la base de datos utilizando las credenciales configuradas, extraerá los datos desde `ESP_URL`, los procesará y almacenará en la tabla `vueltas_table` dentro de la base de datos especificada.

## Resolución de Problemas Comunes

- **Error al conectar a la base de datos**: Verifica que las credenciales y el nombre de la base de datos en el archivo `.env` sean correctos.
- **Certificados SSL no encontrados**: Asegúrate de que los archivos `server.key` y `server.crt` estén en el directorio raíz del proyecto y que los nombres sean correctos.
- **Error durante la ingesta de datos**: Asegúrate de que `ESP_URL` está correctamente configurada en el archivo `.env` y que la conexión con la fuente de datos externa es estable.

## Contacto

Si encuentras algún problema durante la instalación o configuración, por favor contacta al equipo de desarrollo en [agustin.mtto.madygraf@gmail.com](mailto:agustin.mtto.madygraf@gmail.com).