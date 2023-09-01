from connect import connect
from datetime import datetime


from mongoengine import Document
from mongoengine.fields import DateTimeField, StringField, BooleanField

    
class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone = StringField()
    optimal_send = StringField(default='email')
    is_send = BooleanField(default=False)
    born_date = DateTimeField()
    address = StringField()
    description = StringField()
    create_at = DateTimeField(default=datetime.now())
