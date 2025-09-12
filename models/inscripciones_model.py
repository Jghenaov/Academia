from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from data.database import Base
from datetime import datetime

class Inscripcion(Base):
    __tablename__ = 'Inscripciones'
    id_inscripcion = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey('Estudiantes.id_estudiante'))
    id_curso = Column(Integer, ForeignKey('Cursos.id_curso'))
    fecha_inscripcion = Column(DateTime, default=datetime.now(), nullable=False)

    estudiante = relationship("Estudiante", back_populates="inscripciones")
    curso = relationship("Curso", back_populates="inscripciones")