
### 9. **Modificar `http_service.py`**
   - **Archivo:** `src/services/http_service.py`
   - **Descripción:** Asegúrate de que los servicios HTTP estén utilizando el contexto SSL correcto, especialmente si se utiliza un servicio específico para manejar las solicitudes HTTPS.

### 10. **Modificar `config_logger.py`**
   - **Archivo:** `src/logs/config_logger.py`
   - **Descripción:** Añade configuraciones para registrar eventos específicos relacionados con SSL, especialmente en cuanto a errores que puedan surgir al cargar o verificar certificados SSL emitidos por una CA de confianza.