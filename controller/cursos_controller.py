from models.curso_model import Curso
from data.database import session
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
        session.add(curso)
        session.commit()
        logger.info('Curso registrado exitosamente')
    except Exception as e:
        session.rollback()
        logger.error(f'Error al registrar el curso: {e}')
    finally:
        session.close()
        

def obtener_cursos():
    try:
        cursos = session.query(Curso).all()
        logger.info('Cursos obtenidos exitosamente')
        return cursos
    except Exception as e:
        logger.error(f'Error al obtener los cursos: {e}')
    finally:
        session.close()
        
def eliminar_curso(id_curso):
    try:
        curso = session.query(Curso).get(id_curso)
        session.delete(curso)
        session.commit()
        logger.info('Curso eliminado exitosamente')
    except Exception as e:
        session.rollback()
        logger.error(f'Error al eliminar el curso: {e}')
    finally:
        session.close()
        
def actualizar_curso(id_curso, nombre_curso, descripcion, creditos, id_docente):
    try:
        curso = session.query(Curso).get(id_curso)
        curso.nombre_curso = nombre_curso
        curso.descripcion = descripcion
        curso.creditos = creditos
        curso.id_docente = id_docente
        session.commit()
        logger.info('Curso actualizado exitosamente')
    except Exception as e:
        session.rollback()
        logger.error(f'Error al actualizar el curso: {e}')
    finally:
        session.close()