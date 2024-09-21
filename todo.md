### To Do List

1. **Separar la configuración del logger**
   - **Archivo a modificar**: [`src/install/project_installer.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FAppServ%2Fwww%2FVisionArtificial%2Fsrc%2Finstall%2Fproject_installer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22c279cdb3-27fa-478d-8698-378db6895387%22%5D "c:\AppServ\www\VisionArtificial\src\install\project_installer.py")
   - **Descripción detallada**: La configuración del logger debe ser movida a una clase o módulo separado. Esto ayudará a cumplir con el Principio de Responsabilidad Única (SRP) y hará que la clase `ProjectInstaller` sea más cohesiva.

2. **Crear pruebas unitarias para nuevas funciones**
   - **Archivo a modificar**: [`tests/test_install.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FAppServ%2Fwww%2FVisionArtificial%2Ftests%2Ftest_install.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22c279cdb3-27fa-478d-8698-378db6895387%22%5D "c:\AppServ\www\VisionArtificial\tests\test_install.py")
   - **Descripción detallada**: Después de refactorizar las funciones y clases, se deben crear pruebas unitarias para asegurar que el nuevo código funcione correctamente y que no se introduzcan errores.