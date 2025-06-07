import os

# Configuración básica
SECRET_KEY = 'tu_clave_secreta_aqui'

# Configuración de base de datos (SQLite para desarrollo)
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'medicamentos.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False