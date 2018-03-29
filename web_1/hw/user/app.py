from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return ("chào a Quý lần 3 :v")

@app.route('/user/<username>')
def get_info(username):
    Users = {
        "quy" : {
                    "name" : "Dinh Cong Quy",
                    "age" : 20,
                    "work" : "support"
                },
        "tuananh" : {
                    "name" : "Huynh tuan Anh",
                    "age" : 22,
                    "work" : 'teacher'
                    },
        "minhduc" : {
                    "name" : "Pham Minh Duc",
                    "age" : 19,
                    "work" : 'student'
                    }
    }

    if username not in Users:
        return('404 User not found.')
    else:
        return render_template('index.html', Users=Users ,username=username)

if __name__ == '__main__':
  app.run(debug=True)
