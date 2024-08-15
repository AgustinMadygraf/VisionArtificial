# Installer

## 1. Refactorizar `ProjectInstaller` para cumplir con DIP
- **Archivo:** `src/install/project_installer.py`
- **Descripción:** Refactoriza la clase `ProjectInstaller` para que dependa de una interfaz `LoggerInterface` en lugar de la clase concreta `LoggerConfigurator`. Implementa la inyección de dependencias mediante el constructor para facilitar el cambio de implementaciones de logger sin modificar la clase base.

## 2. Crear la interfaz `LoggerInterface`
- **Archivo:** `src/install/logging_utils.py` (nuevo archivo)
- **Descripción:** Crea una nueva interfaz `LoggerInterface` que defina los métodos necesarios para la configuración de loggers. Refactoriza la clase `LoggerConfigurator` para que implemente esta interfaz. De esta manera, `ProjectInstaller` puede trabajar con cualquier implementación que siga la interfaz.

## 3. Dividir responsabilidades en `ProjectInstaller`
- **Archivo:** `src/install/project_installer.py`
- **Descripción:** Separa la configuración del logger y la gestión de accesos directos de la instalación del proyecto en clases diferentes. Crea una nueva clase `LoggerManager` para manejar la configuración del logger.

## 4. Implementar el patrón de fábrica para `DependencyInstaller`
- **Archivo:** `src/install/dependency_manager.py`
- **Descripción:** Introduce un patrón de fábrica para la creación de diferentes tipos de `DependencyInstaller`. Esto permitirá extender la funcionalidad para manejar otros gestores de dependencias (por ejemplo, `CondaDependencyInstaller`) sin modificar la lógica existente.

## 5. Refactorizar `DependencyInstallerManager` para cumplir con SRP
- **Archivo:** `src/install/dependency_manager.py`
- **Descripción:** Divide `DependencyInstallerManager` en dos clases diferentes: una que se encargue de la gestión de instalación de dependencias y otra para la actualización de pip. Así, cada clase tendrá una única responsabilidad.

## 6. Crear pruebas unitarias para `ProjectInstaller`
- **Archivo:** `tests/test_project_installer.py` (nuevo archivo)
- **Descripción:** Escribe pruebas unitarias para la clase `ProjectInstaller`, asegurando que funcione correctamente con diferentes implementaciones de `LoggerInterface` y `ShortcutCreationStrategy`. Usa mocking para las dependencias externas.

## 7. Dividir la interfaz `ShortcutCreationStrategy` según ISP
- **Archivo:** `src/install/shortcut_creation_strategy.py`
- **Descripción:** Evalúa la interfaz `ShortcutCreationStrategy` y divídela en interfaces más pequeñas si es necesario, por ejemplo, una para la creación de accesos directos y otra para la verificación y gestión de iconos.

## 8. Refactorizar `PipDependencyInstaller` para permitir la extensión
- **Archivo:** `src/install/dependency_manager.py`
- **Descripción:** Modifica `PipDependencyInstaller` para que sea más fácil extender su funcionalidad. Considera la posibilidad de utilizar métodos plantilla o estrategias para manejar casos especiales como instalaciones personalizadas o entornos específicos.

## 9. Implementar la clase `CondaDependencyInstaller`
- **Archivo:** `src/install/dependency_manager.py`
- **Descripción:** Implementa una nueva clase `CondaDependencyInstaller` que herede de `DependencyInstaller`. Esta clase debe manejar la instalación de dependencias usando `conda`. Integra esta clase en el patrón de fábrica para la creación de instaladores de dependencias.

## 10. Documentar las nuevas interfaces y patrones
- **Archivo:** `docs/architecture.md`
- **Descripción:** Documenta las nuevas interfaces y patrones de diseño introducidos en el proyecto, como la interfaz `LoggerInterface`, las nuevas clases de instaladores de dependencias, y el uso del patrón de fábrica. Explica cómo estas mejoras cumplen con los principios SOLID.
