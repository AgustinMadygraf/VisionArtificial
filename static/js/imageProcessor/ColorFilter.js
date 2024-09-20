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
    applyColorFilter(ctx, width, height) {
        const imageData = ctx.getImageData(0, 0, width, height);
        const data = imageData.data;

        for (let i = 0; i < data.length; i += 4) {
            const r = data[i];
            const g = data[i + 1];
            const b = data[i + 2];
        // Verificar si el color es amarillo o naranja
        const r_g = 5
        const g_b = 4
        const isBrown = r > (g  + r_g )&& g > ( b + g_b ) ;

            // Verificar si el color es marrón usando umbrales y relaciones
            if ( isBrown
            ) {
                // Mantener el color original
                data[i] = r; 
                data[i + 1] = g; 
                data[i + 2] = b; 
            } else {
                // Transformar
                data[i]     = 255;    // Rojo
                data[i + 1] = 0;    // Verde
                data[i + 2] = 0;    // Azul
            }
        }
        ctx.putImageData(imageData, 0, 0);
    }
}
