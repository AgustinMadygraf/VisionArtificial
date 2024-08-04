// static/js/script.js
import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor.js';
import DOMUpdater from './domUpdater.js';
import { getLocalIp } from './networkUtils.js';

const secs = 3;             // Obtener el número de segundos para la evaluación de la imagen
const halfEvalHeight = 10;  // Obtener la mitad de la altura de la evaluación de la imagen
const halfEvalWidth = 200;  // Obtener la mitad del ancho de la evaluación de la imagen
const refreshInterval = 20; // Obtener el tiempo de refresco de la URL, 20 milisegundos

let ws;
let isWebSocketOpen = false; // Bandera para controlar el estado del WebSocket
let messageCount = 0; // Contador de mensajes

async function initializeWebSocket() {
    console.log("Initializing WebSocket...");
    const localIp = await getLocalIp();
    if (!localIp) {
        console.error('Unable to get local IP. WebSocket will not be initialized.');
        return;
    }
    
    console.log(`Local IP obtained: ${localIp}`);
    const wsUrl = `ws://${localIp}:8765`;
    console.log(`Connecting to WebSocket at ${wsUrl}`);
    ws = new WebSocket(wsUrl);

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
            console.log(`Sending message: ${message}`);
            ws.send(message);
        } else {
            console.error("WebSocket is not open. Unable to send message.");
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");
    initializeWebSocket();
    const videoManager = new VideoManager();
    const imageProcessor = new ImageProcessor(secs, halfEvalHeight, halfEvalWidth);
    const domUpdater = new DOMUpdater();

    console.log("Initializing VideoManager...");
    videoManager.initialize();

    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
    }, refreshInterval);
});
