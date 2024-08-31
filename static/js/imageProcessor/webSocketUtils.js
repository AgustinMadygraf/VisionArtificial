// static/js/imageProcessor/webSocketUtils.js

import { getLocalIp } from '../utils/networkUtils.js';

let ws;
let messageCount = 0;

export async function initializeWebSocket() {
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
    };

    ws.onerror = function(error) {
        console.error("WebSocket error:", error);
    };

    ws.onclose = function() {
        console.log("WebSocket connection closed");
        // Reintentar conexión después de 5 segundos
        setTimeout(initializeWebSocket, 5000);
    };
}

export function sendWebSocketMessage(message) {
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