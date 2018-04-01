from models.service import Service
import mlab
mlab.connect()
all_services = Service.objects()

print(all_services[100].name)
