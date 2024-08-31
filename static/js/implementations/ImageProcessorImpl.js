// static/js/implementations/ImageProcessorImpl.js
import ImageProcessingInterface from '../interfaces/imageProcessingInterface.js';

export default class ImageProcessorImpl extends ImageProcessingInterface {
    processImage(image) {
        // Implementación del procesamiento de imágenes
        console.log(image); // Uso de la variable 'image'
    }

    applyFilter(image, filter) {
        // Implementación de la aplicación de filtros
        console.log(image, filter); // Uso de las variables 'image' y 'filter'
    }
}