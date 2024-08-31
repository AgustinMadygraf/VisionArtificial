/* 
static/js/main_camara.js
Este archivo contiene el código principal de la aplicación. Se encarga de inicializar las clases 
y objetos necesarios, y de configurar los listeners de eventos para la interacción con el usuario.
*/

import ImageProcessor from './imageProcessor/ImageProcessor.js';
import VerticalLineStrategy from './imageProcessor/strategies/VerticalLineStrategy.js';
import CanvasUtilsImpl from './implementations/CanvasUtilsImpl.js';
import WebSocketUtilsImpl from './implementations/WebSocketUtilsImpl.js';
import VideoManager from './videoManager.js';
import { adjustLayoutForOrientation } from './uiManager.js'; // Import the function
import DOMUpdater from './domUpdater.js'; // Import the class

// Implementaciones de interfaces
const canvasUtils       = new CanvasUtilsImpl();
const webSocketUtils    = new WebSocketUtilsImpl();
const strategy          = new VerticalLineStrategy(canvasUtils, webSocketUtils);
const imageProcessor    = new ImageProcessor(5, 100, 50, canvasUtils, webSocketUtils, strategy);
const domUpdater        = new DOMUpdater(); // Create an instance of DOMUpdater

// Define refreshInterval
const refreshInterval = 20;

// Función para inicializar VideoManager
function initializeVideoManager(testValue) {
    const videoManager = new VideoManager(testValue);
    videoManager.initialize();
    videoManager.startVideoStream();
    return videoManager;
}

// Función para configurar los listeners de eventos
function setupEventListeners() {
    adjustLayoutForOrientation();
    window.addEventListener('resize', adjustLayoutForOrientation);
}

// Función principal de inicialización
function initializeApp() {
    console.log("DOM fully loaded and parsed");

    //const testValue = getQueryParam('test'); // Use the imported function
    const testValue = null;
    console.log("Query parameter 'test':", testValue);

    const videoManager = initializeVideoManager(testValue);
    console.log("VideoManager initialized:", videoManager);
    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img); // Use the instance method
    }, refreshInterval);
    setupEventListeners();
    console.log("Event listeners set up");
}

// Evento DOMContentLoaded

document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});