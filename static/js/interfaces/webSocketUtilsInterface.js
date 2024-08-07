// static/js/interfaces/WebSocketUtilsInterface.js
export default class WebSocketUtilsInterface {
    initializeWebSocket() {
        throw new Error('You have to implement the method initializeWebSocket!');
    }
    sendWebSocketMessage(message) {
        throw new Error('You have to implement the method sendWebSocketMessage!');
    }
}
