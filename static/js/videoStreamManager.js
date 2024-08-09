// static/js/videoStreamManager.js

export default class VideoStreamManager {
    constructor(videoElement) {
        this.videoElement = videoElement;
    }

    async startStream() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            this.videoElement.srcObject = stream;
            this.videoElement.play();
        } catch (error) {
            console.error("Error starting video stream:", error);
            throw error;
        }
    }

    stopStream() {
        const stream = this.videoElement.srcObject;
        if (stream) {
            const tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
            this.videoElement.srcObject = null;
        }
    }
}