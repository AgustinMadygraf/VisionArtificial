import ButtonManager from './buttonManager.js';
import VideoStreamManager from './videoStreamManager.js';

// static/js/videoManager.js

/**
 * Clase que gestiona el video desde la webcam.
 */
export default class VideoManager {
    constructor(testValue) {
        this.video = document.getElementById("vid");
        this.video.muted = true;
        this.buttonManager = new ButtonManager(this); // Inyección de dependencia
        this.testValue = testValue;
        this.videoStreamManager = new VideoStreamManager(this.video);
    }

    initialize() {
        this.buttonManager.initialize();
    }

    startVideoStream() {
        if (this.testValue === 'True') {
            console.log("Test value is True, setting video source to 'test.jpeg'");
            this.video.src = './static/test.jpeg';
            this.video.style.display = 'block';
        } else {
            console.log("Test value is not True, starting video stream from device");
            this.videoStreamManager.startStream()
                .then(() => {
                    document.getElementById("but").classList.add("hidden");
                })
                .catch(alert);
        }
    }
}
