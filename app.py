from flask import Flask, render_template, request, redirect, url_for, flash
from models.database import db
from controllers.paciente_controller import paciente_blueprint
from controllers.medicamento_controller import medicamento_blueprint
from controllers.novedad_controller import novedad_blueprint


app = Flask(__name__)
app.config.from_pyfile('config.py')


app.register_blueprint(medicamento_blueprint, url_prefix='/medicamentos')
app.register_blueprint(paciente_blueprint, url_prefix='/pacientes')
app.register_blueprint(novedad_blueprint, url_prefix='/novedad')


# Configurar base de datos
db.init_app(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(debug=True)