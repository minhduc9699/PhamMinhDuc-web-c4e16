from flask import Flask, render_template
from models.service import Service, Customer
import mlab

app = Flask(__name__)
mlab.connect()


# #creat a Document
# new_service = Service(name="Linh ka", yob=2002, gender=0, height=148, phone="098124141", address="hà nội", status = False)
#
#
# new_service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_services= Service.objects(gender=gender)


    return render_template('search.html', all_services = all_services)

@app.route('/customer')
def get_customer():
    #Render all customers: (bỏ cmt để kiểm tra a eii :v)

        # all_customers = Customer.objects()
        # return render_template('customer.html', all_customers = all_customers)

    #render 10 male uncontacted customers:
    uncontacted_customers = Customer.objects(gender=1, contacted=False).limit(10)
    return render_template('customer.html', all_customers=uncontacted_customers)


if __name__ == '__main__':
  app.run(debug=True)
