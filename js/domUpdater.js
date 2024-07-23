// js/domUpdater.js
export default class DOMUpdater {
    updateCanvas(img) {
        const imgCanvas = document.getElementById("image-canvas");
        imgCanvas.replaceChildren(img);
    }
}
