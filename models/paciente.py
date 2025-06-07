from .database import db
import uuid

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cedula = db.Column(db.BigInteger, nullable=False, unique=True)
    direccion = db.Column(db.String(100), nullable=False)
    
    def __init__(self, nombre, cedula, direccion):
        self.id = f"PAC-{uuid.uuid4().hex[:5].upper()}"
        self.nombre = nombre
        self.cedula = int(cedula)
        self.direccion = direccion
        
    def __repr__(self):
        return f'<Paciente {self.nombre} (ID: {self.id})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cedula': self.cedula,
            'direccion': self.direccion
        }
    
    def _generar_id_prefijado(self):
        """Genera un ID único con prefijo MED- (método de instancia)"""
        return f"MED-{str(uuid.uuid4().hex)[:6].upper()}"