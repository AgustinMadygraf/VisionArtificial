// js/canvasUtils.js

/**
 * Dibuja una línea vertical en el canvas.
 * @param {CanvasRenderingContext2D} context - El contexto del canvas en el que se va a dibujar.
 * @param {number} pos - La posición horizontal en la que se dibujará la línea.
 * @param {string} [color='yellow'] - El color de la línea.
 */
export function drawVerticalLine(context, pos, color = 'yellow') {
    context.strokeStyle = color; // Color de la línea
    context.lineWidth = 2; // Ancho de la línea

    context.beginPath();
    context.moveTo(pos, 0);
    context.lineTo(pos, context.canvas.height);
    context.stroke();
}

/**
 * Dibuja una línea horizontal en el canvas.
 * @param {CanvasRenderingContext2D} context - El contexto del canvas en el que se va a dibujar.
 * @param {number} pos - La posición vertical en la que se dibujará la línea.
 * @param {string} [color='green'] - El color de la línea.
 */
export function drawHorizontalLine(context, pos, color = 'green') {
    context.strokeStyle = color; // Color de la línea
    context.lineWidth = 2; // Ancho de la línea

    context.beginPath();
    context.moveTo(0, pos);
    context.lineTo(context.canvas.width, pos);
    context.stroke();
}

/**
 * Dibuja una regla horizontal en el centro del canvas.
 * @param {CanvasRenderingContext2D} context - El contexto del canvas en el que se va a dibujar.
 * @param {string} [color='blue'] - El color de las líneas de la regla.
 * @param {number} [lineLength=10] - La longitud de cada línea de la regla.
 * @param {number} [spacing=10] - El espacio entre cada línea de la regla.
 */
export function drawCenterRuler(context, color = 'blue', lineLength = 10, spacing = 10) {
    const centerY = context.canvas.height / 2; // Centro vertical del canvas
    context.strokeStyle = color; // Color de las líneas
    context.lineWidth = 2; // Ancho de las líneas

    for (let x = 0; x < context.canvas.width; x += spacing) {
        context.beginPath();
        context.moveTo(x, centerY - lineLength / 2);
        context.lineTo(x, centerY + lineLength / 2);
        context.stroke();
    }
}
