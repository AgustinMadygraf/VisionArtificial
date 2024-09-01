/*
static/js/videoManager.js
Este archivo contiene la clase VideoManager, que se encarga de gestionar el video desde la webcam.
*/

import ButtonManager from './buttonManager.js';
import VideoStreamManager from './videoStreamManager.js';

/**
 * Clase que gestiona el video desde la webcam.
 */
export default class VideoManager {
    constructor() {
        this.video = document.getElementById("vid");
        this.video.muted = true;
        this.buttonManager = new ButtonManager(this);
        this.videoStreamManager = new VideoStreamManager(this.video);
    }

    /**
     * Initializes the video manager.
     */
    initialize() {
        this.buttonManager.initialize();
        console.log("VideoManager inicializado.");
    }

    /**
     * Starts the video stream.
     * 
     * @returns {Promise<void>} A promise that resolves when the video stream is started successfully.
     */
    startVideoStream() {
            this.videoStreamManager.startStream()
                .then(() => {
                    document.getElementById("but").classList.add("hidden");
                })
                .catch(alert);
                console.log("Stream de video iniciado.");
        }
    }

