import pika

params = pika.URLParameters('amqps://zvhfnqdw:VcneOBF3Qqf-rYGyewkAJleHcyduwmT_@gull.rmq.cloudamqp.com/zvhfnqdw')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='dbname')

def callback( ch, method, properties, body):
    print('Received in dbname')
    print(body)

channel.basic_consume(queue='dbname', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()