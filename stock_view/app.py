import flask
from flask import render_template, redirect, url_for

app = flask.Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    return render_template("home.html", stock_code=323410, stock_name='카카오뱅크')

@app.route("/code/<code>")
def get_stock_code(code):
    return render_template("home.html", stock_code=code)

@app.route("/name/<name>")
def get_stock_name(name):
    return render_template("home.html", stock_name=name)

if __name__ == '__main__':
    
    app.run(host="localhost", port=8000, debug=True)