from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return ('em lại chào a Quý :v')

# without using render_template, bỏ cmt ra check a nhá :v
'''
@app.route('/bmi/<int:weight>/<int:height>')
def calc(weight, height):

    height_m = height / 100
    BMI_float = float(weight / (height_m * height_m))
    BMI = round(BMI_float, 2)
    if BMI < 16:
        return ('your BMI is: '+ str(BMI) +' your are severely underweigh')
    elif BMI < 18.5:
        return ('your BMI is: '+ str(BMI) +' you are underweigh')
    elif BMI < 25:
        return ('your BMI is: '+ str(BMI) +' you are normal')
    elif BMI < 30:
        return ('your BMI is: '+ str(BMI) +' you are overweight')
    else:
        return ('your BMI is: '+ str(BMI) +' you are obese')

'''

#with using render_template: cái này cũng bỏ cmt nốt :)))
'''
@app.route('/bmi/<int:weight>/<int:height>')
def calc(weight, height):
    height_m = height / 100
    BMI_float = float(weight / (height_m * height_m))
    BMI = round(BMI_float, 2)
    return render_template('index.html', BMI=BMI)'''


if __name__ == '__main__':
  app.run(debug=True)
