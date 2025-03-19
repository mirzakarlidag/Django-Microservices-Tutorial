import pika

params = pika.URLParameters(
    "amqps://dfxffsbh:ylqnsnleUfjyZ4YlzAiqGKUA0vWP1Pyn@leopard.lmq.cloudamqp.com/dfxffsbh"
)

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="admin", body="Hello")
