from flask import Flask


"""
Para ejecutar la app de Flask necesitamos un servidor web.
Flask proporciona uno para desarrollo pero necesitamos
un par de variables de entorno.

- Linux/Mac
  export FLASK_APP=hello     (hello es el nombre del archivo sin extensión)
  export FLASK_ENV=development    (puede ser también "production")

- Windows
  set FLASK_APP=hello
  set FLASK_ENV=development
"""

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/hola')
def hola():
    return "Hola, soy Flask. Y tú, ¿cómo te llamas?"


@app.route('/adios')
def otra():
    return "Hasta luego!"