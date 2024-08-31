/*
static/js/videoManagerInitializer.js
Este archivo contiene la función initializeVideoManager, que se encarga de inicializar la clase VideoManager.
*/

import VideoManager from './videoManager.js';

/**
 * Inicializa la clase VideoManager, configura el stream de video y devuelve la instancia de VideoManager.
 * @returns {VideoManager} La instancia inicializada de VideoManager.
 */
export function initializeVideoManager() {
    console.log("Inicializando VideoManager...");
    const videoManager = new VideoManager();
    videoManager.initialize();
    videoManager.startVideoStream();
    return videoManager;
}