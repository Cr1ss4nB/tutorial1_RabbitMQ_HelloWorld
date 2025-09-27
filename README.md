# RabbitMQ Tutorial - Hello World (Python)

- **Cristian Andrés Basto Largo - 202010495**

Prueba taller  del capítulo 1 del tutorial oficial de RabbitMQ utilizando Python y Docker.

## Requisitos
- Docker Compose
- Python 3.12+
- Librería [pika](https://pypi.org/project/pika/)

## Archivos incluidos
- `docker-compose.yml`: configuración de RabbitMQ con plugin de administración.
- `send.py`: script que envía mensajes a la cola.
- `receive.py`: script que recibe mensajes de la cola.

## Ejecución
1. Levantar RabbitMQ con Docker Compose.
2. Ejecutar `receive.py` en una terminal.
3. Ejecutar `send.py` en otra terminal.
4. Observar los mensajes enviados y recibidos.

## RabbitMQ Management
- URL: [http://localhost:15672](http://localhost:15672)  
- Usuario: `guest`  
- Contraseña: `guest`  

No se definieron las credenciales, entonces por predeterminado RabbitMQ selecciona como usuario y contraseña guest/guest respectivamente.

## Código fuente

### docker-compose.yml
```
services:
  rabbitmq:
    image: rabbitmq:3.13-management
    container_name: rabbitmq
    ports:
      - "5672:5672"
      - "15672:15672"
    networks:
      - rabbitmq_network
```


La imagen rabbitmq:3.13-management usa la imagen oficial de RabbitMQ con el plugin de administración (para poder entrar al panel web).

puertos:

- 5672: puerto de RabbitMQ para clientes (donde se conecta pika).

- 15672: puerto de la interfaz web de gestión.

### receive.py

Se conecta a RabbitMQ, escucha la cola hello y muestra los mensajes que recibe en la terminal.

```
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaramos la misma cola
channel.queue_declare(queue='hola')

def callback(ch, method, properties, body):
    print(f" [x] Recibido {body}")

channel.basic_consume(queue='hola',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Esperando mensaje. Para salir ejecute ctrl + C')
channel.start_consuming()

```
### send.py

Se conecta a RabbitMQ, declara la cola hello y envía un mensaje "Hello World!".

```
import pika

# conexión a RabbitMQ localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaramos la  cola
channel.queue_declare(queue='hola')

# enviamos el  mensaje
channel.basic_publish(exchange='',
                      routing_key='hola',
                      body='Hola Mundo!')

print(" [x] Enviado 'Hola Mundo!'")
connection.close()
```
Uno publica y el otro consume los mensajes. 

---

## Ejecución y Pruebas

### Ejecutar contenedor

Se hizo el doccker compose up -d --build y se verifico con docker ps para verificar que el contenedor estaba corriendo y escuchando en el puerto.

<img width="1914" height="152" alt="Captura desde 2025-09-26 20-52-39" src="https://github.com/user-attachments/assets/407238e0-16ab-472a-a674-099ee2f82d08" />

### Send.py

Se manda el mensaje

<img width="704" height="93" alt="Captura desde 2025-09-26 20-52-25" src="https://github.com/user-attachments/assets/112dd970-9438-40df-b42f-acfeb643d236" />

### Receive.py

Se recibe o consume el mensaje

<img width="704" height="93" alt="Captura desde 2025-09-26 20-52-20" src="https://github.com/user-attachments/assets/bd91a042-486b-4732-a70e-b635485f2271" />

### RabbitMQ

Se accede al localhost con el puerto 15672. 

#### Login

<img width="856" height="311" alt="Captura desde 2025-09-26 20-46-39" src="https://github.com/user-attachments/assets/6cf535e5-de83-418a-bc0e-890b81d55dc3" />

#### Menú Principal

<img width="1918" height="927" alt="Captura desde 2025-09-26 20-46-56" src="https://github.com/user-attachments/assets/28e21559-ccd4-4d6f-8ffd-8885e80edda7" />

#### Ventana de Queues

<img width="1138" height="478" alt="Captura desde 2025-09-26 20-49-16" src="https://github.com/user-attachments/assets/c45a5c08-770a-4405-afad-d41c305daa4a" />

## Flujo del Sistema

<img width="648" height="472" alt="diagramaSecuencia" src="https://github.com/user-attachments/assets/012b2d93-fd96-4059-8f71-78424fc2f113" />

Este diagrama de secuencia fue hecho con PlantText de PlantUML.
