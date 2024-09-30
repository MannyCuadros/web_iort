import asyncio
import websockets

#ip = "127.0.0.1"
ip = "192.168.1.114"
#puerto = 5000
puerto = 8080

emotions = ["angry",
            "embarrassed",
            "excited",
            "happy",
            "neutral",
            "sad",
            "scared",
            "surprised"]

# Función para enviar el gesto seleccionado al servidor WebSocket
async def enviar_gesto():
    uri = "ws://" + ip + ":" + str(puerto)  # Dirección del servidor WebSocket
    print("uri: ", uri)
    async with websockets.connect(uri) as websocket:
        while True:
            # Menú de selección
            print("Elige un gesto:")
            print("0. Angry")
            print("1. Embarrassed")
            print("2. Excited")
            print("3. Happy")
            print("4. Neutral")
            print("5. Sad")
            print("6. Scared")
            print("7. Surprised")
            print("8. Exit")

            opcion = input("Ingresa el número de tu elección: ")

            if opcion == "8":
                print("Saliendo...")
                break
            elif (int(opcion) >= 0 and int(opcion) <= 7):
                mensaje = "%Alice#Android#Socket#p#gestos#" + emotions[int(opcion)] + "%"
                print(mensaje)
            else:
                print("Opción no válida, por favor intenta de nuevo.")
                continue

            # Enviar el mensaje al servidor WebSocket
            await websocket.send(mensaje)
            print(f"Gesto '{mensaje}' enviado.")

# Ejecutar la función de forma asincrónica
asyncio.get_event_loop().run_until_complete(enviar_gesto())
