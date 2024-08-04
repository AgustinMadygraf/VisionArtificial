// static/js/main.js

import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor.js';
import DOMUpdater from './domUpdater.js';
import { initializeWebSocket } from './webSocketManager.js';
import { adjustLayoutForOrientation } from './uiManager.js';

// Constantes de configuración para la evaluación de la imagen
const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;
const refreshInterval = 20;

/**
 * Inicializa la aplicación una vez que el DOM ha sido completamente cargado.
 */
document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");
    
    // Inicializar el WebSocket para la comunicación
    initializeWebSocket();
    
    // Crear instancias de los gestores de video, imagen y DOM
    const videoManager = new VideoManager();
    const imageProcessor = new ImageProcessor(secs, halfEvalHeight, halfEvalWidth);
    const domUpdater = new DOMUpdater();

    console.log("Initializing VideoManager...");
    videoManager.initialize();
    videoManager.startVideoStream();

    // Establecer un intervalo para procesar imágenes del video
    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
    }, refreshInterval);

    // Ajustar el diseño para la orientación inicial y en cada cambio de tamaño de la ventana
    adjustLayoutForOrientation();
    window.addEventListener('resize', adjustLayoutForOrientation);
});
