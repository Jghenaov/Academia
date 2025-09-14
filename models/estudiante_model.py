from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base

class Estudiante (Base):
    __tablename__ = 'Estudiantes'
    id_estudiante = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero_documento = Column(String(50), nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    fecha_nacimiento = Column(String(50), nullable=False)
    email = Column(String(25), nullable=False)
    telefono = Column(String(15), nullable=False)
    
    inscripciones = relationship("Inscripcion", back_populates="estudiantes")