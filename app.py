from flask import Flask, render_template, redirect, url_for, request
from backend import predict
# Reference:
# https://pythonspot.com/flask-web-app-with-python/
# https://www.tutorialspoint.com/index.html

## Heroku reference
# https://github.com/datademofun/heroku-basic-flask

# https://simple-text-prediction.herokuapp.com/
app = Flask(__name__)


@app.route("/")
def index():
    output = None
    return render_template(
        "index_page.html",**locals()
    )



@app.route('/index_page',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      textFromWeb = request.form['nm']
      out = predict(textFromWeb)
      return redirect(url_for('show_result',result = out))

@app.route('/out/<string:result>')
def show_result(result):
    input, output = result.split(placeholder)
    return render_template(
        "index_page.html",**locals()
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')