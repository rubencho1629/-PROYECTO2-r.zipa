from .. import db
from .ingrediente import Ingrediente

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)

    # Relación con ingredientes (usando tres llaves foráneas)
    ingrediente1_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    ingrediente2_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))
    ingrediente3_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'))

    # Relaciones para obtener los ingredientes directamente
    ingrediente1 = db.relationship("Ingrediente", foreign_keys=[ingrediente1_id])
    ingrediente2 = db.relationship("Ingrediente", foreign_keys=[ingrediente2_id])
    ingrediente3 = db.relationship("Ingrediente", foreign_keys=[ingrediente3_id])

    def calcular_costo(self):
        # Calcula el costo sumando los precios de cada ingrediente
        return sum([ing.precio for ing in [self.ingrediente1, self.ingrediente2, self.ingrediente3] if ing])

    def calcular_rentabilidad(self):
        # Calcula la rentabilidad restando el costo del precio de venta
        return self.precio_publico - self.calcular_costo()
