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

        // Ajuste de los valores RGB típicos del marrón y las tolerancias
        const r_set = 150; // Ajustar valor base de rojo para marrón
        const g_set = 150;  // Ajustar valor base de verde para marrón
        const b_set = 150;  // Ajustar valor base de azul para marrón
        const tolerancia_r = 120; // Aumentar tolerancia para mayor rango de marrones
        const tolerancia_g = 120;
        const tolerancia_b = 120;

        for (let i = 0; i < data.length; i += 4) {
            const r = data[i];
            const g = data[i + 1];
            const b = data[i + 2];

            // Verificar si el color es marrón usando umbrales y relaciones
            if (
                r >= r_set - tolerancia_r && r <= r_set + tolerancia_r &&
                g >= g_set - tolerancia_g && g <= g_set + tolerancia_g &&
                b >= b_set - tolerancia_b && b <= b_set + tolerancia_b &&
                r > g && r > b // Condición adicional para tonos marrones
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
