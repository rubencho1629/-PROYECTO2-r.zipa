from app.config import db
from app.models.producto_ingrediente import producto_ingrediente  # Importa la tabla intermedia

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)

    # Define la relación many-to-many usando la tabla intermedia
    ingredientes = db.relationship('Ingrediente', secondary=producto_ingrediente, backref='productos')
