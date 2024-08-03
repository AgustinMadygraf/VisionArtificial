// js/canvasUtils.js
export function drawVerticalLine(context, pos, color = 'yellow') {
    context.strokeStyle = color; // Color de la línea
    context.lineWidth = 2; // Ancho de la línea

    context.beginPath();
    context.moveTo(pos, 0);
    context.lineTo(pos, context.canvas.height);
    context.stroke();
}

export function drawHorizontalLine(context, pos, color = 'green') {
    context.strokeStyle = color; // Color de la línea
    context.lineWidth = 2; // Ancho de la línea

    context.beginPath();
    context.moveTo(0, pos);
    context.lineTo(context.canvas.width, pos);
    context.stroke();
}

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
