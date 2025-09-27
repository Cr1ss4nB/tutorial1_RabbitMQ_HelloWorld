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
