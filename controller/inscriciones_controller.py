from sqlalchemy.orm import joinedload
from models.inscripciones_model import Inscripcion
from data.database import Session
from utils.logs import get_logger

logger = get_logger(__name__)

#------------------------------------CRUD------------------------------------
# Funcion para registrar una inscripcion
def registrar_inscripcion(id_estudiante, id_curso, fecha_inscripcion):
    try:
        with Session() as session:
            inscripcion = Inscripcion(
                id_estudiante=id_estudiante,
                id_curso=id_curso, 
                fecha_inscripcion=fecha_inscripcion
            )

            session.add(inscripcion)
            session.commit()
            logger.info(f"Inscripcion con ID {inscripcion.id_inscripcion} registrada exitosamente")
            
    except Exception as e:
        session.rollback()
        logger.error(f"Error al registrar la inscripcion: {e}")
    finally:
        session.close()

# Funcion para obtener todas las inscripciones
def obtener_inscripciones():
    session = Session()
    try:
        inscripciones = session.query(Inscripcion).options(
            joinedload(Inscripcion.estudiantes),   
            joinedload(Inscripcion.cursos)         
        ).all()
        logger.info('Inscripciones obtenidas exitosamente')
        return inscripciones
    except Exception as e:
        logger.error(f'Error al obtener las inscripciones: {e}')
        return []
    finally:
        session.close()

        
# Funcion para eliminar una inscripcion
def eliminar_inscripcion(id_inscripcion):
    try:
        with Session() as session:
            inscripcion = session.get(Inscripcion, id_inscripcion)
            if not inscripcion:
                logger.warning(f"No se encontró una inscripcion con ID {id_inscripcion}")
                return False

            session.delete(inscripcion)
            session.commit()
            logger.info(f"Inscripcion con ID {id_inscripcion} eliminada exitosamente")
            return True
    except Exception as e:
        logger.error(f"Error al eliminar la inscripcion: {e}")
        return False
    
# Funcion para actualizar una inscripcion
def actualizar_inscripcion(id_inscripcion, id_estudiante, id_curso, fecha_inscripcion):
    try:
        with Session() as session:
            inscripcion = session.get(Inscripcion, id_inscripcion)
            if not inscripcion:
                logger.warning(f"No se encontró una inscripcion con ID {id_inscripcion}")
                return False

            inscripcion.id_estudiante = id_estudiante
            inscripcion.id_curso = id_curso
            inscripcion.fecha_inscripcion = fecha_inscripcion

            session.commit()
            logger.info(f"Inscripcion con ID {id_inscripcion} y nombre {inscripcion.id_estudiante} actualizada exitosamente")
            return True
    except Exception as e:
        session.rollback()
        logger.error(f"Error al actualizar la inscripcion: {e}")
        return False

#----------------------------------------------------------------------------

# MOstrar las inscripciones de un estudiante
def obtener_inscripciones_estudiante(id_estudiante):
    session = Session()
    try:
        inscripciones = (
            session.query(Inscripcion)
            .options(
                joinedload(Inscripcion.estudiantes),  
                joinedload(Inscripcion.cursos)        
            )
            .filter(Inscripcion.id_estudiante == id_estudiante)
            .all()
        )
        logger.info('Inscripciones del estudiante obtenidas exitosamente')
        return inscripciones
    except Exception as e:
        logger.error(f'Error al obtener las inscripciones del estudiante: {e}')
        return []
    finally:
        session.close()
        
# Funcion para mostrar las inscripciones de un curso
def obtener_inscripciones_curso(id_curso):
    session = Session()
    try:
        inscripciones = (
            session.query(Inscripcion)
            .options(
                joinedload(Inscripcion.estudiantes), 
                joinedload(Inscripcion.cursos)        
            )
            .filter_by(id_curso=id_curso)
            .all()
        )
        logger.info('Inscripciones obtenidas exitosamente')
        return inscripciones
    except Exception as e:
        logger.error(f'Error al obtener las inscripciones: {e}')
        return []
    finally:
        session.close()
        
# Funcion para mostrar inscripcion por id
def obtener_inscripcion_por_id(id_inscripcion):
    session = Session()
    try:
        inscripcion = session.query(Inscripcion).filter_by(id_inscripcion=id_inscripcion).first()
        logger.info(f'Inscripcion con ID {id_inscripcion} obtenida exitosamente')
        return inscripcion
    except Exception as e:
        logger.error(f'Error al obtener la inscripcion: {e}')
        return None
    finally:
        session.close()