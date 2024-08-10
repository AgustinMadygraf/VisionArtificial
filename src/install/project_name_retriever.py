# VisionArtificial/src/install/project_name_retriever.py

from pathlib import Path

class ProjectNameRetriever:
    """
    Clase responsable de obtener el nombre del proyecto basado en el nombre del directorio principal o un archivo específico.
    """
    def __init__(self, project_dir: Path):
        """
        Inicializa la clase con la ruta del directorio del proyecto.
        
        :param project_dir: Ruta del directorio del proyecto.
        """
        self.project_dir = project_dir

    def get_project_name(self) -> str:
        """
        Recupera el nombre del proyecto basado en el nombre del directorio principal.

        :return: Nombre del proyecto.
        """
        try:
            project_name = self.project_dir.name
            return project_name
        except Exception as e:
            print(f"Error al obtener el nombre del proyecto: {e}")
            return "Unknown_Project"
