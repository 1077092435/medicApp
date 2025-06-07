from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.novedad import Novedad
from models.database import db
from datetime import datetime

novedad_blueprint = Blueprint('novedad', __name__)

@novedad_blueprint.route('/registrarNovedad', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        try:
            nueva_novedad = Novedad(
                nombre_enfermera=request.form['nombre_enfermera'],
                nombre_paciente=request.form['nombre_paciente'],
                medicamento=request.form['medicamento'],
                cantidad=int(request.form['cantidad'])
            )
            db.session.add(nueva_novedad)
            db.session.commit()
            flash('Novedad registrada con éxito', 'success')
            return redirect(url_for('novedad.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar novedad: {str(e)}', 'error')
    
    return render_template('registroNovedad.html')

@novedad_blueprint.route('/novedades')
def listar():
    novedades = Novedad.query.order_by(Novedad.fecha_registro.desc()).all()
    return render_template('novedades.html', novedades=novedades)

@novedad_blueprint.route('/editar/<string:id>', methods=['GET', 'POST'])
def editar(id):
    novedad = Novedad.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            novedad.nombre_enfermera = request.form['nombre_enfermera']
            novedad.nombre_paciente = request.form['nombre_paciente']
            novedad.medicamento = request.form['medicamento']
            novedad.cantidad = int(request.form['cantidad'])
            
            db.session.commit()
            flash('novedad actualizada con éxito', 'success')
            return redirect(url_for('novedad.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar novedad: {str(e)}', 'error')
    
    # GET: Mostrar formulario con datos actuales
    return render_template('registroNovedad.html', novedad=novedad)

@novedad_blueprint.route('/eliminar/<string:id>')
def eliminar(id):
    novedad = Novedad.query.get_or_404(id)
    try:
        db.session.delete(novedad)
        db.session.commit()
        flash('Novedad eliminada con éxito', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar novedad: {str(e)}', 'error')
    
    return redirect(url_for('novedad.listar'))