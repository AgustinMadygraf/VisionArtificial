<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visión Artificial</title>
    <link rel="icon" href="../static/favicon.ico" type="image/x-icon">
    <script type="module" src="../static/js/main_camara.js"></script>
    <link rel="stylesheet" href="../static/css/style.css">
</head>

<body>
    <header>
        <h1>Visión Artificial</h1>
    </header>
    <main>
        <button id="but" aria-label="Iniciar Webcam">Iniciar</button>
        <div id="container">
            <div class="video-section">
                <h2>Original</h2>
                <video id="vid"></video>
            </div>
            <div class="image-section">
                <h2>Procesada</h2>
                <div id="image-canvas">
                    <img>
                </div>
            </div>
        </div>
    </main>
    <footer>
        <p>&copy; 2024 Visión Artificial. Todos los derechos reservados.</p>
    </footer>
</body>

</html>
