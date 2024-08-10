# setup.py
import subprocess
import sys
import os
from src.install.dependency_manager import PipUpdater, DependencyVerifier, PipDependencyInstaller, DependencyInstallerManager

def is_pipenv_updated() -> bool:
    """
    Verifica si pipenv está actualizado con Pipfile y Pipfile.lock.
    """
    print("Verificando si pipenv está actualizado...")
    try:
        result = subprocess.run(['pipenv', 'sync', '--dry-run'], capture_output=True, text=True)
        if result.returncode == 0:
            print("pipenv está actualizado.")
            return True
        else:
            print("pipenv no está actualizado.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error al verificar pipenv. Error: {e}")
        return False

if __name__ == "__main__":
    # Limpiar pantalla
    os.system("cls")

    # Imprimir mensaje de inicio
    print("Iniciando instalador...")

    # Mostrar versión de Python
    print(f"Versión de Python: {sys.version}")

    # Lista de dependencias que se requiere verificar e instalar
    dependencies = ["pipenv", "winshell", "win32com.client", "pywintypes", "colorlog"]
    
    # Crear instancias de las clases necesarias
    pip_updater = PipUpdater()
    verifier = DependencyVerifier(dependencies)
    installer_manager = DependencyInstallerManager(PipDependencyInstaller(), pip_updater, max_retries=3)
    
    # Verifica e instala las dependencias faltantes
    missing_dependencies = verifier.get_missing_dependencies()
    if missing_dependencies:
        pip_updater.update_pip()
        installer_manager.install_missing_dependencies(missing_dependencies)
    else:
        print("Todas las dependencias están instaladas.")
    
    # Verifica si pipenv está actualizado
    if not is_pipenv_updated():
        print("Actualizando dependencias con pipenv...")
        subprocess.check_call(['pipenv', 'install'])

    try:
        # Intento de importar y ejecutar el instalador del proyecto
        from src.install.installer_utils import ProjectInstaller
        installer = ProjectInstaller()
        installer.main()
    except ImportError as e:
        print(f"Error al importar ProjectInstaller: {e}")
