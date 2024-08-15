
### Tarea 1: Verificar Configuración de Logger
- **Archivo a Modificar:** `src/logs/config_logger.py`
- **Descripción:**
  - Revisa la configuración del logger, especialmente la sección que configura el `ssl_file_handler`. Asegúrate de que el nivel del logger esté configurado correctamente (`DEBUG`, `INFO`, etc.) para capturar todos los eventos necesarios.
  - Verifica que la ruta del archivo de log sea correcta y que se tengan los permisos necesarios para escribir en él.

### Tarea 2: Revisar la Implementación del Logger en `SSLService`
- **Archivo a Modificar:** `src/services/ssl_service.py`
- **Descripción:**
  - Asegúrate de que el logger se esté utilizando correctamente en el servicio SSL. Revisa las llamadas al logger y verifica que todos los eventos críticos (errores, advertencias, información) estén siendo registrados.
  - Si es necesario, añade más registros de depuración para capturar más detalles sobre la ejecución del servicio.

### Tarea 3: Validar Rutas y Permisos de los Archivos de Log
- **Archivo a Revisar:** `src/logs/logging.json`
- **Descripción:**
  - Verifica que la ruta especificada en `filename` para `ssl_file_handler` sea correcta y asegúrate de que el archivo `ssl_events.log` existe y tiene los permisos adecuados para ser escrito por el proceso que corre la aplicación.
  - Si el archivo no existe, intenta crearlo manualmente o ajusta la configuración para que se cree automáticamente.

### Tarea 4: Implementar Pruebas para el Servicio SSL
- **Archivo a Crear/Modificar:** `src/tests/test_ssl_service.py` (o en un archivo de pruebas existente)
- **Descripción:**
  - Crea pruebas unitarias que verifiquen la correcta generación y validación de certificados en el `SSLService`.
  - Incluye casos de prueba donde los certificados sean inválidos o estén ausentes, y verifica que los logs correspondientes se generen en el archivo de log.

### Tarea 5: Verificar la Carga del Logger al Iniciar el Servidor
- **Archivo a Modificar:** `src/main.py`
- **Descripción:**
  - Asegúrate de que el logger esté configurado y listo para su uso antes de que se inicialicen los servicios SSL. Esto puede incluir mover la configuración del logger más arriba en la secuencia de inicialización.
  - Añade un log inicial justo después de la configuración del logger para confirmar que el logger está operativo.

### Tarea 6: Aumentar el Nivel de Verbosidad en los Logs
- **Archivo a Modificar:** `src/logs/config_logger.py`
- **Descripción:**
  - Temporalmente, ajusta el nivel de log del `ssl_file_handler` a `DEBUG` para asegurar que todos los eventos posibles se registren. Esto te ayudará a identificar cualquier problema que podría estar siendo pasado por alto debido a un nivel de log más restrictivo.

### Tarea 7: Reiniciar y Monitorear
- **Archivo a Revisar:** N/A
- **Descripción:**
  - Después de realizar los cambios, reinicia el servidor y monitorea el archivo `ssl_events.log` para ver si ahora se registran los eventos esperados. Si aún está vacío, revisa los permisos y considera activar logs en consola para comparación.
