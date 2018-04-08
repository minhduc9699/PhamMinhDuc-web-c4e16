from models.service import Service
import mlab
mlab.connect()



# all_services = Service.objects()
# all_services.delete()

# print(all_services[100].name)
# id_to_find = '5ac08eb336b8e40a64c5759d'
#
# Service = Service.objects.with_id(id_to_find)
#
# if Service is None:
#     print('Service not found')
# else:
#     #kieu_anh.delete()
#     #Update data
#     Service.update(set__address="Trần Duy Hưng")
#     Service.reload()
#     print(Service.address)
