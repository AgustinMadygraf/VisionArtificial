/*
 static/js/videoStreamManager.js
Este archivo contiene la clase VideoStreamManager, que se encarga de gestionar el stream de video.
 */
/**
 * Clase que gestiona el stream de video.
 */
export default class VideoStreamManager {
    constructor(videoElement) {
        this.videoElement = videoElement;
    }

    async startStream() {
        try {
            const devices = await navigator.mediaDevices.enumerateDevices();
            const videoDevices = devices.filter(device => device.kind === 'videoinput');
            let constraints = { video: { facingMode: { exact: "environment" } } };

            if (videoDevices.length > 0) {
                try {
                    const stream = await navigator.mediaDevices.getUserMedia(constraints);
                    this.videoElement.srcObject = stream;
                    this.videoElement.play();
                } catch (error) {
                    console.warn("No se pudo acceder a la cámara trasera, utilizando la cámara frontal.", error);
                    constraints = { video: { facingMode: "user" } };
                    const stream = await navigator.mediaDevices.getUserMedia(constraints);
                    this.videoElement.srcObject = stream;
                    this.videoElement.play();
                }
            } else {
                console.error("No se encontraron dispositivos de video.");
            }
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