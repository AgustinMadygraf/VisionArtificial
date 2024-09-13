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
        this.kernel = [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ]; // Kernel por defecto
    }

    /**
     * Configura el kernel (núcleo) para el filtro.
     * @param {number[][]} newKernel - El nuevo kernel de 3x3.
     */
    setKernel(newKernel) {
        if (newKernel.length === 3 && newKernel.every(row => row.length === 3)) {
            this.kernel = newKernel;
        } else {
            throw new Error("El kernel debe ser una matriz de 3x3.");
        }
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
        
        // Aplica el filtro de blanco y negro
        this.applyBlackAndWhiteFilter(ctx, canvas.width, canvas.height);

        // Aplica el filtro basado en el núcleo
        this.applyKernelFilter(ctx, canvas.width, canvas.height);

        this.strategy.process(canvas);
        const img = new Image();
        img.src = canvas.toDataURL();
        return { image: img };
    }

    /**
     * Aplica un filtro de blanco y negro en el canvas.
     * @param {CanvasRenderingContext2D} ctx - Contexto del canvas.
     * @param {number} width - Ancho del canvas.
     * @param {number} height - Altura del canvas.
     */
    applyBlackAndWhiteFilter(ctx, width, height) {
        const imageData = ctx.getImageData(0, 0, width, height);
        const data = imageData.data;
        for (let i = 0; i < data.length; i += 4) {
            const avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
            data[i] = avg; // Red
            data[i + 1] = avg; // Green
            data[i + 2] = avg; // Blue
        }
        ctx.putImageData(imageData, 0, 0);
    }

    /**
     * Aplica un filtro basado en un núcleo (kernel) en el canvas.
     * @param {CanvasRenderingContext2D} ctx - Contexto del canvas.
     * @param {number} width - Ancho del canvas.
     * @param {number} height - Altura del canvas.
     */
    applyKernelFilter(ctx, width, height) {
        const imageData = ctx.getImageData(0, 0, width, height);
        const data = imageData.data;
        const result = new Uint8ClampedArray(data.length);
        const side = 3;
        const halfSide = Math.floor(side / 2);

        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                let r = 0, g = 0, b = 0, a = 0;
                for (let ky = 0; ky < side; ky++) {
                    for (let kx = 0; kx < side; kx++) {
                        const scy = y + ky - halfSide;
                        const scx = x + kx - halfSide;
                        if (scy >= 0 && scy < height && scx >= 0 && scx < width) {
                            const srcOffset = (scy * width + scx) * 4;
                            const wt = this.kernel[ky][kx];
                            r += data[srcOffset] * wt;
                            g += data[srcOffset + 1] * wt;
                            b += data[srcOffset + 2] * wt;
                            a += data[srcOffset + 3] * wt;
                        }
                    }
                }
                const dstOffset = (y * width + x) * 4;
                result[dstOffset] = r;
                result[dstOffset + 1] = g;
                result[dstOffset + 2] = b;
                result[dstOffset + 3] = a;
            }
        }
        ctx.putImageData(new ImageData(result, width, height), 0, 0);
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