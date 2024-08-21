// static/js/main_photo.js
import DOMUpdater from './domUpdater.js';
import ImageProcessor from './imageProcessor/ImageProcessor.js';

document.getElementById('but').addEventListener('click', () => {
    const imgElement = document.getElementById('vid');
    const domUpdater = new DOMUpdater();
    const imageProcessor = new ImageProcessor(/* parámetros necesarios */);

    // Procesar la imagen
    const processedImage = imageProcessor.videoToImg(imgElement).image;

    // Actualizar el canvas con la imagen procesada
    domUpdater.updateCanvas(processedImage);
});