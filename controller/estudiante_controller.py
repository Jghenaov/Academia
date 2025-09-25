from models.estudiante_model import Estudiante
from data.database import Session
from utils.logs import get_logger

logger = get_logger(__name__)

#------------------------------------CRUD------------------------------------
# Funcion para registrar un estudiante
def registro_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    session = Session()
    try:
        estudiante = Estudiante(
            numero_documento=numero_documento, 
            nombre=nombre, 
            apellido=apellido, 
            fecha_nacimiento=fecha_nacimiento, 
            email=email, 
            telefono=telefono
        )
        session.add(estudiante)
        session.commit()
        logger.info(f'Estudiante {nombre} registrado exitosamente')
    except Exception as e:
        session.rollback()
        logger.error(f'Error al registrar el estudiante: {e}')
    finally:
        session.close()

# Funcion para obtener todos los estudiantes
def obtener_estudiantes():
    session = Session()
    try:
        estudiantes = session.query(Estudiante).all()
        logger.info('Estudiantes obtenidos exitosamente')
        return estudiantes
    except Exception as e:
        logger.error(f'Error al obtener los estudiantes: {e}')
        return []
    finally:
        session.close()
    
# Funcion para eliinar un estudiante
def eliminar_estudiante(id_estudiante):
    try:
        with Session() as session:
            estudiante = session.get(Estudiante, id_estudiante)
            if not estudiante:
                logger.warning(f"No se encontró un estudiante con ID {id_estudiante}")
                return False

            session.delete(estudiante)
            session.commit()
            logger.info(f"Estudiante con ID {id_estudiante} eliminado exitosamente")
            return True
    except Exception as e:
        logger.error(f"Error al eliminar el estudiante: {e}")
        return False
    
# Funcion para actualizar un estudiante
def actualizar_estudiante(id_estudiante, numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    try:
        with Session() as session:
            estudiante = session.get(Estudiante, id_estudiante)
            if not estudiante:
                logger.warning(f"No se encontró un estudiante con ID {id_estudiante}")
                return False

            estudiante.numero_documento = numero_documento
            estudiante.nombre = nombre
            estudiante.apellido = apellido
            estudiante.fecha_nacimiento = fecha_nacimiento
            estudiante.email = email
            estudiante.telefono = telefono

            session.commit()
            logger.info(f"Estudiante {nombre} con ID {id_estudiante} actualizado exitosamente")
            return True
    except Exception as e:
        logger.error(f"Error al actualizar el estudiante: {e}")
        return False
    
#----------------------------------------------------------------------------

# Funcion para obtener un estudiante por su ID
def obtener_estudiante_por_id(id_estudiante):
    try:
        with Session() as session:
            estudiante = session.get(Estudiante, id_estudiante)
            if not estudiante:
                logger.warning(f"No se encontró un estudiante con ID {id_estudiante}")
                return None
            return estudiante
    except Exception as e:
        logger.error(f"Error al obtener el estudiante: {e}")
        return None