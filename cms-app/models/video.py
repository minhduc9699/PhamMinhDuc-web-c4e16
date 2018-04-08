from mongoengine import *

class Video(Document):
    title = StringField()
    thumbnail = StringField()
    views = IntField()
    link = StringField()
    youtubeid = StringField()
