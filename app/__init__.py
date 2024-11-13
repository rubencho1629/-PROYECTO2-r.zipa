from flask import Flask
from app.config import Config, db
from app.controllers.heladeria_controller import heladeria_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar la base de datos con la aplicación
    db.init_app(app)

    # Registrar el blueprint de heladería
    app.register_blueprint(heladeria_bp, url_prefix='/heladeria')

    return app
