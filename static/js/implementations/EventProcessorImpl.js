// static/js/implementations/EventProcessorImpl.js
import EventHandlingInterface from '../interfaces/eventHandlingInterface.js';

export default class EventProcessorImpl extends EventHandlingInterface {
    handleEvent(event) {
        // Implementación del manejo de eventos
        console.log(event); // Ejemplo de uso de la variable 'event'
    }
}