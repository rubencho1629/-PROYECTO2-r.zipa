from app.config import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto

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
        """Intenta vender un producto y actualiza el inventario de ingredientes."""
        producto = Producto.query.filter_by(nombre=nombre_producto).first()
        if not producto:
            return False, "Producto no encontrado"

        # Verificar inventario de ingredientes
        for ingrediente in producto.ingredientes:
            if ingrediente.inventario <= 0:
                return False, f"No hay suficiente inventario de {ingrediente.nombre}"

        # Reducir inventario
        for ingrediente in producto.ingredientes:
            ingrediente.inventario -= 1
        db.session.commit()
        return True, f"Producto {nombre_producto} vendido exitosamente"
