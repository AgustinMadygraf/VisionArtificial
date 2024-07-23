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
                video: true,
                audio: true,
            })
            .then((stream) => {
                this.video.srcObject = stream;
                this.video.addEventListener("loadedmetadata", () => {
                    this.video.play();
                });
            })
            .catch(alert);
    }
}
