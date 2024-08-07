### Lista de Tareas para Implementar SOLID en JS

- [ ] **Implementar Inyección de Dependencias (DIP) en `ImageProcessor`**
  - Crear interfaces para las dependencias en `ImageProcessor` y utilizar inyección de dependencias para mayor flexibilidad y facilidad de prueba.

- [ ] **Refactorizar `ImageProcessor` utilizando el Patrón Strategy (OCP)**
  - Permitir diferentes estrategias de procesamiento de imágenes sin modificar la clase base `ImageProcessor`.

- [ ] **Segregar Interfaces en `ImageProcessor` (ISP)**
  - Dividir la interfaz de `ImageProcessor` en varias interfaces más específicas, asegurando que las clases solo implementen los métodos que necesitan.

- [ ] **Asegurar el Principio de Sustitución de Liskov (LSP) en Clases Derivadas**
  - Revisar las clases derivadas de `ImageProcessor` y asegurarse de que puedan ser sustituidas sin romper la funcionalidad del sistema.

- [ ] **Crear una Clase para Gestionar WebSocket Separadamente (SRP)**
  - Refactorizar la gestión de WebSocket en una clase dedicada, separando esta responsabilidad de `webSocketUtils.js`.

- [ ] **Refactorizar `initializeWebSocket` para Utilizar Inyección de Dependencias (DIP)**
  - Modificar `initializeWebSocket` para aceptar dependencias a través de parámetros o constructor, permitiendo la fácil sustitución en pruebas.

- [ ] **Implementar el Patrón Factory para Crear Instancias de Clases (OCP)**
  - Utilizar el patrón Factory para instanciar clases como `VideoManager`, `ImageProcessor` y `DOMUpdater`, facilitando la extensión futura sin modificar el código existente.

- [ ] **Crear Interfaces para Utilidades de Canvas (ISP)**
  - Dividir las funciones de utilidades de canvas en interfaces específicas para mejorar la claridad y la modularidad.

- [ ] **Refactorizar `main.js` para Mejorar la Legibilidad y la Responsabilidad (SRP)**
  - Dividir la lógica en `main.js` en funciones y módulos más pequeños y específicos para mejorar la legibilidad y la separación de responsabilidades.

- [ ] **Crear Clases Derivadas para Diferentes Tipos de `ImageProcessor` (LSP)**
  - Crear clases derivadas para diferentes tipos de procesamiento de imágenes, asegurándose de que cada una pueda ser utilizada en lugar de la clase base sin problemas.


### Lista de Tareas para Implementar SOLID en Python

- [x] **Refactorización del Logger**:
  - **Descripción**: Crear una clase `LoggerConfigurator` independiente para la configuración del logger, como se mostró en el ejemplo anterior.
  - **Archivo**: `src/logger_config.py`

- [ ] **División de Responsabilidades en `ProjectInstaller`**:
  - **Descripción**: Dividir la clase `ProjectInstaller` en varias clases con responsabilidades específicas: una clase para la instalación, otra para la creación de accesos directos y otra para la creación de archivos BAT.
  - **Archivo**: `src/installer_utils.py`

- [ ] **Inyección de Dependencias**:
  - **Descripción**: Implementar inyección de dependencias para las clases que dependen de configuraciones o servicios externos, permitiendo mayor flexibilidad y facilidad de pruebas.
  - **Archivo**: Varios archivos, comenzando por `src/store_data.py` y `src/views/websocket_server.py`

- [ ] **Segregación de Interfaces**:
  - **Descripción**: Dividir interfaces grandes en interfaces más pequeñas y específicas. Asegurar que cada clase implemente solo las interfaces que realmente necesita.
  - **Archivo**: Varios archivos, a revisar durante la implementación.

- [ ] **Apertura/Cierre en `ShortcutManager`**:
  - **Descripción**: Rediseñar la clase `ShortcutManager` para permitir la extensión de funcionalidades sin modificar la clase base. Esto puede implicar el uso de patrones de diseño como Estrategia o Composición.
  - **Archivo**: `src/installer_utils.py`

- [ ] **Pruebas Unitarias para Cada Componente**:
  - **Descripción**: Escribir pruebas unitarias para cada clase y método, asegurando que cada componente cumple con su responsabilidad específica.
  - **Archivo**: Crear archivos de prueba en `tests/`, por ejemplo, `tests/test_installer_utils.py`

- [ ] **Refactorización de `WebSocketServer`**:
  - **Descripción**: Refactorizar la clase `WebSocketServer` para cumplir con los principios SOLID, especialmente el principio de Responsabilidad Única y el principio de Inversión de Dependencias.
  - **Archivo**: `src/views/websocket_server.py`

- [ ] **Modularización de Configuraciones**:
  - **Descripción**: Separar las configuraciones en módulos distintos, por ejemplo, configuraciones de base de datos, configuraciones de red, etc.
  - **Archivo**: Crear archivos de configuración específicos en `src/config/`

- [ ] **Rediseño de `store_data.py`**:
  - **Descripción**: Rediseñar `store_data.py` para separar claramente las responsabilidades de extracción de datos, procesamiento de datos y almacenamiento de datos.
  - **Archivo**: `src/store_data.py`

- [ ] **Documentación del Código y las Clases**:
  - **Descripción**: Agregar documentación detallada en cada clase y método, explicando su propósito y cómo cumple con los principios SOLID.
  - **Archivo**: Todos los archivos, comenzando por los más complejos como `src/installer_utils.py` y `src/views/websocket_server.py`
