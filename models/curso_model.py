from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base

class Curso(Base):
    __tablename__ = 'Cursos'

    id_curso = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_curso = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=False)
    creditos = Column(Integer, nullable=False)
    id_docentes = Column(Integer, ForeignKey('Docentes.id_docente'))
    
    docente = relationship("Docente", back_populates="cursos")