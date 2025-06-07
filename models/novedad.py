from .database import db
from datetime import datetime
import uuid

class Novedad(db.Model):
    __tablename__ = 'novedades'
    
    id = db.Column(db.String(10), primary_key=True)
    nombre_enfermera = db.Column(db.String(100), nullable=False)
    nombre_paciente = db.Column(db.String(100), nullable=False)
    medicamento = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, nombre_enfermera, nombre_paciente, medicamento, cantidad):
        self.id = f"NOV-{str(uuid.uuid4().hex)[:5].upper()}"
        self.nombre_enfermera = nombre_enfermera
        self.nombre_paciente = nombre_paciente
        self.medicamento = medicamento
        self.cantidad = cantidad
        
    def __repr__(self):
        return f'<Novedad {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre_enfermera': self.nombre_enfermera,
            'nombre_paciente': self.nombre_paciente,
            'medicamento': self.medicamento,
            'cantidad': self.cantidad,
            'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d %H:%M')
        }
    
    def _generar_id_prefijado(self):
        """Genera un ID único con prefijo MED- (método de instancia)"""
        return f"MED-{str(uuid.uuid4().hex)[:6].upper()}"