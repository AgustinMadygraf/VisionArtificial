/*
static/js/videoManagerInitializer.js
Este archivo contiene la función initializeVideoManager, que se encarga de inicializar la clase VideoManager.
*/

import VideoManager from './videoManager.js';

export function initializeVideoManager() {
    const videoManager = new VideoManager();
    videoManager.initialize();
    videoManager.startVideoStream();
    return videoManager;
}