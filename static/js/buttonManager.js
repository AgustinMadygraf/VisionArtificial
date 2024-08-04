// js/buttonManager.js

/**
 * Clase que gestiona los eventos de botones.
 */
export default class ButtonManager {
    constructor(videoManager) {
        this.videoManager = videoManager;
    }

    initialize() {
        const but = document.getElementById("but");
        but.addEventListener("click", () => this.videoManager.startVideoStream());
    }
}
