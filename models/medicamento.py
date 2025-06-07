from .database import db
import uuid

class Medicamento(db.Model):
    __tablename__ = 'medicamentos'
    
    id = db.Column(db.String(10), primary_key=True)  # Cambiado a String
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    def __init__(self, nombre, tipo, stock):
        self.id = f"MED-{uuid.uuid4().hex[:5].upper()}"  # Genera ID como string
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock
    
    # Resto de métodos...
        
    def __repr__(self):
        return f'<Medicamento {self.nombre} (ID: {self.id})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'stock': self.stock
        }
    
    def _generar_id_prefijado(self):
        """Genera un ID único con prefijo MED- (método de instancia)"""
        return f"MED-{str(uuid.uuid4().hex)[:6].upper()}"  # Ejemplo: MED-A1B2C3