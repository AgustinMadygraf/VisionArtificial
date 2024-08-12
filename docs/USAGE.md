# Guía de Uso del Proyecto

Esta guía proporciona instrucciones detalladas sobre cómo utilizar las funcionalidades del software **Visión Artificial e Ingesta de Datos** para el procesamiento de imágenes y la ingesta de datos en un sistema de control de procesos productivos.

## Funcionalidades Principales

1. **Procesamiento de Imágenes**
   - **Descripción**: El sistema permite la visualización de la transmisión en vivo desde una webcam, captura imágenes en tiempo real, y las procesa para extraer información relevante que puede ser utilizada para el control de procesos productivos.
   - **Uso**: 
     - Inicia la transmisión de video desde la webcam.
     - Captura imágenes en tiempo real.
     - Procesa las imágenes para extraer información relevante para el control del proceso, como la posición de objetos y su desviación respecto a posiciones deseadas.

2. **Ingesta y Almacenamiento de Datos**
   - **Descripción**: El sistema extrae datos de un dispositivo externo a través de una URL configurada, los procesa y almacena en una base de datos.
   - **Uso**: 
     - Configura la URL del dispositivo externo en el archivo `.env`.
     - Ejecuta el script de ingesta de datos para extraer, procesar y almacenar la información obtenida.

3. **Clasificación de la Posición del Objeto**
   - **Descripción**: El sistema analiza cada imagen capturada para determinar la posición actual de un objeto y calcula cualquier desviación respecto a la posición deseada, permitiendo realizar ajustes automáticos en el proceso productivo.
   - **Uso**: 
     - Define la posición deseada del objeto en la configuración del sistema.
     - El sistema analizará cada imagen capturada para determinar la posición actual del objeto.
     - Calcula la desviación del objeto respecto a la posición deseada y actúa en consecuencia.

## Pasos para Iniciar el Sistema

1. **Iniciar la Transmisión de Video**
   - Abre un navegador y navega a `https://<TU_DIRECCION_IP>:4443`.
2. **Ejecutar el Sistema de Ingesta de Datos**
   - Navega al directorio raíz del proyecto.
   - Ejecuta el siguiente comando para iniciar la ingesta de datos:
   
     ```bash
     python src/store_data.py
     ```
   - Este comando extraerá los datos de la URL configurada en el archivo `.env`, los procesará y los almacenará en la base de datos especificada.

## Características Avanzadas

1. **Ajuste de Parámetros de Configuración**
   - **Descripción**: Ajusta los parámetros de configuración del sistema para optimizar el procesamiento de imágenes y la ingesta de datos.
   - **Ejemplo**: Modificar la sensibilidad de detección de la posición del objeto en el archivo de configuración o ajustar la URL y las credenciales de la base de datos en el archivo `.env`.

2. **Integración con Otros Dispositivos IoT**
   - **Descripción**: Conecta el sistema con otros dispositivos IoT para un control integrado del proceso productivo.
   - **Ejemplo**: Utiliza el ESPWROOM32 para enviar y recibir datos en tiempo real, ajustando el proceso según la información obtenida del análisis de imágenes y los datos ingeridos.

## Contacto y Soporte

Si encuentras algún problema o necesitas ayuda adicional, por favor contacta al equipo de desarrollo en [agustin.mtto.madygraf@gmail.com](mailto:agustin.mtto.madygraf@gmail.com).
