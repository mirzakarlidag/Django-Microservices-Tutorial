import pika

params = pika.URLParameters(
    "amqps://dfxffsbh:ylqnsnleUfjyZ4YlzAiqGKUA0vWP1Pyn@leopard.lmq.cloudamqp.com/dfxffsbh"
)

connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    print("Received in main")


channel.basic_consume(queue="main", on_message_callback=callback)

print("Started Consuming")

channel.start_consuming()

channel.close()
