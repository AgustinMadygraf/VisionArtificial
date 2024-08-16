# To Do List
1. **Tarea:** Crear pruebas unitarias para `main.py`.
   - **Archivo a Crear:** `tests/test_main.py`
   - **Descripción Detallada:** Desarrollar pruebas unitarias que validen la correcta inicialización y ejecución del servidor HTTP y WebSocket, asegurándose de que los servicios `SSLService`, `HTTPService`, y `WebSocketServer` se configuren y se inicien correctamente. Incluir pruebas para los posibles errores que podrían ocurrir durante la inicialización del servidor.

2. **Tarea:** Desarrollar pruebas unitarias para `http_service.py`.
   - **Archivo a Crear:** `tests/test_http_service.py`
   - **Descripción Detallada:** Crear pruebas unitarias que verifiquen los métodos `fetch_data` y `send_request` de la clase `HTTPService`. Asegurarse de que las solicitudes HTTP manejen correctamente los reintentos y los tiempos de espera, y que los errores se registren adecuadamente.

3. **Tarea:** Implementar pruebas unitarias para `websocket_server.py`.
   - **Archivo a Crear:** `tests/test_websocket_server.py`
   - **Descripción Detallada:** Desarrollar pruebas que cubran la inicialización y manejo de conexiones en `WebSocketServer`. Incluir pruebas para validar que las conexiones se manejen correctamente y que los mensajes se procesen de manera adecuada, así como para verificar la correcta integración con `SSLService`.

4. **Tarea:** Agregar pruebas de integración para validar la interacción de `WebSocketServer` con `SSLService` y `WebSocketHandler`.
   - **Archivo a Crear:** `tests/test_integration_websocket.py`
   - **Descripción Detallada:** Crear pruebas de integración que simulen el flujo completo de inicio del servidor WebSocket, manejo de conexiones SSL, y el procesamiento de mensajes a través del `WebSocketHandler`. Validar la correcta colaboración entre estos componentes y su manejo de errores.

5. **Tarea:** Reestructurar los archivos de prueba actuales para separar pruebas unitarias y de integración.
   - **Archivo a Modificar:** `tests/`
   - **Descripción Detallada:** Reorganizar los archivos de prueba existentes para diferenciar claramente entre pruebas unitarias y de integración. Crear subcarpetas si es necesario (`unit` y `integration`), y mover los archivos de prueba a las carpetas correspondientes. Asegurarse de que las pruebas se ejecuten correctamente en esta nueva estructura.

6. **Tarea:** Revisar y optimizar el uso de mocks en las pruebas actuales, especialmente en `test_install.py`.
   - **Archivo a Modificar:** `tests/test_install.py`
   - **Descripción Detallada:** Evaluar el uso actual de mocks dentro de `test_install.py` para asegurarse de que no se están omitiendo comportamientos críticos del código real. Optimizar los mocks para reflejar mejor los casos de uso reales y, cuando sea necesario, sustituir mocks con pruebas más cercanas a la integración.

7. **Tarea:** Agregar pruebas unitarias para todos los módulos en `services`, `utils`, y `views` que no tienen cobertura actual.
   - **Archivos a Crear:** 
     - `tests/test_ssl_service.py`
     - `tests/test_server_utility.py`
     - `tests/test_http_server.py`
   - **Descripción Detallada:** Desarrollar pruebas unitarias para los módulos en `services`, `utils`, y `views` que actualmente carecen de cobertura. Asegurarse de que cada método crítico esté cubierto, incluyendo la gestión de errores y validaciones dentro de estos módulos.

8. **Tarea:** Implementar un script de cobertura que identifique áreas de código sin pruebas y optimice la cobertura total.
   - **Archivo a Crear:** `scripts/check_coverage.sh`
   - **Descripción Detallada:** Crear un script de shell (`check_coverage.sh`) que ejecute `pytest` con la opción de cobertura (`--cov`). El script debería generar un reporte de cobertura indicando qué áreas del código no están cubiertas por las pruebas y sugerir mejoras. Incluir instrucciones para ejecutar el script en el archivo `README.md`.

9. **Tarea:** Verificar que las pruebas de registro de logs en `test_logs.py` cubran todos los niveles y filtros de logs.
   - **Archivo a Modificar:** `tests/test_logs.py`
   - **Descripción Detallada:** Revisar y extender las pruebas existentes en `test_logs.py` para asegurar que todos los niveles de logs (DEBUG, INFO, WARNING, ERROR) y todos los filtros (como `ExcludeHTTPLogsFilter` y `InfoErrorFilter`) estén correctamente probados. Añadir casos de prueba adicionales si es necesario.

10. **Tarea:** Documentar la estructura y el flujo de las pruebas para facilitar la contribución y mantenimiento futuro.
    - **Archivo a Modificar:** `README.md` o `tests/README.md`
    - **Descripción Detallada:** Redactar documentación que describa la estructura de las pruebas, la metodología utilizada (pruebas unitarias, de integración), cómo ejecutar las pruebas, y cómo contribuir con nuevas pruebas. Incluir ejemplos prácticos para ayudar a futuros desarrolladores a entender y ampliar el conjunto de pruebas.