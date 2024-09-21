### todo.md

1. **Tarea**: Refactorizar para cumplir con el Principio de Responsabilidad Única (SRP)
   - **Archivo a modificar**: [`setup.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FAppServ%2Fwww%2FVisionArtificial%2Fsetup.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%2208cccf67-8c71-4694-8c33-efd05060254d%22%5D "c:\AppServ\www\VisionArtificial\setup.py")
   - **Descripción detallada**: Dividir la función `iniciar` en varias funciones más pequeñas, cada una con una única responsabilidad. Por ejemplo, crear funciones separadas para limpiar la pantalla, mostrar mensajes, actualizar pip, y verificar dependencias.

2. **Tarea**: Reducir el acoplamiento alto
   - **Archivo a modificar**: [`src/install/project_installer.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FAppServ%2Fwww%2FVisionArtificial%2Fsrc%2Finstall%2Fproject_installer.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%2208cccf67-8c71-4694-8c33-efd05060254d%22%5D "c:\AppServ\www\VisionArtificial\src\install\project_installer.py")
   - **Descripción detallada**: Introducir interfaces o clases abstractas para las dependencias de `ProjectInstaller` como `ProjectNameRetriever`, `BatFileCreator`, y `ShortcutManager`. Utilizar inyección de dependencias para pasar estas dependencias a `ProjectInstaller`.

3. **Tarea**: Implementar el Principio de Inversión de Dependencias (DIP)
   - **Archivo a modificar**: [`src/install/dependency_manager.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FAppServ%2Fwww%2FVisionArtificial%2Fsrc%2Finstall%2Fdependency_manager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%2208cccf67-8c71-4694-8c33-efd05060254d%22%5D "c:\AppServ\www\VisionArtificial\src\install\dependency_manager.py")
   - **Descripción detallada**: Crear interfaces para `PipDependencyInstaller` y `PipUpdater`. Modificar las clases concretas para que implementen estas interfaces y cambiar las dependencias en `DependencyInstallerManager` para que dependan de las interfaces en lugar de las clases concretas.

4. **Tarea**: Implementar el Principio de Inversión de Dependencias (DIP)
   - **Archivo a modificar**: [`src/install/python_interpreter_utils.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FAppServ%2Fwww%2FVisionArtificial%2Fsrc%2Finstall%2Fpython_interpreter_utils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%2208cccf67-8c71-4694-8c33-efd05060254d%22%5D "c:\AppServ\www\VisionArtificial\src\install\python_interpreter_utils.py")
   - **Descripción detallada**: Crear interfaces para las funcionalidades de `PythonInterpreterUtils`. Modificar la clase `PythonInterpreterUtils` para que implemente estas interfaces y cambiar las dependencias en el código para que utilicen las interfaces en lugar de la clase concreta.