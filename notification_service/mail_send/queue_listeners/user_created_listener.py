import json
import pika
import threading
from django.core.mail import send_mail
import os

ROUTING_KEY = os.getenv('USER_CREATED_ROUTING_KEY', 'testing_key')
EXCHANGE = os.getenv('USER_EXCHANGE', 'testing_exchange')
THREADS = 5


class UserCreatedListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.exchange_declare(
            exchange=EXCHANGE, exchange_type='direct')
       # self.channel.queue_declare(queue=QUEUE_NAME, auto_delete=False)
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(
            queue=queue_name, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=THREADS*10)
        self.channel.basic_consume(
            queue=queue_name, on_message_callback=self.callback)

    def callback(self, channel, method, properties, body):
        # print(properties.content_type)
        # print(method)
        if (properties.content_type == "user_created_method"):
            # print(type(body))
            message = json.loads(body)
            send_mail("hello", "hello world", "jugalchanda7@gmail.com",
                      [message['email']], fail_silently=False)
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        print("user created listener started")
        self.channel.start_consuming()
