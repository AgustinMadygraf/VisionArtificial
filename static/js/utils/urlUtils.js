/* 
static/js/utils/urlUtils.js
Este archivo contiene funciones para trabajar con URLs.
*/


/**
 * Obtiene el valor de un parámetro de consulta de la URL actual.
 *
 * @param {string} param - El nombre del parámetro de consulta a obtener.
 * @returns {string|null} El valor del parámetro de consulta, o null si no se encuentra.
 */
export function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}