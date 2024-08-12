"""
Este módulo gestiona la instalación y actualización de dependencias de Python usando pip.
"""

import subprocess
import sys

class PipUpdater:
    """
    Clase responsable de actualizar pip a la última versión disponible.
    """
    def update_pip(self) -> None:
        """
        Actualiza pip utilizando el comando `pip install --upgrade pip`.
        """
        print("Actualizando pip...")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'
            ])
            print("pip actualizado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"No se pudo actualizar pip. Error: {e}")


class DependencyInstaller:
    """
    Interfaz para la instalación de dependencias.
    Las clases que hereden de esta deberán implementar el método `install`.
    """
    def install(self, dependency: str) -> None:
        """
        Método para instalar una dependencia. Debe ser implementado por una subclase.
        """
        raise NotImplementedError("Este método debe ser implementado por una subclase")


class PipDependencyInstaller(DependencyInstaller):
    """
    Clase concreta que implementa la instalación de dependencias usando pip.
    """
    def install(self, dependency: str) -> bool:
        """
        Instala una dependencia usando pip.

        :param dependency: Nombre de la dependencia a instalar.
        :return: True si la instalación fue exitosa, False en caso contrario.
        """
        print(f"Instalando {dependency} usando pip...")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', dependency
            ])
            print(f"{dependency} instalado correctamente.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"No se pudo instalar {dependency}. Error: {e}")
            return False


class DependencyInstallerManager:
    """
    Clase responsable de instalar las dependencias faltantes.
    """
    def __init__(
        self,
        installer: DependencyInstaller,
        pip_updater: PipUpdater,
        max_retries: int = 3
    ):
        self.installer = installer
        self.pip_updater = pip_updater
        self.max_retries = max_retries

    def install_missing_dependencies(self, requirements_file: str = 'requirements.txt') -> None:
        """
        Instala las dependencias faltantes utilizando el instalador proporcionado.
        Si una instalación falla, se reintentará hasta max_retries veces.

        :param requirements_file: Ruta al archivo requirements.txt que contiene las dependencias.
        """
        print(f"Verificando dependencias desde {requirements_file}...")
