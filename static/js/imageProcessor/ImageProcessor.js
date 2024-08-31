/*
static/js/imageProcessor/ImageProcessor.js
Este archivo contiene la clase ImageProcessor, que se encarga de 
procesar las imágenes capturadas desde la webcam.
*/

export default class ImageProcessor {
    /**
     * Constructor de la clase ImageProcessor.
     * @param {number} secs - Segundos para la captura de la imagen.
     * @param {number} halfEvalHeight - Altura de evaluación a la mitad.
     * @param {number} halfEvalWidth - Ancho de evaluación a la mitad.
     * @param {Object} canvasUtils - Utilidades para el manejo del canvas.
     * @param {Object} webSocketUtils - Utilidades para el manejo de WebSocket.
     * @param {Object} strategy - Estrategia de procesamiento de imágenes.
     */
    constructor(secs, halfEvalHeight, halfEvalWidth, canvasUtils, webSocketUtils, strategy) {
        this.secs = secs;
        this.halfEvalHeight = halfEvalHeight;
        this.halfEvalWidth = halfEvalWidth;
        this.canvasUtils = canvasUtils;
        this.webSocketUtils = webSocketUtils;
        this.strategy = strategy;
    }

    /**
     * Captura una imagen del video.
     * @param {HTMLVideoElement} video - Elemento de video del cual se capturará la imagen.
     * @returns {HTMLImageElement} - Imagen capturada del video.
     */
    pickImage(video) {
        this.getVideoImage(video, this.secs, this.printImageDetails.bind(this));
        const vid = this.videoToImg(video);
        return vid.image;
    }

    /**
     * Convierte un elemento de video en una imagen.
     * @param {HTMLVideoElement} video - Elemento de video a convertir.
     * @returns {Object} - Objeto que contiene la imagen capturada.
     */
    videoToImg(video) {
        const canvas = document.createElement('canvas');
        canvas.height = video.videoHeight;
        canvas.width = video.videoWidth;
        const ctx = canvas.getContext('2d', { willReadFrequently: true });
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        this.strategy.process(canvas);
        const img = new Image();
        img.src = canvas.toDataURL();
        return { image: img };
    }

    /**
     * Captura una imagen del video en un tiempo específico.
     * @param {HTMLVideoElement} video - Elemento de video del cual se capturará la imagen.
     * @param {number|function} secs - Segundos para la captura de la imagen o función que retorna los segundos.
     * @param {function} callback - Función de callback que se ejecutará después de capturar la imagen.
     */
    getVideoImage(video, secs, callback) {
        video.onloadedmetadata = () => {
            if (typeof secs === 'function') {
                secs = secs(this.duration);
            }
            video.currentTime = Math.min(Math.max(0, (secs < 0 ? video.duration : 0) + secs), video.duration);
            const vid = this.videoToImg(video);
            callback(vid, video.currentTime, undefined);
        };

        video.onseeked = () => {
            callback(undefined, video.currentTime, undefined);
        };

        video.onerror = () => {
            callback(undefined, undefined, undefined);
        };
    }

    /**
     * Imprime los detalles de la imagen capturada.
     * @param {Object} vid - Objeto que contiene la imagen capturada.
     * @param {number} currentTime - Tiempo actual del video.
     */
    printImageDetails(vid, currentTime) {
        this.webSocketUtils.sendWebSocketMessage(`Image details: width=${vid.image.width}, height=${vid.image.height}, time=${currentTime}`);
    }
}