// static/js/implementations/CanvasUtilsImpl.js
import CanvasUtilsInterface from '../interfaces/canvasUtilsInterface.js';
import { drawVerticalLine, drawHorizontalLine, drawCenterRuler } from '../utils/canvasUtils.js';

export default class CanvasUtilsImpl extends CanvasUtilsInterface {
    drawVerticalLine(context, pos, color) {
        drawVerticalLine(context, pos, color);
    }
    drawHorizontalLine(context, pos, color) {
        drawHorizontalLine(context, pos, color);
    }
    drawCenterRuler(context, color, lineLength, spacing) {
        drawCenterRuler(context, color, lineLength, spacing);
    }
}

