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
