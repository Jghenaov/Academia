from models.docente_model import Docente
from data.database import Session
from utils. logs import get_logger

logger = get_logger(__name__)

#------------------------------------CRUD------------------------------------
# Funcion para registrar un docente
def registro_docente(numero_documento, nombre, apellido, email, especialidad):
    session = Session()
    try:
        docente = Docente(
            numero_documento=numero_documento, 
            nombre=nombre, 
            apellido=apellido, 
            email=email, 
            especialidad=especialidad
        )
        session.add(docente)
        session.commit()
        logger.info(f'Docente {nombre} registrado exitosamente')
    except Exception as e:
        session.rollback()
        logger.error(f'Error al registrar el docente: {e}')
    finally:
        session.close()

# Funcion para obtener todos los docentes        
def obtener_docentes():
    session = Session()
    try:
        docentes = session.query(Docente).all()
        logger.info('Docentes obtenidos exitosamente')
        return docentes
    except Exception as e:
        logger.error(f'Error al obtener los docentes: {e}')
        return []
    finally:
        session.close()
        
# Funcion para eliminar un docente
def eliminar_docente(id_docente):
    try:
        with Session() as session:
            docente = session.get(Docente, id_docente)
            if not docente:
                logger.warning(f"No se encontró un docente con ID {id_docente}")
                return False

            session.delete(docente)
            session.commit()
            logger.info(f"Docente con ID {id_docente} eliminado exitosamente")
            return True
    except Exception as e:
        logger.error(f"Error al eliminar el docente: {e}")
        return False
    
# Funcion para actualizar un docente
def actualizar_docente(id_docente, numero_documento, nombre, apellido, email, especialidad):
    try:
        with Session() as session:
            docente = session.get(Docente, id_docente)
            if not docente:
                logger.warning(f"No se encontró un docente con ID {id_docente}")
                return False

            docente.numero_documento = numero_documento
            docente.nombre = nombre
            docente.apellido = apellido
            docente.email = email
            docente.especialidad = especialidad

            session.commit()
            logger.info(f"Docente {nombre} con ID {id_docente} actualizado exitosamente")
            return True
    except Exception as e:
        logger.error(f"Error al actualizar el docente: {e}")
        return False
#----------------------------------------------------------------------------

# Funcion para obtener un docente por su ID
def obtener_docente_por_id(id_docente):
    session = Session()
    try:
        docente = session.query(Docente).filter_by(id_docente=id_docente).first()
        logger.info('Docente obtenido exitosamente')
        return docente
    except Exception as e:
        logger.error(f'Error al obtener el docente: {e}')
        return None
    finally:
        session.close()
        

# Funcion para asiganar un curso a un docente
def asignar_curso_docente(id_docente, id_curso):
    try:
        with Session() as session:
            docente = session.get(Docente, id_docente)
            if not docente:
                logger.warning(f"No se encontró un docente con ID {id_docente}")
                return False

            docente.id_curso = id_curso

            session.commit()
            logger.info(f"Docente con ID {id_docente} actualizado exitosamente")
            return True
    except Exception as e:
        logger.error(f"Error al actualizar el docente: {e}")
        return False


def existe_numero_documento(numero_documento):
    session = Session()
    try:
        return session.query(Docente).filter_by(numero_documento=numero_documento).first() is not None
    
    finally:
        session.close()
