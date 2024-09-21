// static/js/imageProcessor/ColorFilter.js

export default class ColorFilter {
    /**
     * Aplica un filtro en el canvas.
     * Si el color es marrón, se mantiene.
     * Si no es marrón, se convierte a verde.
     * @param {CanvasRenderingContext2D} ctx - Contexto del canvas.
     * @param {number} width - Ancho del canvas.
     * @param {number} height - Altura del canvas.
     */
    applyColorFilter(ctx, canvasWidth, canvasHeight) {
        const imageData = ctx.getImageData(0, 0, canvasWidth, canvasHeight);
        const pixelData = imageData.data;

        for (let i = 0; i < pixelData.length; i += 4) {
            const red = pixelData[i];
            const green = pixelData[i + 1];
            const blue = pixelData[i + 2];

            const blueMargin = 40;            
            const greenBlueThreshold = 4;
            const redGreenThreshold = greenBlueThreshold * 2;

            const isBrown = red > (green + redGreenThreshold) && green > (blue + greenBlueThreshold);
            const isYellow = red > (blue + blueMargin) && green > (blue + blueMargin);
            const isNotYellow = !isYellow;

            if (isBrown 
                && isNotYellow
            ) {
                // Mantener el color original
                pixelData[i] = red; 
                pixelData[i + 1] = green; 
                pixelData[i + 2] = blue; 
            } else {
                // Transformar a rojo
                pixelData[i] = 255;    // Rojo
                pixelData[i + 1] = 0;  // Verde
                pixelData[i + 2] = 0;  // Azul
            }
        }
        ctx.putImageData(imageData, 0, 0);
    }
}
