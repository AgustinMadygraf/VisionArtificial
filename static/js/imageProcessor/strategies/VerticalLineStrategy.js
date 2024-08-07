// static/js/imageProcessor/strategies/VerticalLineStrategy.js
import ImageProcessingStrategy from './ImageProcessingStrategy.js';

export default class VerticalLineStrategy extends ImageProcessingStrategy {
    constructor(canvasUtils, webSocketUtils) {
        super();
        this.canvasUtils = canvasUtils;
        this.webSocketUtils = webSocketUtils;
    }

    process(canvas) {
        const pos = this.maxVerticalJumpPixelPos(canvas);
        this.vertLineInCanvas(canvas, pos.pos);
    }

    maxVerticalJumpPixelPos(canvas) {
        const ctx = canvas.getContext('2d', { willReadFrequently: true });

        const heightMid = Math.floor(canvas.height / 2);
        const heightCotas = { lo: heightMid - 100, hi: heightMid + 100 };

        const widthMid = Math.floor(canvas.width / 2);
        const widthCotas = { lo: widthMid - 50, hi: widthMid + 50 };

        const vertAdd = [];
        const horizDiff = [];
        let maxDiff = { diff: -256 * 3 * 2 * 100, pos: 0 };

        for (let x = widthCotas.lo; x < widthCotas.hi; x++) {
            const arr_x = x - widthCotas.lo;
            vertAdd.push(0);
            for (let y = heightCotas.lo; y < heightCotas.hi; y++) {
                const point = ctx.getImageData(x, y, 1, 1).data;
                vertAdd[arr_x] = vertAdd[arr_x] + (point[0] + point[1] + point[2]);
            }
            if (arr_x > 1) {
                horizDiff.push(vertAdd[arr_x] - vertAdd[arr_x - 1]);
                if (horizDiff[arr_x - 2] > maxDiff.diff) {
                    maxDiff.pos = x - 1;
                    maxDiff.diff = horizDiff[arr_x - 2];
                }
            }
        }
        return maxDiff;
    }

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
