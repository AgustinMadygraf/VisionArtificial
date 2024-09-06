/* 
static/js/main_camara.js
Este archivo contiene el código principal de la aplicación. Se encarga de inicializar las clases 
y objetos necesarios, y de configurar los listeners de eventos para la interacción con el usuario.
*/

import ImageProcessor from './imageProcessor/ImageProcessor.js';
import VerticalLineStrategy from './imageProcessor/strategies/VerticalLineStrategy.js';
import CanvasUtilsImpl from './implementations/CanvasUtilsImpl.js';
import WebSocketUtilsImpl from './implementations/WebSocketUtilsImpl.js';
import DOMUpdater from './domUpdater.js';
import { initializeVideoManager } from './videoManagerInitializer.js';
import { setupEventListeners } from './eventListeners.js'; // Import the function

// Implementaciones de interfaces
const canvasUtils       = new CanvasUtilsImpl();
const webSocketUtils    = new WebSocketUtilsImpl();
const strategy          = new VerticalLineStrategy(canvasUtils, webSocketUtils);
const imageProcessor    = new ImageProcessor(5, 100, 50, canvasUtils, webSocketUtils, strategy);
const videoManager = initializeVideoManager();
const domUpdater        = new DOMUpdater(); // Create an instance of DOMUpdater

// Define refreshInterval
let refreshInterval = 2000;

function promedio(dateInicio, arrayTimeProccessor){
    let margen = 2; // margen para no sobre exigir el procesador
    let dateFin = new Date();
    let diff = dateFin - dateInicio;
    arrayTimeProccessor.push(diff);
    let sum = 0;
    for(let i = 0; i < arrayTimeProccessor.length; i++){
        sum += arrayTimeProccessor[i];
    }
    let average = sum / arrayTimeProccessor.length;
    average = Math.round(average);

    // quiero que diff tenga 3 digitos, si tiene menos, le agrego 0 al principio
    diff = diff.toString();
    while(diff.length < 3){
        diff = "0" + diff;
    }
    
    average = average.toString();
    while(average.length < 3){
        average = "0" + average;
    }
    console.log("T1: ", diff, " ms - T2: ", average, " ms");
    refreshInterval = average * margen;
    return refreshInterval;
}



/**
 * Función principal de inicialización.
 * Inicializa el VideoManager, configura el procesamiento de imágenes y los listeners de eventos.
 */
function initializeApp() {
    console.log("DOM fully loaded and parsed");
    console.log("VideoManager initialized:", videoManager);
    let arrayTimeProccessor = [];
    
    function update() {
        let dateInicio = new Date();
        const img = imageProcessor.pickImage(videoManager.video);
        domUpdater.updateCanvas(img);
        refreshInterval = promedio(dateInicio, arrayTimeProccessor);
        
        // Reiniciar el intervalo con el nuevo valor de refreshInterval
        clearInterval(intervalId);
        intervalId = setInterval(update, refreshInterval);
    }
    
    let intervalId = setInterval(update, refreshInterval);
    setupEventListeners();
    console.log("Event listeners set up");
}

// Evento DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});