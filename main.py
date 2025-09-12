from data.database import crear_tablas, conexion
from utils.logs import config_logs
from models import estudiante_model, docente_model, curso_model, inscripciones_model
from menu.menu_general import menuGeneral


if __name__ == '__main__':
    config_logs()
    crear_tablas()
    conexion()
    menuGeneral()