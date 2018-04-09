from flask import *
from models.service import Service, Customer, User, Order
from datetime import *
from gmail import GMail, Message
import mlab

app = Flask(__name__)
app.secret_key = "sudo"
mlab.connect()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all_services')
def show_all():
    all_services = Service.objects()

    return render_template('search.html', all_services = all_services)

@app.route('/search/<int:gender>')
def search(gender):
    all_services= Service.objects(gender=gender)
    return render_template('search.html', all_services = all_services)


@app.route('/detail/<service_id>')
def get_detail(service_id):
    if 'logged_user' in session:
        all_services = Service.objects.with_id(service_id)
        return render_template('detail.html', all_services=all_services)
    else:
        return redirect(url_for('log_in'))

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

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "GET":
        return render_template('sign_in.html')
    elif request.method == "POST":
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        new_user = User(fullname=fullname,
                        email=email,
                        username=username,
                        password=password)
        new_user.save()
        return redirect(url_for('log_in'))

@app.route('/login', methods=["GET", "POST"])
def log_in():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username_input = form['username']
        password_input = form['password']
        account = User.objects(username=username_input, password=password_input).first()
        if account == None:
            return redirect(url_for('log_in'))
        else:
            session['logged_user'] = str(account['id'])
            return redirect(url_for('index'))
@app.route('/logout')
def logout():
    del session['logged_user']
    return redirect(url_for('index'))

@app.route('/login-admin', methods=["GET", "POST"])
def log_in_admin():
    if request.method == "GET":
        return render_template('login_admin.html')
    elif request.method == "POST":
        form = request.form
        username = form['username_admin']
        password = form['password_admin']

        if username == "admin" and password == "admin":
            session['logged_admin'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login_admin.html')

@app.route('/logout_admin')
def log_out_admin():
    del session['logged_admin']
    return redirect(url_for('index'))


@app.route('/admin')
def admin():
    if 'logged_admin' in session:
        services = Service.objects()
        return render_template('admin.html', services= services)
    else:
        return redirect(url_for('log_in_admin'))

@app.route('/delete/<service_id>')
def delete(service_id):
    services_to_del = Service.objects.with_id(service_id)
    if service_to_del is None:
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
        phone = form['phone']
        height = form["height"]
        gender = form['gender']
        status = form['status']
        new_service = Service(name=name,
                              yob=yob,
                              address=address,
                              phone=phone,
                              height=height,
                              gender=gender,
                              status=status)
        new_service.save()

        return redirect(url_for('admin'))

@app.route('/delete_member')
def delete_all():
    all_services = Service.objects()
    all_services.delete()
    return redirect(url_for('admin'))


@app.route('/order-page')
def show_order():
    all_order = Order.objects(is_accepted=False)
    return render_template('order.html', all_order=all_order)


@app.route('/order-click/<order_id>')
def order(order_id):

        all_order = Order.objects.with_id(order_id)
        all_order.update(set__is_accepted=True)

        user_mail = all_order['user']['email']
        html_content = ''' Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của "Mùa Đông Không Lạnh" '''
        gmail = GMail('tuananhc4e16@gmail.com', '01662518199')
        msg = Message('Mùa Đông Không Lạnh', to= user_mail, html= html_content)
        gmail.send(msg)
        return redirect(url_for('show_order'))

@app.route('/update-service/<service_id>', methods=['GET', 'POST'])
def update(service_id):

    if request.method == "GET":
        all_services = Service.objects.with_id(service_id)
        return render_template('update.html', service=all_services)
    elif request.method == "POST":
        all_services = Service.objects.with_id(service_id)
        form = request.form
        image = form['image']
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        address = form['address']
        phone = form['phone']
        height = form["height"]
        measurements1 = form['measurements1']
        measurements2 = form['measurements2']
        measurements3 = form['measurements3']
        measure= [measurements1, measurements2, measurements3]
        description = form['description']
        status = form['status']
        if status == "True":
            status = True
        else:
            status = False


        all_services.update(set__image=image,
                            set__name=name,
                            set__yob=yob,
                            set__address=address,
                            set__phone=phone,
                            set__height=height,
                            set__description=description,
                            set__measurements=measure,
                            set__gender=gender,
                            set__status=status)
        return redirect(url_for('admin'))

@app.route('/order/<service_id>')
def new_order(service_id):
    user_id = session['logged_user']
    user = User.objects.with_id(user_id)
    service = Service.objects.with_id(service_id)
    time ='{0:%H:%M %d/%m}'.format(datetime.now())
    is_accepted = False
    new_order = Order(service=service,
                      user=user,
                      time=time,
                      is_accepted=is_accepted)
    new_order.save()
    return 'Đã gửi yêu cầu, bấm back để quay lại'
if __name__ == '__main__':
  app.run(debug=True)
