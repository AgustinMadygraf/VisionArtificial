// static/js/uiManager.js

/**
 * Ajusta el diseño de la interfaz de usuario según la orientación de la pantalla.
 */
function adjustLayoutForOrientation() {
    const container = document.getElementById('container');
    if (window.innerWidth > window.innerHeight) {
        // Añadir clase para orientación horizontal (landscape)
        container.classList.add('landscape');
    } else {
        // Remover clase para orientación vertical (portrait)
        container.classList.remove('landscape');
    }
}

export { adjustLayoutForOrientation };
