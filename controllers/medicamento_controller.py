from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.medicamento import Medicamento
from models.database import db

medicamento_blueprint = Blueprint('medicamento', __name__)

@medicamento_blueprint.route('/registrarMedicamento', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        stock = request.form['stock']
        
        if not nombre or not tipo or not stock:
            flash('Por favor complete todos los campos', 'error')
            return redirect(url_for('medicamento.registrar'))
        
        try:
            nuevo_medicamento = Medicamento(nombre=nombre, tipo=tipo, stock=stock)
            db.session.add(nuevo_medicamento)
            db.session.commit()
            flash('Medicamento registrado con éxito', 'success')
            return redirect(url_for('medicamento.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar medicamento: {str(e)}', 'error')
    
    return render_template('registroMedicamento.html')

@medicamento_blueprint.route('/medicamentos')
def listar():
    medicamentos = Medicamento.query.all()
    return render_template('medicamentos.html', medicamentos=medicamentos)

@medicamento_blueprint.route('/editar/<string:id>', methods=['GET', 'POST'])
def editar(id):
    medicamento = Medicamento.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            medicamento.nombre = request.form['nombre']
            medicamento.tipo = request.form['tipo']
            medicamento.stock = int(request.form['stock'])
            
            db.session.commit()
            flash('Medicamento actualizado con éxito', 'success')
            return redirect(url_for('medicamento.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar medicamento: {str(e)}', 'error')
    
    # GET: Mostrar formulario con datos actuales
    return render_template('registroMedicamento.html', medicamento=medicamento)

@medicamento_blueprint.route('/eliminar/<string:id>')
def eliminar(id):
    medicamento = Medicamento.query.get_or_404(id)
    try:
        db.session.delete(medicamento)
        db.session.commit()
        flash('Medicamento eliminado con éxito', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar medicamento: {str(e)}', 'error')
    
    return redirect(url_for('medicamento.listar'))