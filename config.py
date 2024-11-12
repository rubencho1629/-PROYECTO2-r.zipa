from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
USER_DB = 'ruben'
PASS_DB = '12345'
URL_DB = 'localhost'
NAME_DB = 'tablas'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
