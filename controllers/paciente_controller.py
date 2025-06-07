from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.paciente import Paciente
from models.database import db

paciente_blueprint = Blueprint('paciente', __name__)

@paciente_blueprint.route('/registrarPaciente', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = int(request.form['cedula'])
        direccion = request.form['direccion']
        
        if not nombre or not cedula or not direccion:
            flash('Por favor complete todos los campos', 'error')
            return redirect(url_for('paciente.registrar'))
        
        try:
            if Paciente.query.filter_by(cedula=cedula).first():
                flash('Esta cédula ya está registrada', 'error')
                return redirect(url_for('paciente.registrar'))
            nuevo_paciente = Paciente(nombre=nombre, cedula=cedula, direccion=direccion)
            db.session.add(nuevo_paciente)
            db.session.commit()
            flash('Paciente registrado con éxito', 'success')
            return redirect(url_for('paciente.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar paciente: {str(e)}', 'error')
    
    return render_template('registroPaciente.html')

@paciente_blueprint.route('/pacientes')
def listar():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=pacientes)

@paciente_blueprint.route('/editar/<string:id>', methods=['GET', 'POST'])
def editar(id):
    paciente = Paciente.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            paciente.nombre = request.form['nombre']
            paciente.cedula = int(request.form['cedula'])
            paciente.direccion = request.form['direccion']
            
            db.session.commit()
            flash('paciente actualizado con éxito', 'success')
            return redirect(url_for('paciente.listar'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar paciente: {str(e)}', 'error')
    
    # GET: Mostrar formulario con datos actuales
    return render_template('registroPaciente.html', paciente=paciente)

@paciente_blueprint.route('/eliminar/<string:id>')
def eliminar(id):
    paciente = Paciente.query.get_or_404(id)
    try:
        db.session.delete(paciente)
        db.session.commit()
        flash('Paciente eliminado con éxito', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar paciente: {str(e)}', 'error')
    
    return redirect(url_for('paciente.listar'))