import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds239029.mlab.com:39029/csm-app

host = "ds239029.mlab.com"
port = 39029
db_name = "csm-app"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
