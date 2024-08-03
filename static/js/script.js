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

// Obtener el tiempo de refresco de la URL, por defecto 20 milisegundos
const refreshInterval = parseInt(getUrlParameter('t')) || 20;

// Obtener la IP local desde el servidor
async function getLocalIp() {
    const response = await fetch('/local-ip');
    const data = await response.json();
    return data.ip;
}

let ws;
let isWebSocketOpen = false; // Bandera para controlar el estado del WebSocket
let messageCount = 0; // Contador de mensajes

async function initializeWebSocket() {
    const localIp = await getLocalIp();
    ws = new WebSocket(`wss://${localIp}:8765`);

    ws.onopen = function() {
        console.log("WebSocket connection established");
        isWebSocketOpen = true; // Establecer la bandera a true cuando se abre la conexión
    };

    ws.onerror = function(error) {
        console.error("WebSocket error: " + error);
    };

    ws.onclose = function() {
        console.log("WebSocket connection closed");
        isWebSocketOpen = false; // Establecer la bandera a false cuando se cierra la conexión
    };
}

export function sendWebSocketMessage(message) {
    messageCount++; // Incrementar el contador de mensajes

    if (messageCount % 100 === 0) { // Enviar el mensaje si el contador es múltiplo
        if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send(message);
        } else {
            console.error("WebSocket is not open. Unable to send message.");
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    initializeWebSocket();
    const videoManager = new VideoManager();
    const imageProcessor = new ImageProcessor(secs, halfEvalHeight, halfEvalWidth);
    const domUpdater = new DOMUpdater();

    videoManager.initialize();

    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
    }, refreshInterval);
});