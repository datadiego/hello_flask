"""
Un movimiento debe tener:

1. Fecha
2. Concepto
3. Tipo (I-ngreso, G-asto)
4. Cantidad
"""
import csv
from datetime import date, datetime

from . import FICHERO


class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            self.errores.append("El formato de la fecha no es válido")

        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_archivo(self):
        with open(FICHERO, "r") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                mov = Movimiento(
                    linea["fecha"], linea["concepto"],
                    linea["tipo"], linea["cantidad"])
                self.movimientos.append(mov)
