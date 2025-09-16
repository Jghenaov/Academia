from models.curso_model import Curso
from data.database import Session
from utils.logs import get_logger
from models.docente_model import Docente
from sqlalchemy.orm import joinedload

logger = get_logger(__name__)


#------------------------------------CRUD------------------------------------
# Funcion para registrar un curso
def registro_curso(nombre_curso, descripcion, creditos, id_docente):
    session = Session()
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
        
# Funcion para obtener todos los cursos
def obtener_cursos():
    session = Session()
    try:
        cursos = session.query(Curso).options(joinedload(Curso.docente)).all()
        logger.info('Cursos obtenidos exitosamente')
        return cursos
    except Exception as e:
        logger.error(f'Error al obtener los cursos: {e}')
        return []
    finally:
        session.close()

# Funcion para eliminar un curso        
def eliminar_curso(id_curso):
    try:
        with Session() as session:
            curso = session.get(Curso, id_curso)
            if not curso:
                logger.warning(f"No se encontró un curso con ID {id_curso}")
                return False
            session.delete(curso)
            session.commit()
            logger.info(f'Curso con ID {id_curso} eliminado exitosamente')
            return True
    except Exception as e:
        session.rollback()
        logger.error(f'Error al eliminar el curso: {e}')
        return False

# Funcion para actualizar un curso        
def actualizar_curso(id_curso, nombre_curso, descripcion, creditos, id_docente):
    try:
        with Session() as session:
            curso = session.get(Curso, id_curso)
            if not curso:
                logger.warning(f"No se encontró un curso con ID {id_curso}")
                return False

            curso.nombre_curso = nombre_curso
            curso.descripcion = descripcion
            curso.creditos = creditos
            curso.id_docente = id_docente

            session.commit()
            logger.info(f"Curso con ID {id_curso} actualizado exitosamente")
            return True
    except Exception as e:
        logger.error(f"Error al actualizar el curso: {e}")
        return False

#----------------------------------------------------------------------------

        
#Mostrar cursos dictados por un docente
def mostrar_cursos_docente(id_docente):
    session = Session()
    try:
        cursos = session.query(Curso).options(joinedload(Curso.docente)).filter(Curso.id_docente == id_docente).all()
        return cursos
    finally:
        session.close()

#Verificar si un docente existe por su id        
def existe_docente(id_docente):
    session = Session()
    try:
        docente = session.query(Docente).filter_by(id_docente=id_docente).first()
        return docente is not None
    finally:
        session.close()
        
#Verificar si un curso existe por su id        
def existe_curso(id_curso):
    session = Session()
    try:
        curso = session.query(Curso).filter_by(id_curso=id_curso).first()
        logger.info(f'Curso con  ID {id_curso} obtenido exitosamente')
        return curso is not None
    except Exception as e:
        logger.error(f'Error al obtener el curso: {e}')
        return False
    finally:
        session.close()