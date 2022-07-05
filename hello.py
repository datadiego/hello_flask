from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/hola')
@app.route('/index')
def hola():
    return ":)"

@app.route('/adios')
def otra():
    return "Hasta luego"