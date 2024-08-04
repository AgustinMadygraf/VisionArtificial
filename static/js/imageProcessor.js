// static/js/imageProcessor.js
import { drawVerticalLine, drawHorizontalLine, drawCenterRuler } from './canvasUtils.js';
import { sendWebSocketMessage } from './script.js';

export default class ImageProcessor {
    constructor(secs, halfEvalHeight, halfEvalWidth) {
        this.secs = secs;
        this.halfEvalHeight = halfEvalHeight;
        this.halfEvalWidth = halfEvalWidth;
    }

    pickImage(video) {
        this.getVideoImage(video, this.secs, this.printImageDetails.bind(this));
        const vid = this.videoToImg(video);
        return vid.image;
    }

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

    printImageDetails(vid, currentTime, e) {
        sendWebSocketMessage(`Image details: width=${vid.image.width}, height=${vid.image.height}, time=${currentTime}`);
    }

    putLineInCanvas(canvas) {
        const pos = this.maxVerticalJumpPixelPos(canvas);
        this.vertLineInCanvas(canvas, pos.pos);
    }

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

    vertLineInCanvas(canvas, pos) {
        const context = canvas.getContext('2d');

        // Dibujar la línea vertical amarilla
        drawVerticalLine(context, pos, 'yellow');

        // Dibujar la línea vertical roja en el centro del canvas
        const centerX = canvas.width / 2;
        drawVerticalLine(context, centerX, 'red');

        // Dibujar la línea horizontal verde en el centro del canvas
        const centerY = canvas.height / 2;
        drawHorizontalLine(context, centerY, 'green');

        // Dibujar la regla horizontal en el centro del canvas
        drawCenterRuler(context, 'blue', 10, 10);

        // Calcular y mostrar el desvío
        const deviation = pos - centerX;
        context.fillStyle = 'white'; // Color del texto
        context.font = '20px Arial'; // Fuente del texto
        context.fillText(`Desvío: ${deviation}px`, 10, 30); // Mostrar el desvío en la esquina superior izquierda

        // Dibujar línea que conecta las dos posiciones
        context.strokeStyle = 'white'; // Color de la línea de desvío
        context.lineWidth = 1; // Ancho de la línea de desvío
        context.beginPath();
        context.moveTo(centerX, centerY);
        context.lineTo(pos, centerY);
        context.stroke();

        sendWebSocketMessage(`Drawing line in position ${deviation}`);
    }
}
