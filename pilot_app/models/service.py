from mongoengine import *

#creat collection, design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() # 0: female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = StringField()
    description = StringField()
    measurements = ListField()

class Customer(Document):
    name = StringField()
    gender = IntField()
    email = EmailField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()

class User(Document):
    fullname = StringField()
    email = EmailField()
    username = StringField()
    password = StringField()

class Order(Document):
    service = ReferenceField(Service)
    user = ReferenceField(User)
    time = StringField()
    is_accepted = BooleanField()
