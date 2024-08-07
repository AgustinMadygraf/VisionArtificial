// static/js/main.js
import ImageProcessor from './imageProcessor/ImageProcessor.js';
import VerticalLineStrategy from './imageProcessor/strategies/VerticalLineStrategy.js';
import CanvasUtilsImpl from './implementations/CanvasUtilsImpl.js';
import WebSocketUtilsImpl from './implementations/WebSocketUtilsImpl.js';
import VideoManager from './videoManager.js';
import { getQueryParam } from './utils/urlUtils.js'; // Import the function
import { adjustLayoutForOrientation } from './uiManager.js'; // Import the function
import DOMUpdater from './domUpdater.js'; // Import the class

// Implementaciones de interfaces
const canvasUtils = new CanvasUtilsImpl();
const webSocketUtils = new WebSocketUtilsImpl();
const strategy = new VerticalLineStrategy(canvasUtils, webSocketUtils);
const imageProcessor = new ImageProcessor(5, 100, 50, canvasUtils, webSocketUtils, strategy);
const domUpdater = new DOMUpdater(); // Create an instance of DOMUpdater

// Define refreshInterval
const refreshInterval = 20;

// Función para inicializar VideoManager
function initializeVideoManager() {
    const videoManager = new VideoManager();
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

    console.log("CanvasUtilsImpl initialized:", canvasUtils);
    console.log("WebSocketUtilsImpl initialized:", webSocketUtils);

    const videoManager = initializeVideoManager();
    console.log("VideoManager initialized:", videoManager);

    console.log("ImageProcessor initialized:", imageProcessor);

    console.log("Initializing VideoManager...");

    const testValue = getQueryParam('test'); // Use the imported function
    console.log("Query parameter 'test':", testValue);

    if (testValue === 'True') {
        console.log("Test value is True, setting video source to 'test.jpeg'");
        const videoElement = document.getElementById('vid');
        videoElement.src = 'test.jpeg';
        videoElement.style.display = 'block';
    } else {
        console.log("Test value is not True, starting image processing interval");
        setInterval(() => {
            const img = imageProcessor.pickImage(videoManager.video);
            domUpdater.updateCanvas(img); // Use the instance method
        }, refreshInterval);
    }

    setupEventListeners();
    console.log("Event listeners set up");
}

// Evento DOMContentLoaded
document.addEventListener('DOMContentLoaded', (event) => {
    initializeApp();
});