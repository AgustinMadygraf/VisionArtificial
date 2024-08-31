/*
static/js/eventListeners.js
Este archivo contiene la función setupEventListeners, que se encarga de configurar los listeners de eventos.
*/
import { adjustLayoutForOrientation } from './uiManager.js';

/**
 * Configura los listeners de eventos.
 */
export function setupEventListeners() {
    adjustLayoutForOrientation();
    window.addEventListener('resize', adjustLayoutForOrientation);
}