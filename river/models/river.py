from mongoengine import *

class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
