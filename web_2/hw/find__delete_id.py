from models.service import Service
import mlab

id_to_find = '5ac08d8236b8e4026c6f950f'

mlab.connect()
services = Service.objects.get(id= id_to_find).delete()
