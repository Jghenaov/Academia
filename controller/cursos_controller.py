from models.curso_model import Curso
from data.database import Session
from utils.logs import get_logger

logger = get_logger(__name__)

def registro_curso(nombre_curso, descripcion, creditos, id_docente):
    try:    
        curso = Curso(
            nombre_curso=nombre_curso, 
            descripcion=descripcion, 
            creditos=creditos, 
            id_docente=id_docente
        )
        Session.add(curso)
        Session.commit()
        logger.info('Curso registrado exitosamente')
    except Exception as e:
        Session.rollback()
        logger.error(f'Error al registrar el curso: {e}')
    finally:
        Session.close()
        

def obtener_cursos():
    session = Session()
    try:
        cursos = session.query(Curso).all()
        logger.info('Cursos obtenidos exitosamente')
        return cursos
    except Exception as e:
        logger.error(f'Error al obtener los cursos: {e}')
        return []
    finally:
        session.close()
        
def eliminar_curso(id_curso):
    try:
        curso = Session.query(Curso).get(id_curso)
        Session.delete(curso)
        Session.commit()
        logger.info('Curso eliminado exitosamente')
    except Exception as e:
        Session.rollback()
        logger.error(f'Error al eliminar el curso: {e}')
    finally:
        Session.close()
        
def actualizar_curso(id_curso, nombre_curso, descripcion, creditos, id_docente):
    try:
        curso = Session.query(Curso).get(id_curso)
        curso.nombre_curso = nombre_curso
        curso.descripcion = descripcion
        curso.creditos = creditos
        curso.id_docente = id_docente
        Session.commit()
        logger.info('Curso actualizado exitosamente')
    except Exception as e:
        Session.rollback()
        logger.error(f'Error al actualizar el curso: {e}')
    finally:
        Session.close()