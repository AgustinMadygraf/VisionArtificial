// static/js/script.js
import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor.js';
import DOMUpdater from './domUpdater.js';

const secs = 3;             // Obtener el número de segundos para la evaluación de la imagen
const halfEvalHeight = 10;  // Obtener la mitad de la altura de la evaluación de la imagen
const halfEvalWidth = 200;  // Obtener la mitad del ancho de la evaluación de la imagen
const refreshInterval = 20; // Obtener el tiempo de refresco de la URL, 20 milisegundos

// Obtener la IP local desde el servidor
async function getLocalIp() {
    try {
        const response = await fetch('/local-ip');
        const data = await response.json();
        console.log('Local IP:', data.ip);
        return data.ip;
    } catch (error) {
        console.error('Error fetching local IP:', error);
        return null;
    }
}

let ws;
let isWebSocketOpen = false; // Bandera para controlar el estado del WebSocket
let messageCount = 0; // Contador de mensajes

async function initializeWebSocket() {
    const localIp = await getLocalIp();
    if (!localIp) {
        console.error('Unable to get local IP. WebSocket will not be initialized.');
        return;
    }
    
    ws = new WebSocket(`wss://${localIp}:8765`);

    ws.onopen = function() {
        console.log("WebSocket connection established");
        isWebSocketOpen = true; // Establecer la bandera a true cuando se abre la conexión
    };

    ws.onerror = function(error) {
        console.error("WebSocket error:", error);
    };

    ws.onclose = function() {
        console.log("WebSocket connection closed");
        isWebSocketOpen = false; // Establecer la bandera a false cuando se cierra la conexión
        // Intentar reconectar después de un tiempo
        setTimeout(initializeWebSocket, 5000);
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
