// js/videoManager.js
export default class VideoManager {
    constructor() {
        this.video = document.getElementById("vid");
        this.video.muted = true;
    }

    initialize() {
        const but = document.getElementById("but");
        but.addEventListener("click", () => this.startVideoStream());
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
                // If the environment camera is not available, fallback to the user camera
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