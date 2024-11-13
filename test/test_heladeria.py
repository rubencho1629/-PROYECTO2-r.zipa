import unittest
from app import create_app, db
from app.config import TestConfig
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.services.heladeria import Heladeria

class TestHeladeria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializa la aplicación en modo de prueba con TestConfig
        cls.app = create_app(TestConfig)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Limpia la base de datos después de todas las pruebas
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        # Configura datos iniciales para cada prueba
        self.ingrediente1 = Ingrediente(nombre="Fresa", precio=200, calorias=50, inventario=10, es_vegetariano=True)
        self.ingrediente2 = Ingrediente(nombre="Chocolate", precio=300, calorias=150, inventario=5, es_vegetariano=True)
        db.session.add(self.ingrediente1)
        db.session.add(self.ingrediente2)
        db.session.commit()

    def tearDown(self):
        # Elimina los datos de la base de datos después de cada prueba
        db.session.remove()
        db.drop_all()
        db.create_all()

    # Aquí puedes incluir las pruebas, como test_es_sano, test_abastecer_ingrediente, etc.

if __name__ == '__main__':
    unittest.main()
