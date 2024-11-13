from app.config import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_vendido import ProductoVendido

class Heladeria:

    @staticmethod
    def obtener_ingredientes():
        """Consulta todos los ingredientes."""
        return Ingrediente.query.all()

    @staticmethod
    def obtener_productos():
        """Consulta todos los productos."""
        return Producto.query.all()

    @staticmethod
    def producto_mas_rentable():
        """Consulta el producto más rentable."""
        productos = Producto.query.all()
        max_rentabilidad = None
        producto_rentable = None
        for producto in productos:
            costo = sum(ing.precio for ing in producto.ingredientes)
            rentabilidad = producto.precio_publico - costo
            if max_rentabilidad is None or rentabilidad > max_rentabilidad:
                max_rentabilidad = rentabilidad
                producto_rentable = producto
        return producto_rentable

    @staticmethod
    def vender_producto(nombre_producto):
        """Intenta vender un producto y registra la venta en productos_vendidos."""
        producto = Producto.query.filter_by(nombre=nombre_producto).first()
        if not producto:
            return "Producto no encontrado"

        # Verificar inventario de ingredientes y reabastecer si es necesario
        for ingrediente in producto.ingredientes:
            if ingrediente.inventario <= 0:
                ingrediente.reabastecer(10)
                db.session.commit()

            if ingrediente.inventario <= 0:
                raise ValueError(ingrediente.nombre)

        # Reducir inventario de ingredientes para completar la venta
        for ingrediente in producto.ingredientes:
            ingrediente.inventario -= 1
        db.session.commit()

        # Registrar la venta en productos_vendidos
        venta = ProductoVendido(
            producto_id=producto.id,
            precio_vendido=producto.precio_publico
        )
        db.session.add(venta)
        db.session.commit()

        return "¡Vendido!"
