"""
Este módulo define las estrategias para la creación de accesos directos.
"""

from abc import ABC, abstractmethod
from win32com.client import Dispatch
try:
    from pywintypes import com_error
except ImportError:
    from win32api import com_error  # Asegúrate de que la importación sea correcta según tu entorno

class ShortcutCreationStrategy(ABC):
    """
    Clase abstracta que define la interfaz para la creación de accesos directos.
    """
    @abstractmethod
    def create_shortcut(self, ruta_acceso_directo, ruta_archivo_bat, ruta_icono, logger):
        """
        Método abstracto para crear un acceso directo.
        """
        pass

class DefaultShortcutCreationStrategy(ShortcutCreationStrategy):
    """
    Estrategia por defecto para la creación de accesos directos utilizando Windows Script Host.
    """
    def create_shortcut(self, ruta_acceso_directo, ruta_archivo_bat, ruta_icono, logger):
        """
        Crea un acceso directo en el escritorio apuntando al archivo BAT especificado.
        """
        try:
            shell = Dispatch('WScript.Shell')
            acceso_directo = shell.CreateShortCut(str(ruta_acceso_directo))
            acceso_directo.Targetpath = str(ruta_archivo_bat)
            acceso_directo.WorkingDirectory = str(ruta_archivo_bat.parent)
            acceso_directo.IconLocation = str(ruta_icono)
            acceso_directo.save()
            logger.debug("Acceso directo creado o actualizado exitosamente.")
            return True
        except com_error as e:
            logger.error(
                f"No se pudo crear/actualizar el acceso directo debido a un error de COM: {e}",
                exc_info=True
            )
            return False
        except OSError as e:
            logger.error(
            f"No se pudo crear/actualizar el acceso directo debido a un error del sistema operativo: "
            f"{e}",                exc_info=True
                )
            return False
