// static/js/getQueryParam.js
/**
 * Obtiene el valor de un parámetro GET de la URL.
 * @param {string} paramName - El nombre del parámetro GET.
 * @returns {string|null} - El valor del parámetro GET o null si no existe.
 */
function getQueryParam(paramName) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(paramName);
}

export { getQueryParam };