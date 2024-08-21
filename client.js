// En un dispositivo remoto con Node.js
const WebSocket = require('ws');

const socket = new WebSocket('ws://192.168.1.114:8080');

socket.onopen = function() {
    let message = '%Alice#android#Socket#p#gestos#excited%';
    socket.send(message.toString());
    // Cambia la imagen a "feliz.png"
};

socket.onmessage = function(event) {
    console.log('Respuesta del servidor:', event.data);
};
