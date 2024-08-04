// js/videoManager.js
import ButtonManager from './buttonManager.js';

/**
 * Clase que gestiona el video desde la webcam.
 */
export default class VideoManager {
    constructor() {
        this.video = document.getElementById("vid");
        this.video.muted = true;
        this.buttonManager = new ButtonManager(this); // Inyección de dependencia
    }

    initialize() {
        this.buttonManager.initialize();
    }

    startVideoStream() {
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