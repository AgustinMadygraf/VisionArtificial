# TODO

- [x] **Crear archivo:** `src/views/handlers/route_handler.py`  
  **Descripción:**  
  Mover la clase `RouteHandler` a este nuevo archivo. Esta clase servirá como base para los manejadores de rutas personalizados.

- [x] **Crear archivo:** `src/views/handlers/root_handler.py`  
  **Descripción:**  
  Mover la clase `RootHandler` a este nuevo archivo. Este archivo manejará las solicitudes HTTP para la ruta raíz `/`.

- [x] **Crear archivo:** `src/views/handlers/local_ip_handler.py`  
  **Descripción:**  
  Mover la clase `LocalIPHandler` a este nuevo archivo. Este archivo se encargará de responder con la IP local en la ruta `/local-ip`.

- [x] **Crear archivo:** `src/views/server/route_registry.py`  
  **Descripción:**  
  Mover la clase `RouteRegistry` a este nuevo archivo. Este archivo centralizará el registro y la gestión de rutas personalizadas.

- [x] **Crear archivo:** `src/views/server/request_handler.py`  
  **Descripción:**  
  Mover la clase `MyHTTPRequestHandler` a este nuevo archivo. Este archivo manejará las solicitudes HTTP, utilizando las rutas personalizadas registradas en `RouteRegistry`.

- [x] **Actualizar archivo:** `src/views/http_server.py`  
  **Descripción:**  
  Eliminar las clases que han sido movidas a otros módulos y actualizar las importaciones correspondientes para reflejar la nueva estructura modular.

- [x] **Crear archivo:** `src/views/server/http_server.py`  
  **Descripción:**  
  Mover la clase `HTTPServer` a este nuevo archivo. Esta clase iniciará el servidor HTTP con soporte SSL y utilizará las rutas y manejadores personalizados.

- [x] **Actualizar archivo:** `src/views/__init__.py`  
  **Descripción:**  
  Actualizar o crear este archivo para facilitar la importación de los nuevos módulos en `src/views`, centralizando las importaciones necesarias para el servidor HTTP.

- [ ] **Pruebas unitarias:**  
  **Descripción:**  
  Crear y/o actualizar pruebas unitarias para cada uno de los módulos nuevos y asegurarse de que todo el sistema funcione correctamente después de la modularización.

