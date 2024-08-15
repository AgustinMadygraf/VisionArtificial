# Logger

## 5. [Media Prioridad] Separar la funcionalidad de filtros en sus propios módulos
**Archivo**: `src/logs/exclude_http_logs_filter.py`, `src/logs/info_error_filter.py`  
**Descripción**: Mantener los filtros en módulos separados es correcto, pero hay que revisar si su funcionalidad podría estar mejor organizada o extendida. Crear una base común para los filtros si hay suficiente lógica compartida entre ellos.

## 6. [Media Prioridad] Refactorizar `InfoErrorFilter` para cumplir SRP
**Archivo**: `src/logs/info_error_filter.py`  
**Descripción**: Revisar el `InfoErrorFilter` y considerar si la lógica que filtra mensajes por nivel de log debería dividirse en subclases o métodos adicionales. Esto ayudará a asegurar que cada clase tenga una única responsabilidad clara.

## 7. [Media Prioridad] Crear pruebas unitarias para `LoggerConfigurator`
**Archivo**: `tests/test_logger_configurator.py`  
**Descripción**: Escribir pruebas unitarias que aseguren que `LoggerConfigurator` funciona correctamente con diferentes configuraciones inyectadas por `ConfigLoader`. Cubrir los casos en los que no se encuentra la configuración o es inválida.

## 8. [Media Prioridad] Documentar `LoggerConfigurator` y `ConfigLoader`
**Archivo**: `docs/logger_configurator.md`, `docs/config_loader.md`  
**Descripción**: Crear documentación para `LoggerConfigurator` y `ConfigLoader` que explique cómo usar estas clases, sus responsabilidades, y cómo extenderlas. La documentación debe incluir ejemplos de código.

## 9. [Baja Prioridad] Implementar el patrón de Inversión de Dependencias (DIP)
**Archivo**: `src/logs/config_logger.py`  
**Descripción**: Implementar una interfaz o clase abstracta para `ConfigLoader`, permitiendo que `LoggerConfigurator` dependa de la abstracción en lugar de la implementación concreta. Esto facilitará la inyección de diferentes estrategias de carga de configuración.

## 10. [Baja Prioridad] Revisar la configuración del logger en `logging.json`
**Archivo**: `src/logs/logging.json`  
**Descripción**: Revisar el archivo `logging.json` y asegurarse de que todas las configuraciones sean necesarias y estén optimizadas. Considerar la posibilidad de simplificar o dividir la configuración en diferentes archivos según el entorno (desarrollo, producción, pruebas).





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
