// static/js/webSocketManager.js
import { getLocalIp } from './utils/networkUtils.js';

let ws;
let isWebSocketOpen = false;
let messageCount = 0;

/**
 * Inicializa la conexión WebSocket.
 * Obtiene la IP local y establece una conexión WebSocket a esa IP.
 * Si la conexión falla, reintenta después de 5 segundos.
 */
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
        isWebSocketOpen = true;
    };

    ws.onerror = function(error) {
        console.error("WebSocket error:", error);
    };

    ws.onclose = function() {
        console.log("WebSocket connection closed");
        isWebSocketOpen = false;
        // Reintentar conexión después de 5 segundos
        setTimeout(initializeWebSocket, 5000);
    };
}

/**
 * Envía un mensaje a través del WebSocket si está abierto.
 * Sólo envía el mensaje si el contador de mensajes es múltiplo de 100.
 * @param {string} message - El mensaje a enviar.
 */
function sendWebSocketMessage(message) {
    messageCount++;

    if (messageCount % 100 === 0) {
        if (ws && ws.readyState === WebSocket.OPEN) {
            console.log(`Sending message: ${message}`);
            ws.send(message);
        } else {
            console.error("WebSocket is not open. Unable to send message.");
        }
    }
}

export { initializeWebSocket, sendWebSocketMessage };
