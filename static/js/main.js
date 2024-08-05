import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor/ImageProcessor.js';
import DOMUpdater from './domUpdater.js';
import { initializeWebSocket, sendWebSocketMessage } from './imageProcessor/webSocketUtils.js';
import { adjustLayoutForOrientation } from './uiManager.js';
import * as canvasUtils from './utils/canvasUtils.js';
import { getQueryParam } from './getQueryParam.js';
import CanvasUtilsInterface from './interfaces/canvasUtilsInterface.js';
import WebSocketUtilsInterface from './interfaces/webSocketUtilsInterface.js';

// Variables de configuración
const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;
const refreshInterval = 20;

// Implementaciones de interfaces
class CanvasUtilsImpl extends CanvasUtilsInterface {
    drawVerticalLine(context, pos, color) {
        canvasUtils.drawVerticalLine(context, pos, color);
    }
    drawHorizontalLine(context, pos, color) {
        canvasUtils.drawHorizontalLine(context, pos, color);
    }
    drawCenterRuler(context, color, lineLength, spacing) {
        canvasUtils.drawCenterRuler(context, color, lineLength, spacing);
    }
}

class WebSocketUtilsImpl extends WebSocketUtilsInterface {
    initializeWebSocket() {
        initializeWebSocket();
    }
    sendWebSocketMessage(message) {
        sendWebSocketMessage(message);
    }
}

// Función para inicializar WebSocketUtils
function initializeWebSocketUtils() {
    const webSocketUtilsImpl = new WebSocketUtilsImpl();
    webSocketUtilsImpl.initializeWebSocket();
    return webSocketUtilsImpl;
}

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

    const canvasUtilsImpl = new CanvasUtilsImpl();
    console.log("CanvasUtilsImpl initialized:", canvasUtilsImpl);

    const webSocketUtilsImpl = initializeWebSocketUtils();
    console.log("WebSocketUtilsImpl initialized:", webSocketUtilsImpl);

    const videoManager = initializeVideoManager();
    console.log("VideoManager initialized:", videoManager);

    const imageProcessor = new ImageProcessor(secs, halfEvalHeight, halfEvalWidth, canvasUtilsImpl, webSocketUtilsImpl);
    console.log("ImageProcessor initialized:", imageProcessor);

    const domUpdater = new DOMUpdater();
    console.log("DOMUpdater initialized:", domUpdater);

    console.log("Initializing VideoManager...");

    const testValue = getQueryParam('test');
    console.log("Query parameter 'test':", testValue);

    if (testValue === 'True') {
        console.log("Test value is True, setting video source to 'test.jpeg'");
        const videoElement = document.getElementById('vid'); // Corrección aquí
        videoElement.src = 'test.jpeg';
        videoElement.style.display = 'block';
    } else {
        console.log("Test value is not True, starting image processing interval");
        setInterval(() => {
            const img = imageProcessor.pickImage(videoManager.video);
            domUpdater.updateCanvas(img);
        }, refreshInterval);
    }

    setupEventListeners();
    console.log("Event listeners set up");
}

// Evento DOMContentLoaded
document.addEventListener("DOMContentLoaded", initializeApp);