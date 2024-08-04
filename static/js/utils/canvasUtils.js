// static/js/utils/canvasUtils.js

export function drawVerticalLine(context, pos, color = 'yellow') {
    context.strokeStyle = color;
    context.lineWidth = 2;

    context.beginPath();
    context.moveTo(pos, 0);
    context.lineTo(pos, context.canvas.height);
    context.stroke();
}

export function drawHorizontalLine(context, pos, color = 'green') {
    context.strokeStyle = color;
    context.lineWidth = 2;

    context.beginPath();
    context.moveTo(0, pos);
    context.lineTo(context.canvas.width, pos);
    context.stroke();
}

export function drawCenterRuler(context, color = 'blue', lineLength = 10, spacing = 10) {
    const centerY = context.canvas.height / 2;
    context.strokeStyle = color;
    context.lineWidth = 2;

    for (let x = 0; x < context.canvas.width; x += spacing) {
        context.beginPath();
        context.moveTo(x, centerY - lineLength / 2);
        context.lineTo(x, centerY + lineLength / 2);
        context.stroke();
    }
}
