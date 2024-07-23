# Webcam Server Project

Este proyecto proporciona un servidor web seguro que permite la visualización de la transmisión de video desde una webcam, la toma de capturas de pantalla y la visualización de varias líneas y reglas sobre la imagen capturada.

## Estructura del Proyecto

```
webcam2/
├── index.html
├── js/
│   ├── script.js
│   ├── videoManager.js
│   ├── imageProcessor.js
│   ├── domUpdater.js
│   ├── canvasUtils.js
├── server.py
├── ssl_config.py
├── style.css
└── logs/
    ├── config_logger.py
    ├── logging.json
    └── __init__.py
```

## Requisitos

- Python 3.6 o superior
- OpenSSL (para la generación de certificados SSL)
- Navegador moderno que soporte ES6 módulos

## Configuración

1. Clona el repositorio del proyecto:

   ```bash
   git clone https://github.com/AgustinMadygraf/webcam2
   cd webcam2
   ```

2. Instala las dependencias necesarias (si las hay).

3. Genera los certificados SSL (si no existen). Los certificados se generarán automáticamente si no se encuentran.

## Ejecución del Servidor

1. Ejecuta el servidor utilizando Python:

   ```bash
   python server.py
   ```

   El servidor estará disponible en `https://<TU_DIRECCION_IP>:4443`.

## Uso

1. Abre un navegador y navega a `https://<TU_DIRECCION_IP>:4443`.

2. Presiona el botón "Open WebCam" para iniciar la transmisión de video desde tu webcam.

3. Presiona el botón "Take Screenshot" para tomar una captura de pantalla de la transmisión de video.

4. Puedes ajustar el tiempo de refresco de la captura de pantalla utilizando el parámetro `t` en la URL. Por ejemplo, `https://<TU_DIRECCION_IP>:4443/?t=2500` ajustará el tiempo de refresco a 2500 milisegundos. El valor por defecto es 3000 milisegundos.

## Descripción de los Archivos

- **index.html**: Página principal del proyecto.
- **js/script.js**: Archivo principal de JavaScript que inicializa los componentes y gestiona el intervalo de refresco.
- **js/videoManager.js**: Clase para manejar la transmisión de video.
- **js/imageProcessor.js**: Clase para procesar las imágenes capturadas.
- **js/domUpdater.js**: Clase para actualizar el DOM con la nueva imagen capturada.
- **js/canvasUtils.js**: Utilidades para dibujar líneas y reglas en el canvas.
- **server.py**: Servidor web principal que maneja las solicitudes HTTP y HTTPS.
- **ssl_config.py**: Configuración y generación de certificados SSL.
- **logs/config_logger.py**: Configuración del sistema de logging.
- **logs/logging.json**: Archivo de configuración para el logging.
- **style.css**: Archivo de estilos para la página web.

## Logs

Los logs se generan en la carpeta `logs/` y están configurados para registrar información de nivel `INFO` y `ERROR`.
