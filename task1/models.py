from connect import connect


from mongoengine import Document, CASCADE
from mongoengine.fields import DateTimeField, ListField, StringField, ReferenceField

    
class Author(Document):
    fullname = StringField(required=True)
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()
    
class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote_ = StringField(required=True)
    tags = ListField(StringField())
    