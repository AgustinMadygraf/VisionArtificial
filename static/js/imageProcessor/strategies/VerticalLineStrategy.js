/**
 * static/js/imageProcessor/strategies/VerticalLineStrategy.js
 * Clase VerticalLineStrategy.
 * Estrategia de procesamiento de imágenes que dibuja una línea vertical en el canvas.
 */
export default class VerticalLineStrategy {
    constructor(canvasUtils, webSocketUtils) {
        this.canvasUtils = canvasUtils;
        this.webSocketUtils = webSocketUtils;
    }

    /**
     * Process the given canvas by finding the maximum vertical jump pixel position 
     * and drawing a vertical line on the canvas.
     * 
     * @param {Canvas} canvas - The canvas to be processed.
     * @returns {void}
     */
    process(canvas) {
        const pos = this.maxVerticalJumpPixelPos(canvas);
        this.vertLineInCanvas(canvas, pos.pos);
    }

    /**
     * Calculates the maximum vertical jump pixel position within the given canvas.
     * 
     * @param {HTMLCanvasElement} canvas - The canvas element to process.
     * @returns {{ diff: number, pos: number }} - An object containing the maximum difference and its corresponding position.
     */
    maxVerticalJumpPixelPos(canvas) {
        const ctx = this.getContext(canvas);
        const { heightCotas, widthCotas } = this.getCotas(canvas);
        const vertAdd = this.calculateVerticalSums(ctx, widthCotas, heightCotas);
        const horizDiff = this.calculateHorizontalDifferences(vertAdd);
        return this.findMaxDifference(horizDiff, widthCotas);
    }

    /**
     * Obtiene el contexto 2D del canvas.
     * 
     * @param {HTMLCanvasElement} canvas - El elemento canvas del cual obtener el contexto.
     * @returns {CanvasRenderingContext2D} - El contexto 2D del canvas.
     */
    getContext(canvas) {
        return canvas.getContext('2d', { willReadFrequently: true });
    }
    /**
     * Calcula y devuelve las cotas (límites) verticales y horizontales alrededor del centro del canvas.
     * 
     * @param {HTMLCanvasElement} canvas - El elemento canvas del cual calcular las cotas.
     * @returns {{ heightCotas: { lo: number, hi: number }, widthCotas: { lo: number, hi: number } }} - Un objeto que contiene las cotas verticales y horizontales.
     */
    getCotas(canvas) {
        const heightMid = Math.floor(canvas.height / 2);
        const heightCotas = { lo: heightMid - 100, hi: heightMid + 100 };

        const widthMid = Math.floor(canvas.width / 2);
        const widthCotas = { lo: widthMid - 50, hi: widthMid + 50 };

        return { heightCotas, widthCotas };
    }

    /**
     * Calcula las sumas verticales solo para los píxeles de color marrón.
     * 
     * @param {CanvasRenderingContext2D} ctx - El contexto 2D del canvas.
     * @param {{ lo: number, hi: number }} widthCotas - Las cotas horizontales (límites) para el procesamiento.
     * @param {{ lo: number, hi: number }} heightCotas - Las cotas verticales (límites) para el procesamiento.
     * @returns {number[]} - Un arreglo que contiene las sumas verticales de los valores RGB de los píxeles marrones para cada columna.
     */
    calculateVerticalSums(ctx, widthCotas, heightCotas) {
        const vertAdd = [];
        for (let x = widthCotas.lo; x < widthCotas.hi; x++) {
            const arr_x = x - widthCotas.lo;
            vertAdd.push(0);
            for (let y = heightCotas.lo; y < heightCotas.hi; y++) {
                const point = ctx.getImageData(x, y, 1, 1).data;
                // Verificar si el píxel es marrón antes de sumarlo
                if (this.isBrown(point)) {
                    vertAdd[arr_x] += (point[0] + point[1] + point[2]);
                }
            }
        }
        return vertAdd;
    }

