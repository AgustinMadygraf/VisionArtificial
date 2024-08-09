// static/js/videoManager.js
import ButtonManager from './buttonManager.js';

/**
 * Clase que gestiona el video desde la webcam.
 */
export default class VideoManager {
    constructor(testValue) {
        this.video = document.getElementById("vid");
        this.video.muted = true;
        this.buttonManager = new ButtonManager(this); // Inyección de dependencia
        this.testValue = testValue;
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
            navigator.mediaDevices
                .getUserMedia({
                    video: { facingMode: { exact: "environment" } },
                    audio: true,
                })
                .then((stream) => {
                    this.video.srcObject = stream;
                    this.video.addEventListener("loadedmetadata", () => {
                        this.video.play();
                        document.getElementById("but").classList.add("hidden");
                    });
                })
                .catch(() => {
                    navigator.mediaDevices
                        .getUserMedia({
                            video: { facingMode: "user" },
                            audio: true,
                        })
                        .then((stream) => {
                            this.video.srcObject = stream;
                            this.video.addEventListener("loadedmetadata", () => {
                                this.video.play();
                                document.getElementById("but").classList.add("hidden");
                            });
                        })
                        .catch(alert);
                });
        }
    }
}