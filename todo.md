1. **Separar la lógica de manejo de solicitudes HTTP en clases específicas**:
   - Crear clases separadas para manejar diferentes tipos de solicitudes (GET, POST, etc.) y rutas específicas (`/`, `/local-ip`, etc.).
   - **Archivos a modificar/crear**: `src/views/http_server.py`, `src/views/handlers.py`

2. **Aplicar el principio de Responsabilidad Única (SRP)**:
   - Dividir la clase `MyHTTPRequestHandler` en múltiples clases, cada una con una única responsabilidad, como manejar la IP local, manejar pruebas, etc.
   - **Archivos a modificar/crear**: `src/views/http_server.py`, `src/views/handlers.py`

3. **Utilizar Inyección de Dependencias (DI)**:
   - Inyectar dependencias como `ServerUtility` y `LoggerConfigurator` en lugar de instanciarlas directamente dentro de las clases.
   - **Archivos a modificar**: `src/views/http_server.py`, `src/views/handlers.py`

4. **Implementar Interfaces para el manejo de solicitudes**:
   - Definir interfaces para el manejo de solicitudes HTTP y asegurarse de que las clases las implementen, facilitando la extensión y modificación del comportamiento.
   - **Archivos a modificar/crear**: `src/views/handlers.py`, `src/interfaces/request_handler_interface.py`

5. **Aplicar el principio de Sustitución de Liskov (LSP)**:
   - Asegurarse de que las clases derivadas puedan sustituir a las clases base sin alterar el comportamiento esperado del programa.
   - **Archivos a modificar/crear**: `src/views/handlers.py`, `src/interfaces/request_handler_interface.py`

6. **Utilizar el principio de Segregación de Interfaces (ISP)**:
   - Crear interfaces más pequeñas y específicas para diferentes funcionalidades en lugar de una interfaz grande y monolítica.
   - **Archivos a modificar/crear**: `src/interfaces/request_handler_interface.py`

7. **Aplicar el principio de Inversión de Dependencias (DIP)**:
   - Depender de abstracciones en lugar de implementaciones concretas, permitiendo cambiar las implementaciones sin afectar el código que las utiliza.
   - **Archivos a modificar**: `src/views/http_server.py`, `src/views/handlers.py`

8. **Crear una clase de configuración para el servidor**:
   - Encapsular la configuración del servidor (dirección, clase de manejador, configuración SSL) en una clase separada para mejorar la modularidad y la reutilización.
   - **Archivos a modificar/crear**: `src/views/http_server.py`, `src/config/server_config.py`

9. **Implementar pruebas unitarias para cada clase y método**:
   - Escribir pruebas unitarias para cada clase y método, asegurando que cada componente funcione correctamente de manera aislada.
   - **Archivos a modificar/crear**: `tests/test_http_server.py`, `tests/test_handlers.py`, `tests/test_server_config.py`

10. **Refactorizar el manejo de video en el frontend**:
    - Separar la lógica de manejo de video y botones en clases distintas, aplicando el principio de Responsabilidad Única y facilitando la prueba y mantenimiento del código.
    - **Archivos a modificar/crear**: `static/js/videoManager.js`, `static/js/buttonManager.js`, `static/js/videoStreamManager.js`











- [ ] **Generación de Certificados SSL mediante Python**
  - **Descripción**: Implementar un script en Python para generar certificados SSL automáticamente. Este script debe crear una clave privada y un certificado autofirmado, y guardarlos en el directorio raíz del proyecto.
  - **Archivo**: Crear un nuevo archivo `src/generate_ssl_certificates.py`

### Lista de Tareas para Implementar SOLID en JS

- [x] **Implementar Inyección de Dependencias (DIP) en `ImageProcessor`**
  - Crear interfaces para las dependencias en `ImageProcessor` y utilizar inyección de dependencias para mayor flexibilidad y facilidad de prueba.

- [x] **Refactorizar `ImageProcessor` utilizando el Patrón Strategy (OCP)**
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

- [x] **División de Responsabilidades en `ProjectInstaller`**:
  - **Descripción**: Dividir la clase `ProjectInstaller` en varias clases con responsabilidades específicas: una clase para la instalación, otra para la creación de accesos directos y otra para la creación de archivos BAT.
  - **Archivo**: `src/installer_utils.py`

