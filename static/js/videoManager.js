// js/videoManager.js

/**
 * Clase que gestiona el video desde la webcam.
 */
export default class VideoManager {
    /**
     * Constructor de VideoManager. 
     * Inicializa el elemento de video y lo silencia.
     */
    constructor() {
        this.video = document.getElementById("vid");
        this.video.muted = true;
    }

    /**
     * Inicializa los event listeners necesarios.
     * Añade un event listener al botón para iniciar la transmisión de video.
     */
    initialize() {
        const but = document.getElementById("but");
        but.addEventListener("click", () => this.startVideoStream());
    }

    /**
     * Inicia la transmisión de video desde la webcam.
     * Primero intenta obtener la cámara del entorno y, si falla, recurre a la cámara del usuario.
     */
    startVideoStream() {
        navigator.mediaDevices
            .getUserMedia({
                video: { facingMode: { exact: "environment" } }, // Intenta usar la cámara del entorno
                audio: true,
            })
            .then((stream) => {
                this.video.srcObject = stream;
                this.video.addEventListener("loadedmetadata", () => {
                    this.video.play();
                    document.getElementById("but").classList.add("hidden");
                });
            })
            .catch(() => {
                // Si la cámara del entorno no está disponible, usar la cámara del usuario
                navigator.mediaDevices
                    .getUserMedia({
                        video: { facingMode: "user" }, // Usa la cámara del usuario como alternativa
                        audio: true,
                    })
                    .then((stream) => {
                        this.video.srcObject = stream;
                        this.video.addEventListener("loadedmetadata", () => {
                            this.video.play();
                            document.getElementById("but").classList.add("hidden");
                        });
                    })
                    .catch(alert); // Muestra una alerta si no se puede acceder a ninguna cámara
            });
    }
}