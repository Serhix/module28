import pika

import time
import json

from models import Contact

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='send_sms', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def send_message(contact_id):
    '''
    stub function
    '''
    return contact_id


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    send_message(message)
    Contact.objects(id=message.get('id')).update(is_send=True)
    print(f" [x] Received {message}")
    time.sleep(1)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='send_sms', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()