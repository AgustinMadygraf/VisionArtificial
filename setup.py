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
            # Ejecuta el comando para actualizar pip
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
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
    def install(self, dependency: str) -> None:
        """
        Instala una dependencia usando pip.

        :param dependency: Nombre de la dependencia a instalar.
        """
        print(f"Instalando {dependency} usando pip...")
        try:
            # Ejecuta el comando pip para instalar la dependencia
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
            print(f"{dependency} instalado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"No se pudo instalar {dependency}. Error: {e}")

class DependencyChecker:
    """
    Clase responsable de verificar e instalar las dependencias faltantes.
    """
    def __init__(self, dependencies: list, installer: DependencyInstaller, pip_updater: PipUpdater):
        """
        Inicializa la clase DependencyChecker con una lista de dependencias, un instalador y un actualizador de pip.

        :param dependencies: Lista de nombres de dependencias a verificar.
        :param installer: Instancia de una clase que hereda de DependencyInstaller.
        :param pip_updater: Instancia de PipUpdater para actualizar pip antes de instalar dependencias.
        """
        self.dependencies = dependencies
        self.installer = installer
        self.pip_updater = pip_updater

    def check_dependencies(self) -> None:
        """
        Verifica las dependencias, actualiza pip si es necesario e instala las dependencias faltantes.
        """
        missing_dependencies = self.get_missing_dependencies()
        if missing_dependencies:
            self.pip_updater.update_pip()  # Actualiza pip antes de instalar las dependencias faltantes
            self.install_missing_dependencies(missing_dependencies)
        else:
            print("Todas las dependencias están instaladas.")

    def get_missing_dependencies(self) -> list:
        """
        Verifica qué dependencias están faltando y devuelve una lista de ellas.

        :return: Lista de dependencias que no están instaladas.
        """
        missing_dependencies = []
        for dependency in self.dependencies:
            try:
                # Intenta importar la dependencia para verificar si está instalada
                __import__(dependency)
            except ImportError:
                # Si falla la importación, agrega la dependencia a la lista de faltantes
                missing_dependencies.append(dependency)
        return missing_dependencies

    def install_missing_dependencies(self, missing_dependencies: list) -> None:
        """
        Instala las dependencias faltantes utilizando el instalador proporcionado.

        :param missing_dependencies: Lista de dependencias que necesitan ser instaladas.
        """
        print(f"Las siguientes dependencias están faltantes: {', '.join(missing_dependencies)}")
        print("Intentando instalar dependencias faltantes...")
        for dep in missing_dependencies:
            # Usa el instalador inyectado para instalar cada dependencia
            self.installer.install(dep)

if __name__ == "__main__":
    # Lista de dependencias que se requiere verificar e instalar
    dependencies = ["pipenv", "winshell", "win32com.client", "pywintypes", "colorlog"]
    
    # Crear instancias de las clases necesarias
    pip_updater = PipUpdater()
    installer = PipDependencyInstaller()
    checker = DependencyChecker(dependencies, installer, pip_updater)
    
    # Verifica e instala las dependencias faltantes
    checker.check_dependencies()
    
    try:
        # Intento de importar y ejecutar el instalador del proyecto
        from src.installer_utils import ProjectInstaller
        installer = ProjectInstaller()
        installer.main()
    except ImportError as e:
        print(f"Error al importar ProjectInstaller: {e}")
