from flask import *
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
def customer():
    #Render all customers: (bỏ cmt để kiểm tra a eii :v)
     all_customers = Customer.objects()
     return render_template('customer.html', all_customers = all_customers)
@app.route('/list_customer/<int:gender>')
def get_customer(gender):

    #render 10 male uncontacted customers:
    uncontacted_customers = Customer.objects[:10](gender=gender, contacted=False)
    return render_template('customer.html', all_customers=uncontacted_customers)


@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services= services)


@app.route('/delete/<service_id>')
def delete(service_id):
    services_to_del = Service.objects.with_id(service_id)
    if service_id is None:
        return('Id not found')
    else:
        services_to_del.delete()
        return redirect(url_for('admin'))

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        new_service = Service(name=name, yob=yob, address=address)
        new_service.save()

        return redirect(url_for('admin'))



if __name__ == '__main__':
  app.run(debug=True)
