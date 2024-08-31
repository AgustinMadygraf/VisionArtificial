// static/js/imageProcessor/ImageProcessor.js

export default class ImageProcessor {
    constructor(secs, halfEvalHeight, halfEvalWidth, canvasUtils, webSocketUtils, strategy) {
        this.secs = secs;
        this.halfEvalHeight = halfEvalHeight;
        this.halfEvalWidth = halfEvalWidth;
        this.canvasUtils = canvasUtils;
        this.webSocketUtils = webSocketUtils;
        this.strategy = strategy;
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
        this.strategy.process(canvas);
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
            callback(vid, video.currentTime, undefined);
        };

        video.onseeked = () => {
            callback(undefined, video.currentTime, undefined);
        };

        video.onerror = () => {
            callback(undefined, undefined, undefined);
        };
    }

    printImageDetails(vid, currentTime) {
        this.webSocketUtils.sendWebSocketMessage(`Image details: width=${vid.image.width}, height=${vid.image.height}, time=${currentTime}`);
    }
}