/*
static/js/implementations/CanvasUtilsImpl.js
Este archivo contiene la implementación de la interfaz CanvasUtilsInterface.
*/
import CanvasUtilsInterface from '../interfaces/canvasUtilsInterface.js';
import { drawVerticalLine, drawHorizontalLine, drawCenterRuler } from '../utils/canvasUtils.js';

/**
 * Implementación de la interfaz CanvasUtilsInterface.
 * Proporciona métodos para dibujar en un canvas.
 */
export default class CanvasUtilsImpl extends CanvasUtilsInterface {
    /**
     * Dibuja una línea vertical en el canvas.
     * @param {CanvasRenderingContext2D} context - El contexto del canvas donde se dibujará la línea.
     * @param {number} pos - La posición en el eje X donde se dibujará la línea.
     * @param {string} [color='yellow'] - El color de la línea.
     */
    drawVerticalLine(context, pos, color = 'yellow') {
        drawVerticalLine(context, pos, color);
    }

    /**
     * Dibuja una línea horizontal en el canvas.
     * @param {CanvasRenderingContext2D} context - El contexto del canvas donde se dibujará la línea.
     * @param {number} pos - La posición en el eje Y donde se dibujará la línea.
     * @param {string} [color='green'] - El color de la línea.
     */
    drawHorizontalLine(context, pos, color = 'green') {
        drawHorizontalLine(context, pos, color);
    }

    /**
     * Dibuja una regla en el centro del canvas.
     * @param {CanvasRenderingContext2D} context - El contexto del canvas donde se dibujará la regla.
     * @param {string} [color='blue'] - El color de la regla.
     * @param {number} [lineLength=10] - La longitud de las líneas de la regla.
     * @param {number} [spacing=10] - El espacio entre las líneas de la regla.
     */
    drawCenterRuler(context, color = 'blue', lineLength = 10, spacing = 10) {
        drawCenterRuler(context, color, lineLength, spacing);
    }
}