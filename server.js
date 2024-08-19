const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const path = require('path');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Sirve los archivos estáticos (imágenes, CSS, etc.)
app.use('/static', express.static(path.join(__dirname, 'static')));

// Sirve la página web
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Maneja las conexiones WebSocket
wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(message) {
        console.log('Mensaje recibido:', message);

        // Transmite el mensaje a todos los clientes conectados
        wss.clients.forEach(function each(client) {
            if (client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });

    ws.send('Conectado al servidor WebSocket');
});

// Inicia el servidor en el puerto 8080
server.listen(8080, () => {
    console.log('Servidor escuchando en http://localhost:8080');
});
