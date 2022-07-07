from flask import render_template

from . import app
from .models import ListaMovimientos


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)


@app.route('/nuevo')
def nuevo():
    return render_template("nuevo.html")


@app.route('/modificar')
def actualizar():
    return "Actualizar movimiento"


@app.route('/borrar')
def borrar():
    return "Borrar movimiento"
