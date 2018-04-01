from flask import Flask, render_template
from models.service import Service
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
    all_services= Service.objects(gender=gender, yob__lte=1998, address__icontains='hà nội')


    return render_template('search.html', all_services = all_services)

if __name__ == '__main__':
  app.run(debug=True)