    /**
     * Verifica si un píxel es de color marrón basado en los valores RGB.
     * 
     * @param {Uint8ClampedArray} point - Un arreglo de valores RGB de un píxel.
     * @returns {boolean} - Verdadero si el píxel es marrón, falso en caso contrario.
     */
    isBrown(point) {
        const [r, g, b] = point;
        // Lógica para determinar si el color es marrón
        // Ajustar los valores según las características de marrón deseadas
        return r > 100 && r < 200 && g > 50 && g < 150 && b < 100 && r > g && r > b;
    }

    /**
     * Calcula las diferencias horizontales entre las sumas verticales de columnas adyacentes.
     * 
     * @param {number[]} vertAdd - Un arreglo que contiene las sumas verticales de los valores RGB de los píxeles para cada columna.
     * @returns {number[]} - Un arreglo que contiene las diferencias horizontales entre las sumas verticales de columnas adyacentes.
     */
    calculateHorizontalDifferences(vertAdd) {
        const horizDiff = [];
        for (let i = 1; i < vertAdd.length; i++) {
            horizDiff.push(vertAdd[i] - vertAdd[i - 1]);
        }
        return horizDiff;
    }

    /**
     * Encuentra la diferencia máxima específica para bordes de color marrón y su posición correspondiente.
     * 
     * @param {number[]} horizDiff - Un arreglo que contiene las diferencias horizontales entre las sumas verticales de columnas adyacentes.
     * @param {{ lo: number, hi: number }} widthCotas - Las cotas horizontales (límites) para el procesamiento.
     * @returns {{ diff: number, pos: number }} - Un objeto que contiene la diferencia máxima para bordes marrones y su posición correspondiente.
     */
    findMaxDifference(horizDiff, widthCotas) {
        let maxDiff = -Infinity;
        let maxPos = widthCotas.lo;

        horizDiff.forEach((diff, i) => {
            // Ajuste para identificar cambios asociados al color marrón
            // Por ejemplo, considerar solo diferencias significativas que podrían indicar la presencia de un borde marrón
            if (this.isSignificantBrownEdge(diff) && diff > maxDiff) {
                maxDiff = diff;
                maxPos = widthCotas.lo + i + 1; // Ajuste del índice para reflejar la posición correcta
            }
        });

        return { diff: maxDiff, pos: maxPos };
    }

    /**
     * Verifica si una diferencia es significativa para detectar un borde marrón.
     * 
     * @param {number} diff - Diferencia entre las sumas verticales de columnas adyacentes.
     * @returns {boolean} - Verdadero si la diferencia es significativa para detectar un borde marrón, falso en caso contrario.
     */
    isSignificantBrownEdge(diff) {
        // Umbrales específicos para la detección de bordes marrones
        // Puedes ajustar estos valores según los requerimientos específicos
        const brownThreshold = 50; // Ajustar este valor según los tonos de marrón esperados
        return diff >= brownThreshold;
    }

    /**
     * Draws a vertical line on the canvas at the specified position.
     * 
     * @param {HTMLCanvasElement} canvas - The canvas element on which to draw the line.
     * @param {number} pos - The x-coordinate of the position where the line should be drawn.
     * @returns {void}
     */
    vertLineInCanvas(canvas, pos) {
        const context = canvas.getContext('2d');

        this.canvasUtils.drawVerticalLine(context, pos, 'yellow');

        const centerX = canvas.width / 2;
        this.canvasUtils.drawVerticalLine(context, centerX, 'red');

        const centerY = canvas.height / 2;
        this.canvasUtils.drawHorizontalLine(context, centerY, 'green');

        this.canvasUtils.drawCenterRuler(context, 'blue', 10, 10);

        const deviation = pos - centerX;
        context.fillStyle = 'white';
        context.font = '20px Arial';
        context.fillText(`Desvío: ${deviation}px`, 10, 30);

        context.strokeStyle = 'white';
        context.lineWidth = 1;
        context.beginPath();
        context.moveTo(centerX, centerY);
        context.lineTo(pos, centerY);
        context.stroke();

        this.webSocketUtils.sendWebSocketMessage(`Drawing line in position ${deviation}`);
    }
}
