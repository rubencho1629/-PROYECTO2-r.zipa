from .. import db

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)

    def __init__(self, nombre, precio, calorias, inventario, es_vegetariano):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self.inventario = inventario
        self.es_vegetariano = es_vegetariano

    def abastecer(self, cantidad=5):
        self.inventario += cantidad

    def es_sano(self):
        return self.calorias < 200
