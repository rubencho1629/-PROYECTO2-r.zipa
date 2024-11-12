from .. import db
from app.models.producto import Producto
from app.models.ingrediente import Ingrediente

class Heladeria:
    def __init__(self):
        self.productos = []       # Lista de productos disponibles
        self.ingredientes = []    # Lista de ingredientes disponibles

    def cargar_datos(self):
        """Carga los ingredientes y productos desde la base de datos."""
        # Cargar todos los ingredientes desde la base de datos
        self.ingredientes = Ingrediente.query.all()

        # Cargar todos los productos desde la base de datos, incluyendo sus ingredientes
        self.productos = Producto.query.all()

    def agregar_producto(self, producto):
        """Agrega un producto a la lista y a la base de datos."""
        self.productos.append(producto)
        db.session.add(producto)
        db.session.commit()

    def agregar_ingrediente(self, ingrediente):
        """Agrega un ingrediente a la lista y a la base de datos."""
        self.ingredientes.append(ingrediente)
        db.session.add(ingrediente)
        db.session.commit()

    def vender_producto(self, nombre_producto):
        """Reduce el inventario de ingredientes cuando se vende un producto."""
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                # Verificar si hay suficiente inventario de ingredientes
                if all(ingrediente.inventario > 0 for ingrediente in [producto.ingrediente1, producto.ingrediente2, producto.ingrediente3] if ingrediente):
                    for ingrediente in [producto.ingrediente1, producto.ingrediente2, producto.ingrediente3]:
                        if ingrediente:
                            ingrediente.inventario -= 1
                    db.session.commit()
                    print(f"Producto {nombre_producto} vendido por {producto.precio_publico}.")
                    return True
                else:
                    print(f"No hay suficiente inventario para {nombre_producto}.")
                    return False
        print(f"Producto {nombre_producto} no encontrado.")
        return False

    def mejor_producto(self):
        """Devuelve el producto con la mayor rentabilidad."""
        if self.productos:
            return max(self.productos, key=lambda p: p.calcular_rentabilidad()).nombre
        return "No hay productos disponibles."
