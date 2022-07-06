from flask import render_template
from . import app
from .models import ListaMovimientos


@app.route('/')
def home():
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs = movimientos.movimientos)
@app.route("/nuevo")
def nuevo():
    return "Creación de movimiento"

@app.route("/modificar")
def modificar():
    return "Actualizar"

@app.route("/borrar")
def borrar():
    return "Borrar movimiento"