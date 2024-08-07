// static/js/implementations/WebSocketUtilsImpl.js
import WebSocketUtilsInterface from '../interfaces/webSocketUtilsInterface.js';
import { sendWebSocketMessage } from '../imageProcessor/webSocketUtils.js';

export default class WebSocketUtilsImpl extends WebSocketUtilsInterface {
    initializeWebSocket() {
        // Implementa la inicialización del WebSocket si es necesario
    }
    sendWebSocketMessage(message) {
        sendWebSocketMessage(message);
    }
}
