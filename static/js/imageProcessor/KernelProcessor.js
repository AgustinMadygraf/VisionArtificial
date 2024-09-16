/*
static/js/imageProcessor/KernelProcessor.js
Este archivo contiene las funciones relacionadas con el procesamiento de imágenes usando un kernel.
*/

export default class KernelProcessor {
    constructor() {
        // Definición de filtros 3x3
        this.filters = {
            default: [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            enfoque: [
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ],
            desenfoque: [
                //un filtro que este dividido por 9
                [1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9],
                [1/9, 1/9, 1/9]
            ],
            eje_basico: [
                [-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]
            ],
            eje_vertical: [
                [-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]
            ],
        };
        this.currentFilter = 'eje_vertical';
        console.log('KernelProcessor initialized');
        console.log('Filtro:', this.currentFilter);
    }

    /**
     * Aplica un filtro de kernel en el canvas.
     * @param {CanvasRenderingContext2D} ctx - Contexto del canvas.
     * @param {number} width - Ancho del canvas.
     * @param {number} height - Altura del canvas.
     */
    applyKernelFilter(ctx, width, height) {
        const imageData = ctx.getImageData(0, 0, width, height);
        const data = imageData.data;
        const filteredData = new Uint8ClampedArray(data.length);
        const kernel = this.filters[this.currentFilter];

        for (let y = 1; y < height - 1; y++) {
            for (let x = 1; x < width - 1; x++) {
                let r = 0, g = 0, b = 0;
                for (let ky = -1; ky <= 1; ky++) {
                    for (let kx = -1; kx <= 1; kx++) {
                        const pixelIndex = ((y + ky) * width + (x + kx)) * 4;
                        const weight = kernel[ky + 1][kx + 1];
                        r += data[pixelIndex] * weight;
                        g += data[pixelIndex + 1] * weight;
                        b += data[pixelIndex + 2] * weight;
                    }
                }
                const index = (y * width + x) * 4;
                filteredData[index] = r;
                filteredData[index + 1] = g;
                filteredData[index + 2] = b;
                filteredData[index + 3] = data[index + 3]; // Preserve alpha
            }
        }

        for (let i = 0; i < data.length; i++) {
            data[i] = filteredData[i];
        }

        ctx.putImageData(imageData, 0, 0);
    }

    /**
     * Cambia el filtro actual.
     * @param {string} filterName - Nombre del filtro a usar.
     */
    setFilter(filterName) {
        if (this.filters[filterName]) {
            this.currentFilter = filterName;
        } else {
            console.warn(`Filter ${filterName} does not exist. Using default filter.`);
            this.currentFilter = 'default';
        }
    }
}