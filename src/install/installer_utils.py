from pathlib import Path
from src.logs.config_logger import LoggerConfigurator
import winshell
from src.install.shortcut_strategy import ShortcutCreationStrategy, DefaultShortcutCreationStrategy  # Actualizar la ruta de importación
from pywintypes import com_error

class ProjectInstaller:
    """
    Clase principal encargada de la instalación del proyecto.
    """
    def __init__(self):
        """
        Inicializa el instalador del proyecto.
        """
        self.logger = LoggerConfigurator().configure()
        self.project_dir = Path(__file__).parent.parent.resolve()
        self.name_proj = self.get_project_name()

    def get_project_name(self):
        """
        Recupera el nombre del proyecto basado en el nombre del directorio principal o un archivo específico.
        
        Returns:
            str: Nombre del proyecto.
        """
        try:
            project_name = self.project_dir.name
            self.logger.debug(f"Nombre del proyecto detectado: {project_name}")
            return project_name
        except Exception as e:
            self.logger.error(f"Error al obtener el nombre del proyecto: {e}")
            return "Unknown_Project"

    def main(self):
        """
        Método principal que inicia el proceso de instalación del proyecto.
        """
        print("Iniciando instalador")
        print(f"Directorio del script: {self.project_dir}")
        print(f"Nombre del proyecto: {self.name_proj}")

        ruta_archivo_bat = self.project_dir / f"{self.name_proj}.bat"
        print(f"Ruta del archivo BAT: {ruta_archivo_bat}")
        if not ruta_archivo_bat.is_file():
            print(f"Creando archivo '{self.name_proj}.bat'")
            BatFileCreator(self.project_dir, self.name_proj, self.logger).crear_archivo_bat_con_pipenv()

        shortcut_strategy = DefaultShortcutCreationStrategy()
        ShortcutManager(self.project_dir, self.name_proj, self.logger, shortcut_strategy).create_shortcut(ruta_archivo_bat)

class ShortcutManager:
    """
    Clase responsable de gestionar la creación de accesos directos.
    """
    def __init__(self, project_dir, name_proj, logger, strategy: ShortcutCreationStrategy):
        self.project_dir = project_dir
        self.name_proj = name_proj
        self.logger = logger
        self.strategy = strategy

    def verificar_icono(self, ruta_icono):
        if not ruta_icono.is_file():
            self.logger.error(f"El archivo de icono '{ruta_icono}' no existe.")
            return False
        return True

    def create_shortcut(self, ruta_archivo_bat):
        escritorio = Path(winshell.desktop())
        ruta_acceso_directo = escritorio / f"{self.name_proj}.lnk"
        ruta_icono = self.project_dir / "config" / f"{self.name_proj}.ico"
        ruta_icono = self.project_dir / "static" / "favicon.ico"

        if not self.verificar_icono(ruta_icono):
            return False

        return self.strategy.create_shortcut(ruta_acceso_directo, ruta_archivo_bat, ruta_icono, self.logger)

class BatFileCreator:
    """
    Clase encargada de crear archivos BAT para la ejecución del proyecto.
    """
    def __init__(self, project_dir, name_proj, logger):
        self.project_dir = project_dir
        self.name_proj = name_proj
        self.logger = logger

    def crear_archivo_bat_con_pipenv(self):
        ruta_app_py = self.project_dir / 'run.py'
        ruta_archivo_bat = self.project_dir / f"{self.name_proj}.bat"

        contenido_bat = f"""
        pipenv run python "{ruta_app_py}"
        """

        with open(ruta_archivo_bat, 'w') as archivo_bat:
            archivo_bat.write(contenido_bat.strip())
        self.logger.debug(f"Archivo '{self.name_proj}.bat' creado exitosamente.")
        self.logger.debug(f"La dirección del archivo .bat es {ruta_archivo_bat}")
