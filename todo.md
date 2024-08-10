### 1. **Refactorizar `ProjectInstaller` para SRP**
   - **Archivo a modificar**: `VisionArtificial/src/install/installer_utils.py`
   - **Tarea**: Separar la responsabilidad de obtención del nombre del proyecto de la clase `ProjectInstaller` creando una nueva clase `ProjectNameRetriever`. La clase `ProjectInstaller` debe enfocarse solo en la instalación del proyecto.

### 2. **Crear Clase `ProjectNameRetriever`**
   - **Archivo a crear**: `VisionArtificial/src/install/project_name_retriever.py`
   - **Tarea**: Implementar la clase `ProjectNameRetriever` que se encargue exclusivamente de obtener el nombre del proyecto. Integrar esta clase en `ProjectInstaller` para obtener el nombre del proyecto.

### 3. **Aplicar el Patrón Strategy en la Creación de Archivos BAT**
   - **Archivo a modificar**: `VisionArtificial/src/install/installer_utils.py`
   - **Tarea**: Refactorizar la lógica de creación de archivos BAT en `ProjectInstaller` para usar el patrón de diseño Strategy, permitiendo diferentes estrategias de creación de archivos BAT.

### 4. **Crear Interfaces para las Estrategias de Creación de Archivos BAT**
   - **Archivo a crear**: `VisionArtificial/src/install/bat_creation_strategy.py`
   - **Tarea**: Crear una interfaz `BatCreationStrategy` para definir el contrato de creación de archivos BAT. Implementar diferentes estrategias, como `PipenvBatCreationStrategy` y `VirtualenvBatCreationStrategy`.

### 5. **Refactorizar `ShortcutManager` para SRP**
   - **Archivo a modificar**: `VisionArtificial/src/install/installer_utils.py`
   - **Tarea**: Separar la lógica de verificación de íconos de la clase `ShortcutManager` creando una nueva clase `IconVerifier`. `ShortcutManager` debería centrarse únicamente en la creación de accesos directos.

### 6. **Crear Clase `IconVerifier`**
   - **Archivo a crear**: `VisionArtificial/src/install/icon_verifier.py`
   - **Tarea**: Implementar la clase `IconVerifier` que maneje la verificación de la existencia de íconos. Integrar esta clase en `ShortcutManager`.

### 7. **Implementar un Patrón Strategy para `ShortcutManager`**
   - **Archivo a modificar**: `VisionArtificial/src/install/shorcut_strategy.py`
   - **Tarea**: Asegurar que la clase `ShortcutManager` puede aceptar diferentes estrategias para la creación de accesos directos, utilizando el patrón Strategy. Modificar el constructor para aceptar cualquier implementación de `ShortcutCreationStrategy`.

### 8. **Refactorizar `DependencyInstallerManager` para DIP**
   - **Archivo a modificar**: `VisionArtificial/src/install/dependency_manager.py`
   - **Tarea**: Modificar `DependencyInstallerManager` para aceptar cualquier implementación de `DependencyInstaller` a través de inyección de dependencias. Esto desacoplará la clase de implementaciones concretas como `PipDependencyInstaller`.

### 9. **Crear Subclase para Nuevas Estrategias de Instalación**
   - **Archivo a crear**: `VisionArtificial/src/install/conda_dependency_installer.py`
   - **Tarea**: Implementar una nueva clase `CondaDependencyInstaller` que herede de `DependencyInstaller`, permitiendo instalar dependencias usando Conda. Esto permitirá extender el código sin modificar `DependencyInstallerManager`.

### 10. **Escribir Pruebas Unitarias para Nuevas Clases y Métodos**
   - **Archivo a modificar/crear**: `VisionArtificial/tests/test_dependency_manager.py`, `VisionArtificial/tests/test_installer_utils.py`, `VisionArtificial/tests/test_shorcut_strategy.py`
   - **Tarea**: Escribir pruebas unitarias que cubran las nuevas clases y métodos creados. Esto incluiría pruebas para `ProjectNameRetriever`, `BatCreationStrategy`, `IconVerifier`, y `CondaDependencyInstaller` para asegurar que todo se comporta como se espera.