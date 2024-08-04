// static/js/script.js
import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor.js';
import DOMUpdater from './domUpdater.js';
import { initializeWebSocket, sendWebSocketMessage } from './webSocketManager.js';

const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;
const refreshInterval = 20;

function adjustLayoutForOrientation() {
    const container = document.getElementById('container');
    if (window.innerWidth > window.innerHeight) {
        container.classList.add('landscape');
    } else {
        container.classList.remove('landscape');
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
    videoManager.startVideoStream();

    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
    }, refreshInterval);

    adjustLayoutForOrientation();
    window.addEventListener('resize', adjustLayoutForOrientation);
});
