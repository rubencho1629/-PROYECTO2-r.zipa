import unittest
from app.services.heladeria import Heladeria
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto

class TestHeladeria(unittest.TestCase):

    def setUp(self):
        # Configurar el entorno de prueba: Crear la instancia de la heladería
        self.heladeria = Heladeria()

        # Crear ingredientes de prueba
        self.fresa = Ingrediente(nombre="Fresa", precio=2000, calorias=50, inventario=10, es_vegetariano=True)
        self.chocolate = Ingrediente(nombre="Chocolate", precio=1000, calorias=150, inventario=15, es_vegetariano=True)
        self.leche = Ingrediente(nombre="Leche", precio=500, calorias=100, inventario=20, es_vegetariano=False)

        # Agregar ingredientes a la heladería
        self.heladeria.agregar_ingrediente(self.fresa)
        self.heladeria.agregar_ingrediente(self.chocolate)
        self.heladeria.agregar_ingrediente(self.leche)

        # Crear productos de prueba
        self.copa_fresa = Producto(nombre="Copa de Fresa", precio_publico=7500)
        self.copa_fresa.ingrediente1 = self.fresa
        self.copa_fresa.ingrediente2 = self.chocolate
        self.copa_fresa.ingrediente3 = self.leche

        self.heladeria.agregar_producto(self.copa_fresa)

    def test_es_sano(self):
        """Probar si un ingrediente es sano."""
        self.assertTrue(self.fresa.es_sano())  # 50 calorías es bajo, es sano
        self.assertFalse(self.chocolate.es_sano())  # 150 calorías es alto, no es sano

    def test_abastecer_ingrediente(self):
        """Abastecer un ingrediente."""
        inventario_anterior = self.fresa.inventario
        self.fresa.abastecer(5)
        self.assertEqual(self.fresa.inventario, inventario_anterior + 5)

    def test_renovar_inventario_complementos(self):
        """Renovar inventario para los complementos."""
        self.leche.inventario = 0
        self.leche.abastecer()
        self.assertEqual(self.leche.inventario, 5)  # Debería ser reabastecido en 5 unidades

    def test_calcular_calorias(self):
        """Calcular las calorías tanto en copas como en malteadas."""
        calorias_totales = self.copa_fresa.calcular_calorias()
        self.assertEqual(calorias_totales, self.fresa.calorias + self.chocolate.calorias + self.leche.calorias)

    def test_calcular_costo_produccion(self):
        """Calcular el costo de producción."""
        costo = self.copa_fresa.calcular_costo()
        self.assertEqual(costo, self.fresa.precio + self.chocolate.precio + self.leche.precio)

    def test_calcular_rentabilidad_producto(self):
        """Calcular la rentabilidad de un producto."""
        rentabilidad = self.copa_fresa.calcular_rentabilidad()
        costo = self.fresa.precio + self.chocolate.precio + self.leche.precio
        self.assertEqual(rentabilidad, self.copa_fresa.precio_publico - costo)

    def test_encontrar_producto_mas_rentable(self):
        """Encontrar el producto más rentable."""
        producto_rentable = self.heladeria.mejor_producto()
        self.assertEqual(producto_rentable, self.copa_fresa.nombre)

    def test_vender_producto(self):
        """Vender un producto."""
        inventario_inicial = self.fresa.inventario
        venta_exitosa = self.heladeria.vender_producto(self.copa_fresa.nombre)
        self.assertTrue(venta_exitosa)
        self.assertEqual(self.fresa.inventario, inventario_inicial - 1)

    def test_vender_producto_sin_inventario(self):
        """Vender un producto sin inventario, debe fallar."""
        # Reducimos el inventario a 0 para simular que no hay inventario
        self.fresa.inventario = 0
        venta_exitosa = self.heladeria.vender_producto(self.copa_fresa.nombre)
        self.assertFalse(venta_exitosa)

if __name__ == "__main__":
    unittest.main()
