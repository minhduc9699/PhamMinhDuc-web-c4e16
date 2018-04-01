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
