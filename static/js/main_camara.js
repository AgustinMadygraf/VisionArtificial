/* 
static/js/main_camara.js
Este archivo contiene el código principal de la aplicación. Se encarga de inicializar las clases 
y objetos necesarios, y de configurar los listeners de eventos para la interacción con el usuario.
*/

import ImageProcessor from './imageProcessor/ImageProcessor.js';
import VerticalLineStrategy from './imageProcessor/strategies/VerticalLineStrategy.js';
import CanvasUtilsImpl from './implementations/CanvasUtilsImpl.js';
import WebSocketUtilsImpl from './implementations/WebSocketUtilsImpl.js';
import DOMUpdater from './domUpdater.js';
import { initializeVideoManager } from './videoManagerInitializer.js';
import { setupEventListeners } from './eventListeners.js'; // Import the function

// Implementaciones de interfaces
const canvasUtils       = new CanvasUtilsImpl();
const webSocketUtils    = new WebSocketUtilsImpl();
const strategy          = new VerticalLineStrategy(canvasUtils, webSocketUtils);
const imageProcessor    = new ImageProcessor(5, 100, 50, canvasUtils, webSocketUtils, strategy);
const domUpdater        = new DOMUpdater(); // Create an instance of DOMUpdater

// Define refreshInterval
const refreshInterval = 20;

/**
 * Función principal de inicialización.
 * Inicializa el VideoManager, configura el procesamiento de imágenes y los listeners de eventos.
 */
function initializeApp() {
    console.log("DOM fully loaded and parsed");
    const videoManager = initializeVideoManager();
    console.log("VideoManager initialized:", videoManager);
    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
    }, refreshInterval);
    setupEventListeners();
    console.log("Event listeners set up");
}

// Evento DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});