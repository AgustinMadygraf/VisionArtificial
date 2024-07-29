import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor.js';
import DOMUpdater from './domUpdater.js';

const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;

// Función para obtener el valor de un parámetro de la URL
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Obtener el tiempo de refresco de la URL, por defecto 3000 milisegundos
const refreshInterval = parseInt(getUrlParameter('t')) || 3000;

// Interceptar console.log y enviar los mensajes al servidor WebSocket
(function() {
    const originalConsoleLog = console.log;
    const ws = new WebSocket("ws://localhost:8765");

    ws.onopen = function() {
        console.log = function(message) {
            originalConsoleLog.apply(console, arguments);
            ws.send(message);
        };
    };

    ws.onerror = function(error) {
        originalConsoleLog("WebSocket error: " + error);
    };

    ws.onclose = function() {
        console.log = originalConsoleLog;
    };
})();

document.addEventListener("DOMContentLoaded", () => {
    const videoManager = new VideoManager();
    const imageProcessor = new ImageProcessor(secs, halfEvalHeight, halfEvalWidth);
    const domUpdater = new DOMUpdater();

    videoManager.initialize();

    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
    }, refreshInterval);
});