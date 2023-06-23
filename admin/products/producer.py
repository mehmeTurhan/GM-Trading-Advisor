import pika, json

params = pika.URLParameters('amqps://zvhfnqdw:VcneOBF3Qqf-rYGyewkAJleHcyduwmT_@gull.rmq.cloudamqp.com/zvhfnqdw')

connection = pika.BlockingConnection(params)

channel = connection.channel()
def publish(method, body):
    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)