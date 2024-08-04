// static/js/imageProcessor.js
import { drawVerticalLine, drawHorizontalLine, drawCenterRuler } from './utils/canvasUtils.js';
import { sendWebSocketMessage } from './webSocketManager.js';

/**
 * Clase que gestiona el procesamiento de imágenes desde un video.
 */
export default class ImageProcessor {
    /**
     * Constructor de ImageProcessor.
     * @param {number} secs - Número de segundos para la evaluación de la imagen.
     * @param {number} halfEvalHeight - La mitad de la altura de la evaluación de la imagen.
     * @param {number} halfEvalWidth - La mitad del ancho de la evaluación de la imagen.
     */
    constructor(secs, halfEvalHeight, halfEvalWidth) {
        this.secs = secs;
        this.halfEvalHeight = halfEvalHeight;
        this.halfEvalWidth = halfEvalWidth;
    }

    /**
     * Selecciona una imagen del video.
     * @param {HTMLVideoElement} video - El elemento de video.
     * @returns {HTMLImageElement} - La imagen seleccionada.
     */
    pickImage(video) {
        this.getVideoImage(video, this.secs, this.printImageDetails.bind(this));
        const vid = this.videoToImg(video);
        return vid.image;
    }

    /**
     * Convierte un frame del video en una imagen.
     * @param {HTMLVideoElement} video - El elemento de video.
     * @returns {Object} - Un objeto que contiene la imagen.
     */
    videoToImg(video) {
        const canvas = document.createElement('canvas');
        canvas.height = video.videoHeight;
        canvas.width = video.videoWidth;
        const ctx = canvas.getContext('2d', { willReadFrequently: true });
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        this.putLineInCanvas(canvas);
        const img = new Image();
        img.src = canvas.toDataURL();
        return { image: img };
    }

    /**
     * Obtiene una imagen del video en el tiempo especificado.
     * @param {HTMLVideoElement} video - El elemento de video.
     * @param {number|Function} secs - El número de segundos o una función para calcular el tiempo.
     * @param {Function} callback - La función de callback.
     */
    getVideoImage(video, secs, callback) {
        video.onloadedmetadata = () => {
            if (typeof secs === 'function') {
                secs = secs(this.duration);
            }
            video.currentTime = Math.min(Math.max(0, (secs < 0 ? video.duration : 0) + secs), video.duration);
            const vid = this.videoToImg(video);
            const img = vid.image;
            callback(vid, video.currentTime, undefined);
        };

        video.onseeked = (e) => {
            callback(undefined, video.currentTime, e);
        };

        video.onerror = (e) => {
            callback(undefined, undefined, e);
        };
    }

    /**
     * Imprime los detalles de la imagen en el WebSocket.
     * @param {Object} vid - El objeto que contiene la imagen.
     * @param {number} currentTime - El tiempo actual del video.
     * @param {Event} e - El evento.
     */
    printImageDetails(vid, currentTime, e) {
        sendWebSocketMessage(`Image details: width=${vid.image.width}, height=${vid.image.height}, time=${currentTime}`);
    }

    /**
     * Dibuja líneas en el canvas basado en la posición de la mayor diferencia vertical.
     * @param {HTMLCanvasElement} canvas - El elemento canvas.
     */
    putLineInCanvas(canvas) {
        const pos = this.maxVerticalJumpPixelPos(canvas);
        this.vertLineInCanvas(canvas, pos.pos);
    }

    /**
     * Encuentra la posición del mayor salto vertical en los píxeles del canvas.
     * @param {HTMLCanvasElement} canvas - El elemento canvas.
     * @returns {Object} - Un objeto que contiene la posición y la diferencia máxima.
     */
    maxVerticalJumpPixelPos(canvas) {
        const ctx = canvas.getContext('2d', { willReadFrequently: true });

        const heightMid = Math.floor(canvas.height / 2);
        const heightCotas = { lo: heightMid - this.halfEvalHeight, hi: heightMid + this.halfEvalHeight };

        const widthMid = Math.floor(canvas.width / 2);
        const widthCotas = { lo: widthMid - this.halfEvalWidth, hi: widthMid + this.halfEvalWidth };

        const vertAdd = [];
        const horizDiff = [];
        let maxDiff = { diff: -256 * 3 * 2 * this.halfEvalHeight, pos: 0 };

        for (let x = widthCotas.lo; x < widthCotas.hi; x++) {
            const arr_x = x - widthCotas.lo;
            vertAdd.push(0);
            for (let y = heightCotas.lo; y < heightCotas.hi; y++) {
                const point = ctx.getImageData(x, y, 1, 1).data;
                vertAdd[arr_x] = vertAdd[arr_x] + (point[0] + point[1] + point[2]);
            }
            if (arr_x > 1) {
                horizDiff.push(vertAdd[arr_x] - vertAdd[arr_x - 1]);
                if (horizDiff[arr_x - 2] > maxDiff.diff) {
                    maxDiff.pos = x - 1;
                    maxDiff.diff = horizDiff[arr_x - 2];
                }
            }
        }
        return maxDiff;
    }

    /**
     * Dibuja varias líneas en el canvas.
     * @param {HTMLCanvasElement} canvas - El elemento canvas.
     * @param {number} pos - La posición de la línea vertical amarilla.
     */
    vertLineInCanvas(canvas, pos) {
        const context = canvas.getContext('2d');

        drawVerticalLine(context, pos, 'yellow');

        const centerX = canvas.width / 2;
        drawVerticalLine(context, centerX, 'red');

        const centerY = canvas.height / 2;
        drawHorizontalLine(context, centerY, 'green');

        drawCenterRuler(context, 'blue', 10, 10);

        const deviation = pos - centerX;
        context.fillStyle = 'white';
        context.font = '20px Arial';
        context.fillText(`Desvío: ${deviation}px`, 10, 30);

        context.strokeStyle = 'white';
        context.lineWidth = 1;
        context.beginPath();
        context.moveTo(centerX, centerY);
        context.lineTo(pos, centerY);
        context.stroke();

        sendWebSocketMessage(`Drawing line in position ${deviation}`);
    }
}
