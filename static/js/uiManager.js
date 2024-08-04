// static/js/uiManager.js

function adjustLayoutForOrientation() {
    const container = document.getElementById('container');
    if (window.innerWidth > window.innerHeight) {
        container.classList.add('landscape');
    } else {
        container.classList.remove('landscape');
    }
}

export { adjustLayoutForOrientation };
