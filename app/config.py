import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Cargar variables de entorno desde .env
load_dotenv()

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('USER_DB')}:{os.getenv('PASS_DB')}@{os.getenv('URL_DB')}/{os.getenv('NAME_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
