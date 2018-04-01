from flask import Flask, render_template
app = Flask(__name__)

\
@app.route('/')
def index():
    return render_template('index_intro.html')

@app.route('/user/<username>')
def get_info(username):
    Users = {
        "quy" : {
                    "name" : "Dinh Cong Quy",
                    "age" : 20,
                    "role" : "supporter",
                    "email" : "quy.dc98@gmail.com"
                },
        "tuananh" : {
                    "name" : "Huynh tuan Anh",
                    "age" : 22,
                    "role" : 'teacher',
                    "email" : 'huynhtuan21895@gmail.com'
                    },
        "minhduc" : {
                    "name" : "Pham Minh Duc",
                    "age" : 19,
                    "role" : 'student',
                    "email" : "minhduc.096.99@gmail.com"
                    },
        "hoacodethoi" : {
                    "name" : "Vu Duc Hoa",
                    "age" : 19,
                    "role" : "student",
                    "email" : "unknown"
                        }

    }

    if username not in Users:
        return('404 User not found.')
    else:
        return render_template('index.html', Users=Users ,username=username)

if __name__ == '__main__':
  app.run(debug=True)
