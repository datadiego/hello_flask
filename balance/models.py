"""
Un movimiento debe tener:
1. Fecha
2. Concepto
3. Tipo (Ingreso o Gasto)
4. Cantidad
"""
import csv
from datetime import date
from encodings import utf_8
from balance import FICHERO

class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            self.errores.append("La fecha no es válida")

        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad




class ListaMovimientos:
    def __init__(self):
        self.movimientos = []
    
    def leer_archivo(self):
        with open(FICHERO, "r", encoding="utf_8") as file:
            reader = csv.DictReader(file)
            for linea in reader:
                mov = Movimiento(linea["fecha"], linea["concepto"], linea["tipo"], linea["cantidad"])
                self.movimientos.append(mov)
