// static/js/networkUtils.js

/**
 * Obtiene la IP local desde el servidor.
 * @returns {Promise<string|null>} - La IP local si se obtiene correctamente, de lo contrario, null.
 */
export async function getLocalIp() {
    try {
        // Realiza una petición para obtener la IP local
        const response = await fetch('/local-ip');
        const data = await response.json();
        console.log('Local IP:', data.ip);
        return data.ip;
    } catch (error) {
        // Manejo de errores en caso de que la petición falle
        console.error('Error fetching local IP:', error);
        return null;
    }
}
