/*
js/buttonManager.js
Este archivo contiene la clase ButtonManager, que se encarga de gestionar los eventos de botones.
*/

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
