from models.service import Service, Customer
from faker import Faker
from random import randint, choice
import mlab


mlab.connect()

fake = Faker()

#image = ['https://images.pexels.com/photos/883441/pexels-photo-883441.jpeg?auto=compress&cs=tinysrgb&h=650&w=940','https://images.pexels.com/photos/247195/pexels-photo-247195.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940','https://images.pexels.com/photos/220452/pexels-photo-220452.jpeg?auto=compress&cs=tinysrgb&h=650&w=940','https://images.pexels.com/photos/160685/business-lady-business-girl-businessman-160685.jpeg?auto=compress&cs=tinysrgb&h=650&w=940']

# image = ['https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&h=350','https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&h=350','https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&h=350','https://images.pexels.com/photos/716411/pexels-photo-716411.jpeg?auto=compress&cs=tinysrgb&h=350','https://images.pexels.com/photos/91227/pexels-photo-91227.jpeg?auto=compress&cs=tinysrgb&h=350']
# for i in range(5):
#     new_service = Service(name=fake.name(), yob=randint(1990, 2000), gender=0, height=randint(150, 180), phone=fake.phone_number(), address=fake.address(), status= choice([True,False]), image=choice(image), measurements=[randint(50,120),randint(50,120),randint(50,120)], description=fake.text())
#     new_service.save()

# for i in range(100):
#     print('Saving customer', i + 1, "...")
#     new_customer = Customer(name=fake.name(), gender=randint(0,1), email=fake.email(), phone=fake.phone_number(), job=fake.job(), company=fake.company(), contacted=choice([True, False]))
#     new_customer.save()
