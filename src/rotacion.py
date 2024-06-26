#VisionArtificial\src\rotacion.py
import cv2
import logging

# Asumiendo que ya tienes configurado un logger en tu aplicación
logger = logging.getLogger(__name__)

def rotar_imagen(frame, grados):
    """
    Rota la imagen un número específico de grados en sentido antihorario.
    
    Utiliza la matriz de rotación de OpenCV para rotar la imagen alrededor de su centro sin cambiar su escala.
    
    Parámetros:
    - frame (np.ndarray): Imagen a rotar.
    - grados (float): Número de grados para rotar la imagen. Los valores positivos rotan en sentido antihorario.
    
    Retorna:
    - np.ndarray: La imagen rotada.
    
    Lanza:
    - Exception: Si ocurre un error durante la rotación de la imagen.
    """
    try:
        altura, ancho = frame.shape[:2]
        punto_central = (ancho // 2, altura // 2)
        matriz_rotacion = cv2.getRotationMatrix2D(punto_central, grados, 1.0)
        return cv2.warpAffine(frame, matriz_rotacion, (ancho, altura))
    except Exception as e:
        logger.error(f"Error al rotar la imagen: {e}")
        raise
