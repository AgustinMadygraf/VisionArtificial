# Guía de Uso del Proyecto

Esta guía proporciona instrucciones detalladas sobre cómo utilizar las funcionalidades del software para el procesamiento de imágenes en un sistema de control de procesos productivos.

## Funcionalidades Principales

1. **Procesamiento de Imágenes**
   - Descripción: El sistema procesa las imágenes capturadas para analizar y controlar el proceso productivo.
   - Uso: 
     - Inicia la transmisión de video desde la webcam.
     - Captura imágenes en tiempo real.
     - Procesa las imágenes para extraer información relevante para el control del proceso.

2. **Clasificación de la Posición del Objeto**
   - Descripción: El sistema clasifica la posición de un objeto en la imagen para determinar su desviación respecto a la posición deseada.
   - Uso: 
     - Define la posición deseada del objeto en la configuración del sistema.
     - El sistema analiza cada imagen capturada para determinar la posición actual del objeto.
     - Calcula la desviación del objeto respecto a la posición deseada y actúa en consecuencia.

## Pasos para Iniciar el Sistema

1. **Iniciar la Transmisión de Video**
   - Abre un navegador y navega a `https://<TU_DIRECCION_IP>:4443`.
   - Presiona el botón "Open WebCam" para iniciar la transmisión de video desde tu webcam.

2. **Tomar una Captura de Pantalla**
   - Presiona el botón "Take Screenshot" para tomar una captura de pantalla de la transmisión de video.
   - La imagen capturada se utilizará para el análisis y procesamiento.

3. **Configuración del Tiempo de Refresco**
   - Puedes ajustar el tiempo de refresco de la captura de pantalla utilizando el parámetro `t` en la URL. 
   - Ejemplo: `https://<TU_DIRECCION_IP>:4443/?t=2500` ajustará el tiempo de refresco a 2500 milisegundos. El valor por defecto es 20 milisegundos.

## Características Avanzadas

1. **Ajuste de Parámetros de Configuración**
   - Descripción: Ajusta los parámetros de configuración del sistema para optimizar el procesamiento de imágenes.
   - Ejemplo: Modificar la sensibilidad de detección de la posición del objeto en el archivo de configuración.

2. **Integración con Otros Dispositivos IoT**
   - Descripción: Conecta el sistema con otros dispositivos IoT para un control integrado del proceso productivo.
   - Ejemplo: Utiliza el ESPWROOM32 para enviar y recibir datos en tiempo real, ajustando el proceso según la información obtenida del análisis de imágenes.

## Ejemplos Prácticos

1. **Iniciar la Transmisión de Video**
   - Navega a `https://<TU_DIRECCION_IP>:4443`.
   - Presiona "Open WebCam".

2. **Tomar una Captura y Analizar la Imagen**
   - Presiona "Take Screenshot".
   - El sistema procesará la imagen para determinar la posición del objeto y calcular cualquier desviación.

3. **Configurar el Tiempo de Refresco**
   - Ajusta la URL a `https://<TU_DIRECCION_IP>:4443/?t=2000` para establecer el tiempo de refresco en 2000 milisegundos.

## Contacto y Soporte

Si encuentras algún problema o necesitas ayuda adicional, por favor contacta al equipo de desarrollo en [email@example.com](mailto:email@example.com).
