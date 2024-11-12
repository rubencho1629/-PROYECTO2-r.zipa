import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
USER_DB = os.getenv('USER_DB')
PASS_DB = os.getenv('PASS_DB')
URL_DB = os.getenv('URL_DB')
NAME_DB = os.getenv('NAME_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Importar controladores
#from .controllers import controllers