- [x] **Inyección de Dependencias**:
  - **Descripción**: Implementar inyección de dependencias para las clases que dependen de configuraciones o servicios externos, permitiendo mayor flexibilidad y facilidad de pruebas.
  - **Archivo**: Varios archivos, comenzando por `src/store_data.py` y `src/views/websocket_server.py`

- [x] **Segregación de Interfaces**:
  - **Descripción**: Dividir interfaces grandes en interfaces más pequeñas y específicas. Asegurar que cada clase implemente solo las interfaces que realmente necesita.
  - **Archivo**: Varios archivos, a revisar durante la implementación.

- [x] **Apertura/Cierre en `ShortcutManager`**:
  - **Descripción**: Rediseñar la clase `ShortcutManager` para permitir la extensión de funcionalidades sin modificar la clase base. Esto puede implicar el uso de patrones de diseño como Estrategia o Composición.
  - **Archivo**: `src/installer_utils.py`

- [x] **Pruebas Unitarias para Cada Componente**:
  - **Descripción**: Escribir pruebas unitarias para cada clase y método, asegurando que cada componente cumple con su responsabilidad específica.
  - **Archivo**: Crear archivos de prueba en `tests/`, por ejemplo, `tests/test_installer_utils.py`

- [x] **Refactorización de `WebSocketServer`**:
  - **Descripción**: Refactorizar la clase `WebSocketServer` para cumplir con los principios SOLID, especialmente el principio de Responsabilidad Única y el principio de Inversión de Dependencias.
  - **Archivo**: `src/views/websocket_server.py`

- [x] **Modularización de Configuraciones**:
  - **Descripción**: Separar las configuraciones en módulos distintos, por ejemplo, configuraciones de base de datos, configuraciones de red, etc.
  - **Archivo**: Crear archivos de configuración específicos en `src/config/`

- [x] **Rediseño de `store_data.py`**:
  - **Descripción**: Rediseñar `store_data.py` para separar claramente las responsabilidades de extracción de datos, procesamiento de datos y almacenamiento de datos.
  - **Archivo**: `src/store_data.py`

- [x] **Documentación del Código y las Clases**:
  - **Descripción**: Agregar documentación detallada en cada clase y método, explicando su propósito y cómo cumple con los principios SOLID.
  - **Archivo**: Todos los archivos, comenzando por los más complejos como `src/installer_utils.py` y `src/views/websocket_server.py`



# Instalador

- [x] **1. Refactorizar `DependencyChecker`:** Dividir esta clase en dos, una que verifique las dependencias (`DependencyVerifier`) y otra que las instale (`DependencyInstaller`).

- [ ] **2. Crear una interfaz para `PipUpdater`:** Implementar una interfaz para `PipUpdater` que permita a `DependencyChecker` depender de una abstracción en lugar de una clase concreta.

- [ ] **3. Aplicar el Patrón Estrategia en `DependencyChecker`:** Implementar un patrón de estrategia para la instalación de dependencias, permitiendo que diferentes estrategias de instalación sean intercambiables.

- [ ] **4. Crear Interfaz para `ProjectInstaller`:** Definir una interfaz o clase abstracta para las operaciones relacionadas con el instalador del proyecto, permitiendo la extensión sin modificar la clase base.

- [ ] **5. Segregar la Interfaz `DependencyInstaller`:** Dividir la interfaz `DependencyInstaller` en interfaces más específicas y enfocadas en tareas concretas.

- [ ] **6. Crear Clase Abstracta para `PipUpdater`:** Implementar una clase base abstracta para el actualizador de `pip` que permita diferentes formas de actualizar `pip`.

- [ ] **7. Inversión de Dependencias en `DependencyChecker`:** Invertir las dependencias en `DependencyChecker` para que dependa de interfaces o abstracciones en lugar de implementaciones concretas.

- [ ] **8. Crear Pruebas Unitarias para Nuevas Interfaces:** Desarrollar pruebas unitarias para cada una de las nuevas interfaces o clases abstractas introducidas para garantizar su correcto funcionamiento.

- [ ] **9. Documentar Clases Refactorizadas:** Documentar cada clase e interfaz nueva para asegurar la comprensión y facilidad de uso en el futuro.

- [ ] **10. Crear Mock Tests para `PipUpdater`:** Implementar pruebas automatizadas utilizando mocks para `PipUpdater` y `DependencyInstaller` para verificar su integración con `DependencyChecker` sin modificar el entorno de desarrollo.
