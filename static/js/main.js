import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor/ImageProcessor.js';
import DOMUpdater from './domUpdater.js';
import { initializeWebSocket, sendWebSocketMessage } from './imageProcessor/webSocketUtils.js';
import { adjustLayoutForOrientation } from './uiManager.js';
import * as canvasUtils from './utils/canvasUtils.js';
import { getQueryParam } from './getQueryParam.js';

// Usa la función para obtener el valor del parámetro GET llamado "test"
const testValue = getQueryParam('test');
console.log("el valor del parámetro GET llamado 'test' es: ", testValue); 

// Implement the interfaces
import CanvasUtilsInterface from './interfaces/canvasUtilsInterface.js';
import WebSocketUtilsInterface from './interfaces/webSocketUtilsInterface.js';

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

const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;
const refreshInterval = 20;

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");

    const canvasUtilsImpl = new CanvasUtilsImpl();
    const webSocketUtilsImpl = new WebSocketUtilsImpl();

    webSocketUtilsImpl.initializeWebSocket();

    const videoManager = new VideoManager();
    const imageProcessor = new ImageProcessor(secs, halfEvalHeight, halfEvalWidth, canvasUtilsImpl, webSocketUtilsImpl);
    const domUpdater = new DOMUpdater();

    console.log("Initializing VideoManager...");

    if (testValue === 'True') {
        // Transmit an image instead of the camera stream
        const videoElement = document.getElementById('vid');
        videoElement.src = 'test.jpeg';
        videoElement.style.display = 'block';
    } else {
        videoManager.initialize();
        videoManager.startVideoStream();

        setInterval(() => {
            const img = imageProcessor.pickImage(videoManager.video);
            domUpdater.updateCanvas(img);
        }, refreshInterval);
    }

    adjustLayoutForOrientation();
    window.addEventListener('resize', adjustLayoutForOrientation);
});