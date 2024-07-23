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

export function drawVerticalLine2(context, pos, color = 'yellow') {
        // Dibujar la línea vertical roja en el centro del canvas
        const centerX = canvas.width / 2; // Calcula el centro del canvas en el eje X
        context.strokeStyle = 'red'; // Color de la línea
        context.lineWidth = 2; // Ancho de la línea
    
        context.beginPath();
        context.moveTo(centerX, 0);
        context.lineTo(centerX, canvas.height);
        context.stroke();
}