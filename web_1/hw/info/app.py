from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return ('Em chào anh Quý =))')

@app.route('/about-me')
def intro():
    infos = {
        "name" : "Phạm Minh Đức",
        "work" : "unkown",
        "school" : "Hanu",
        "hairstyle" : "DreadLocks",
        "talent" : "coding overnight :v"
    }
    return render_template('index.html', infos=infos)


@app.route('/school')
def access():
    return redirect('http://techkids.vn', code=302)

if __name__ == '__main__':
    app.run(debug=True)
