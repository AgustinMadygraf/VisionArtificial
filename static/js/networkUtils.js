// static/js/networkUtils.js

// Obtener la IP local desde el servidor
export async function getLocalIp() {
    try {
        const response = await fetch('/local-ip');
        const data = await response.json();
        console.log('Local IP:', data.ip);
        return data.ip;
    } catch (error) {
        console.error('Error fetching local IP:', error);
        return null;
    }
}
