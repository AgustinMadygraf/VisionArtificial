// static/js/imageProcessor/deviceDetectionColorFilter.js
import ColorFilter from './ColorFilter.js';

async function detectDeviceAndApplyFilter(videoElement) {
    const colorFilter = new ColorFilter();

    // Detectar el dispositivo
    const userAgent = navigator.userAgent.toLowerCase();
    if (userAgent.includes('iphone') || userAgent.includes('ipad')) {
        colorFilter.setCameraCoefficient(5); // Coeficiente para dispositivos iOS
    } else if (userAgent.includes('android')) {
        colorFilter.setCameraCoefficient(3); // Coeficiente para dispositivos Android
    } else {
        colorFilter.setCameraCoefficient(4); // Coeficiente por defecto para otros dispositivos
    }

    // Aplicar el filtro al video
    const canvas = document.createElement('canvas');
    canvas.height = videoElement.videoHeight;
    canvas.width = videoElement.videoWidth;
    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

    colorFilter.applyColorFilter(ctx, canvas.width, canvas.height);

    const img = new Image();
    img.src = canvas.toDataURL();
    return { image: img };
}

// Uso del código
const videoElement = document.getElementById('vid');
detectDeviceAndApplyFilter(videoElement);