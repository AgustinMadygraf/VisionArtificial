### Lista de Tareas para Implementar SOLID

1. **Implementar Inyección de Dependencias (DIP) en `ImageProcessor`**
   - Crear interfaces para las dependencias en `ImageProcessor` y utilizar inyección de dependencias para mayor flexibilidad y facilidad de prueba.

2. **Refactorizar `ImageProcessor` utilizando el Patrón Strategy (OCP)**
   - Permitir diferentes estrategias de procesamiento de imágenes sin modificar la clase base `ImageProcessor`.

3. **Segregar Interfaces en `ImageProcessor` (ISP)**
   - Dividir la interfaz de `ImageProcessor` en varias interfaces más específicas, asegurando que las clases solo implementen los métodos que necesitan.

4. **Asegurar el Principio de Sustitución de Liskov (LSP) en Clases Derivadas**
   - Revisar las clases derivadas de `ImageProcessor` y asegurarse de que puedan ser sustituidas sin romper la funcionalidad del sistema.

5. **Crear una Clase para Gestionar WebSocket Separadamente (SRP)**
   - Refactorizar la gestión de WebSocket en una clase dedicada, separando esta responsabilidad de `webSocketUtils.js`.

6. **Refactorizar `initializeWebSocket` para Utilizar Inyección de Dependencias (DIP)**
   - Modificar `initializeWebSocket` para aceptar dependencias a través de parámetros o constructor, permitiendo la fácil sustitución en pruebas.

7. **Implementar el Patrón Factory para Crear Instancias de Clases (OCP)**
   - Utilizar el patrón Factory para instanciar clases como `VideoManager`, `ImageProcessor` y `DOMUpdater`, facilitando la extensión futura sin modificar el código existente.

8. **Crear Interfaces para Utilidades de Canvas (ISP)**
   - Dividir las funciones de utilidades de canvas en interfaces específicas para mejorar la claridad y la modularidad.

9. **Refactorizar `main.js` para Mejorar la Legibilidad y la Responsabilidad (SRP)**
   - Dividir la lógica en `main.js` en funciones y módulos más pequeños y específicos para mejorar la legibilidad y la separación de responsabilidades.

10. **Crear Clases Derivadas para Diferentes Tipos de `ImageProcessor` (LSP)**
    - Crear clases derivadas para diferentes tipos de procesamiento de imágenes, asegurándose de que cada una pueda ser utilizada en lugar de la clase base sin problemas.
