from flask import Flask
from app.config import Config, db
from app.controllers.heladeria_controller import heladeria_bp

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)

    # Registrar el blueprint de heladeria con el prefijo /heladeria
    app.register_blueprint(heladeria_bp, url_prefix='/heladeria')

    return app
