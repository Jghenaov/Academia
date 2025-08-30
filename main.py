from data.database import crear_tablas, conexion
from utils.logs import config_logs


if __name__ == '__main__':
    config_logs()
    crear_tablas()
    conexion()