from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base

class Docente(Base):
    __tablename__= 'Docentes'
    id_docente = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero_documento = Column(String(50), nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    especialidad = Column(String(80), nullable=False)
    
    curso = relationship("Curso", back_populates="docente")