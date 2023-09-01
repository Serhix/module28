import pika
import faker

from random import choice


from datetime import datetime
import sys
import json

from models import Contact

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.exchange_declare(exchange='send_messages', exchange_type='direct')
channel.queue_declare(queue='send_email', durable=True)
channel.queue_bind(exchange='send_messages', queue='send_email')
channel.queue_declare(queue='send_sms', durable=True)
channel.queue_bind(exchange='send_messages', queue='send_sms')

fake_data = faker.Faker('uk_UA')

MAX_CONTACTS = 30


def main():
    # for _ in range(MAX_CONTACTS):
    #     Contact(
    #         fullname=fake_data.name(),
    #         email=fake_data.email(),
    #         phone=fake_data.phone_number(),
    #         optimal_send=choice(['email', 'sms']),
    #         born_date=fake_data.date_of_birth(),
    #         address=fake_data.address(),
    #         description=fake_data.text(),
    #     ).save()
    #
    for contact in Contact.objects.all():
        message = {
            "id": str(contact.id)
        }

        if contact.phone and contact.optimal_send == 'sms':
            channel.basic_publish(
                exchange='send_messages',
                routing_key='send_sms',
                body=json.dumps(message).encode(),
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ))
        else:
            channel.basic_publish(
                exchange='send_messages',
                routing_key='send_email',
                body=json.dumps(message).encode(),
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                ))

        print(" [x] Sent %r" % message)
    connection.close()
    
    
if __name__ == '__main__':
    main()
