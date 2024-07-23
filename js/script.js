// js/script.js

//import VideoManager from './videoManager.js';

const secs = 3;
const halfEvalHeight = 10;
const halfEvalWidth = 200;

document.addEventListener("DOMContentLoaded", () => {
    const videoManager = new VideoManager();
    const imageProcessor = new ImageProcessor();
    const domUpdater = new DOMUpdater();

    videoManager.initialize();

    setInterval(() => {
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
    }, 30);
});

class VideoManager {
    constructor() {
        this.video = document.getElementById("vid");
        this.video.muted = true;
    }

    initialize() {
        const but = document.getElementById("but");
        but.addEventListener("click", () => this.startVideoStream());
    }

    startVideoStream() {
        navigator.mediaDevices
            .getUserMedia({
                video: true,
                audio: true,
            })
            .then((stream) => {
                this.video.srcObject = stream;
                this.video.addEventListener("loadedmetadata", () => {
                    this.video.play();
                });
            })
            .catch(alert);
    }
}

class ImageProcessor {
    pickImage(video) {
        this.getVideoImage(video, secs, this.printImageDetails);
        const vid = this.videoToImg(video);
        console.log("image to convert dimensions:", vid.image);
        console.log("image data", vid.data);
        return vid.image;
    }

    videoToImg(video) {
        const canvas = document.createElement('canvas');
        canvas.height = video.videoHeight;
        canvas.width = video.videoWidth;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        this.putLineInCanvas(canvas);
        const img = new Image();
        img.src = canvas.toDataURL();
        return { image: img };
    }

    getVideoImage(video, secs, callback) {
        video.onloadedmetadata = function () {
            if (typeof secs === 'function') {
                secs = secs(this.duration);
            }
            this.currentTime = Math.min(Math.max(0, (secs < 0 ? this.duration : 0) + secs), this.duration);
            console.log("currentTime", this.currentTime);
            const vid = videoToImg(video);
            const img = vid.image;
            callback.call(this, vid, this.currentTime, undefined);
        };

        video.onseeked = function (e) {
            callback.call(this, undefined, this.currentTime, e);
        };

        video.onerror = function (e) {
            callback.call(this, undefined, undefined, e);
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
        const ctx = canvas.getContext('2d');

        const heightMid = Math.floor(canvas.height / 2);
        const heightCotas = { lo: heightMid - halfEvalHeight, hi: heightMid + halfEvalHeight };

        const widthMid = Math.floor(canvas.width / 2);
        const widthCotas = { lo: widthMid - halfEvalWidth, hi: widthMid + halfEvalWidth };

        const vertAdd = [];
        const horizDiff = [];
        let maxDiff = { diff: -256 * 3 * 2 * halfEvalHeight, pos: 0 };

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
        context.strokeStyle = 'yellow'; // Color of the line
        context.lineWidth = 2; // Width of the line

        // Draw the vertical line
        context.beginPath();
        context.moveTo(pos, 0);
        context.lineTo(pos, canvas.height);
        context.stroke();

        const ctx = canvas.getContext('2d'); // Obtiene el contexto 2D del canvas
        const centerX = canvas.width / 2; // Calcula el centro del canvas en el eje X

        ctx.strokeStyle = 'red'; // Establece el color de la línea a rojo
        ctx.lineWidth = 2; // Establece el ancho de la línea a 2 píxeles

        // Dibuja la línea vertical
        ctx.beginPath(); // Comienza un nuevo camino
        ctx.moveTo(centerX, 0); // Mueve el cursor al inicio de la línea (centro superior del canvas)
        ctx.lineTo(centerX, canvas.height); // Dibuja una línea hasta el centro inferior del canvas
        ctx.stroke(); // Aplica el trazo al camino, dibujando la línea
    }
}

class DOMUpdater {
    updateCanvas(img) {
        const imgCanvas = document.getElementById("image-canvas");
        imgCanvas.replaceChildren(img);
    }
}
