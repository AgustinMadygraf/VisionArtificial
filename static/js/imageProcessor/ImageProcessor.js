/*
static/js/imageProcessor/ImageProcessor.js
Este archivo contiene la clase ImageProcessor, que se encarga de 
procesar las imágenes capturadas desde la webcam.
*/

import KernelProcessor from './KernelProcessor.js';
import ColorFilter from './ColorFilter.js';

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
        this.kernelProcessor = new KernelProcessor();
        this.colorFilter = new ColorFilter(); 
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
     * Aplica un filtro de blanco y negro en el canvas.
     * Si el color es marrón, se convierte a escala de grises.
     * Si no es marrón, se convierte a blanco.
     * @param {CanvasRenderingContext2D} ctx - Contexto del canvas.
     * @param {number} width - Ancho del canvas.
     * @param {number} height - Altura del canvas.
     */
    applyBlackAndWhiteFilter(ctx, width, height) {
        const imageData = ctx.getImageData(0, 0, width, height);
        const data = imageData.data;
        const r_set = 190;
        const g_set = 144;
        const b_set = 144;
        const tolerancia_r = 128;
        const tolerancia_g = 128;
        const tolerancia_b = 128;
        for (let i = 0; i < data.length; i += 4) {
            const r = data[i];
            const g = data[i + 1];
            const b = data[i + 2];

            // Verificar si el color es marrón
            if (    r >= r_set -tolerancia_r   && r <= r_set + tolerancia_r 
                &&  g >= g_set -tolerancia_g   && g <= g_set + tolerancia_g 
                &&  b >= b_set -tolerancia_b   && b <= b_set + tolerancia_b ) {
                const avg = (r + g + b) / 3;
                data[i] = r; // Red
                data[i + 1] = g; // Green
                data[i + 2] = b; // Blue
            } else {
                data[i] = 0; // Red
                data[i + 1] = 255; // Green
                data[i + 2] = 0; // Blue
            }
        }
        ctx.putImageData(imageData, 0, 0);
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
        
        // Aplica el filtro de color utilizando la clase ColorFilter
        this.colorFilter.applyColorFilter(ctx, canvas.width, canvas.height);

        // Aplica el filtro basado en el núcleo
        this.kernelProcessor.applyKernelFilter(ctx, canvas.width, canvas.height);

        this.strategy.process(canvas);
        const img = new Image();
        img.src = canvas.toDataURL();
        return { image: img };
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