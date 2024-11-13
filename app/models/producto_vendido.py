from datetime import datetime
from app import db

class ProductoVendido(db.Model):
    __tablename__ = 'productos_vendidos'

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    fecha_venta = db.Column(db.DateTime, default=datetime.utcnow)
    precio_vendido = db.Column(db.Float, nullable=False)

    # Relación para acceder al producto vendido desde esta tabla
    producto = db.relationship('Producto', backref='ventas')
