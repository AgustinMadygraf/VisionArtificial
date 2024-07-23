# Tareas Pendientes

## 1. Visualizar en la Terminal de Python todos los `console.log` que se vayan generando

### Descripción
Implementar una funcionalidad que permita redirigir los mensajes de `console.log` del navegador a la terminal donde se está ejecutando el servidor Python.

### Pasos
1. Instalar el paquete `websockets` en Python:
   ```bash
   pip install websockets
   ```

2. Configurar un servidor WebSocket en `server.py` que reciba los mensajes de `console.log` del navegador.

3. Modificar `script.js` para enviar los mensajes de `console.log` al servidor WebSocket.

4. Probar que los mensajes de `console.log` se muestren en la terminal de Python.

## 2. Enviar solicitudes HTTP basadas en el desvío

### Descripción
Si el desvío es mayor a 10, realizar una solicitud HTTP a `http://192.168.0.184/ena_f`. Si el desvío es menor a -10, realizar una solicitud HTTP a `http://192.168.0.184/ena_r`.

### Pasos
1. Modificar el método `vertLineInCanvas` en `imageProcessor.js` para calcular el desvío.

2. Usar la API `fetch` de JavaScript para enviar solicitudes HTTP cuando el desvío sea mayor que 10 o menor que -10.

3. Probar que las solicitudes HTTP se envían correctamente según el valor del desvío.
