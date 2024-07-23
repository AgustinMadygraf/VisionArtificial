// js/imageProcessor.js
import { drawVerticalLine, drawHorizontalLine } from './canvasUtils.js';

export default class ImageProcessor {
    constructor(secs, halfEvalHeight, halfEvalWidth) {
        this.secs = secs;
        this.halfEvalHeight = halfEvalHeight;
        this.halfEvalWidth = halfEvalWidth;
    }

    pickImage(video) {
        this.getVideoImage(video, this.secs, this.printImageDetails.bind(this));
        const vid = this.videoToImg(video);
        console.log("image to convert dimensions:", vid.image);
        console.log("image data", vid.data);
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
            console.log("currentTime", video.currentTime);
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
        console.log("printing:", this, vid.image.width, vid.image.height, currentTime, e);
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
        console.log("Drawing line in position", pos);
        const context = canvas.getContext('2d');

        // Dibujar la línea vertical amarilla
        drawVerticalLine(context, pos, 'yellow');

        // Dibujar la línea vertical roja en el centro del canvas
        const centerX = canvas.width / 2;
        drawVerticalLine(context, centerX, 'red');

        // Dibujar la línea horizontal verde en el centro del canvas
        const centerY = canvas.height / 2;
        drawHorizontalLine(context, centerY, 'green');
    }
}
