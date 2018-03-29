from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():

    posts = [
        {
        'title' : 'abc',
        'content' : 'edf',
        'author' : 'ghj',
        'gender' : 1
        },
        {
        'title' : '23423',
        'content' : '23555',
        'author' : '2345232',
        'gender' : 0
        }
        ]

    return render_template('index.html',
                            posts=posts)



@app.route('/hello')
def hello():
    return "Hello C4E16"


@app.route('/hi/<name>/<age>')
def hi(name,age):
    return"hi " + name + " you are " + age


@app.route('/sum/<int:num1>/<int:num2>')
def calc(num1, num2):
    return str(num1 + num2)


if __name__ == '__main__':
  app.run(debug=True)
