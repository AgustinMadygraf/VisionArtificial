// static/js/main.js
import VideoManager from './videoManager.js';
import ImageProcessor from './imageProcessor.js';
import DOMUpdater from './domUpdater.js';
import { initializeWebSocket } from './webSocketManager.js';
import { adjustLayoutForOrientation } from './uiManager.js';

const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;
const refreshInterval = 20;

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
