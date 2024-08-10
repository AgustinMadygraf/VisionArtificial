# Visión Artificial e Ingesta de Datos

Este proyecto ofrece un servidor web seguro que permite la visualización en tiempo real de la transmisión de video desde una webcam, la captura de imágenes, y la superposición de líneas y reglas para análisis visual. Además, facilita la ingesta de datos desde dispositivos externos, procesando y almacenando la información para su integración en flujos de trabajo de análisis de datos.

## Requisitos

- **Python 3.6 o superior**: Asegúrate de tener instalada una versión compatible de Python.
- **OpenSSL**: Necesario para la generación de certificados SSL que aseguran la conexión.
- **Navegador Moderno**: Requiere un navegador con soporte para módulos ES6 para interactuar con la interfaz web.

## Configuración

1. **Clonación del Repositorio**:
   
   Clona el repositorio del proyecto desde GitHub y navega al directorio del proyecto:

   ```bash
   git clone https://github.com/AgustinMadygraf/VisionArtificial
   cd VisionArtificial
   ```

2. **Instalación de Dependencias**:
   
   Instala todas las dependencias necesarias y configura un entorno virtual utilizando el archivo `setup.py`:

   ```bash
   python setup.py
   ```

   Esto actualizará `pip`, instalará las dependencias requeridas y verificará que estén correctamente configuradas.

3. **Configuración SSL**:
   
   Adjunta los certificados SSL en la ubicación indicada para asegurar la conexión segura del servidor web.

## Ejecución del Servidor

1. **Iniciar el Servidor**:

   Puedes iniciar el servidor utilizando el archivo `VisionArtificial.bat` o a través del acceso directo creado en el escritorio. También puedes iniciar el servidor manualmente desde la línea de comandos:

   ```bash
   pipenv run python run.py
   ```

   El servidor estará disponible en `https://<TU_DIRECCION_IP>:4443`.

## Uso

1. **Acceso a la Interfaz**:

   Abre un navegador y navega a `https://<TU_DIRECCION_IP>:4443` para acceder a la interfaz del sistema.

2. **Funcionalidades Disponibles**:

   - **Transmisión en Vivo**: Visualiza la transmisión de video desde la webcam en tiempo real.
   - **Captura de Imágenes**: Toma capturas de pantalla para su posterior análisis.
   - **Ingesta de Datos**: El sistema automáticamente ingiere datos desde dispositivos externos configurados, procesándolos y almacenándolos en la base de datos para su análisis.

3. **Ajustes Avanzados**:

   - **Configuración del Tiempo de Refresco**: Puedes ajustar el tiempo de refresco de la captura de pantalla utilizando el parámetro `t` en la URL. Ejemplo: `https://<TU_DIRECCION_IP>:4443/?t=2500`.

## Logs

Los registros del sistema se almacenan en la carpeta `logs/`, dentro del archivo `sistema.log`. Estos logs capturan información a nivel `INFO` y `ERROR`, proporcionando un seguimiento detallado de las operaciones del sistema y facilitando la identificación y resolución de problemas.
