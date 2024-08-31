// static/js/interfaces/canvasUtilsInterface.js
export default class CanvasUtilsInterface {
    drawVerticalLine(_context, _pos, _color) {
        throw new Error('You have to implement the method drawVerticalLine!');
    }
    drawHorizontalLine(_context, _pos, _color) {
        throw new Error('You have to implement the method drawHorizontalLine!');
    }
    drawCenterRuler(_context, _color, _lineLength, _spacing) {
        throw new Error('You have to implement the method drawCenterRuler!');
    }
}