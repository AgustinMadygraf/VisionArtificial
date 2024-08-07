// static/js/imageProcessor/ImageProcessor.js
import { drawVerticalLine, drawHorizontalLine, drawCenterRuler } from '../utils/canvasUtils.js';
import { sendWebSocketMessage } from './webSocketUtils.js';

export default class ImageProcessor {
    constructor(secs, halfEvalHeight, halfEvalWidth, canvasUtils, webSocketUtils) {
        this.secs = secs;
        this.halfEvalHeight = halfEvalHeight;
        this.halfEvalWidth = halfEvalWidth;
        this.canvasUtils = canvasUtils;
        this.webSocketUtils = webSocketUtils;
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
        this.webSocketUtils.sendWebSocketMessage(`Image details: width=${vid.image.width}, height=${vid.image.height}, time=${currentTime}`);
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

        this.canvasUtils.drawVerticalLine(context, pos, 'yellow');

        const centerX = canvas.width / 2;
        this.canvasUtils.drawVerticalLine(context, centerX, 'red');

        const centerY = canvas.height / 2;
        this.canvasUtils.drawHorizontalLine(context, centerY, 'green');

        this.canvasUtils.drawCenterRuler(context, 'blue', 10, 10);

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

        this.webSocketUtils.sendWebSocketMessage(`Drawing line in position ${deviation}`);
    }
}

