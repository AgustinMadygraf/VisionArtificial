// js/domUpdater.js

/**
 * Clase que gestiona las actualizaciones del DOM.
 */
export default class DOMUpdater {
    /**
     * Actualiza el contenido del canvas con una nueva imagen.
     * @param {HTMLImageElement} img - La imagen que se va a colocar en el canvas.
     */
    updateCanvas(img) {
        const imgCanvas = document.getElementById("image-canvas");
        imgCanvas.replaceChildren(img); // Reemplaza los hijos actuales del canvas con la nueva imagen
    }
}
