from flask import Flask, render_template
from models.river import river
import mlab
app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/africa")
def get_africa():
    all_rivers = river.objects(continent="Africa")
    return render_template('rivers.html', all_rivers=all_rivers)

@app.route("/S.America")
def get_s_america():
    all_rivers = river.objects(continent="S. America", length__lt=1000)
    return render_template('rivers.html', all_rivers=all_rivers)
if __name__ == '__main__':
  app.run(debug=True)
