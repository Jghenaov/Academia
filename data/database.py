from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from utils.logs import get_logger
from dotenv import load_dotenv
import os

load_dotenv()# Carga las variables de entorno

logger = get_logger(__name__)# Instancia del logger para manejo de logs

# Configuración de la base de datos
DIALECT = os.getenv("DB_DIALECT")
DRIVER = os.getenv("DB_DRIVER")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_NAME")

# Configuración de la cadena de conexión
SQLALCHEMY_DATABASE_URL = f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

Engine = create_engine(SQLALCHEMY_DATABASE_URL)# Crea una instancia de la base de datos
Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)# Crea una sesión de la base de datos
Base = declarative_base()# Se crea instancia para definicion de modelos

# Funcion para obtener la base de datos
def get_db():
    db = Session()
    try:    
        yield db
    finally:
        db.close()
        
# Funcion para conectar a la base de datos
def conexion():    
    try:
        Engine.connect()
        logger.info('Conexion exitosa a la base de datos')
    except Exception as e:
        logger.error(f'Error al conectar a la base de datos: {e}')

# Funcion para crear las tablas        
def crear_tablas():
    try:
        Base.metadata.create_all(bind=Engine)
        logger.info('Tablas creadas exitosamente')
    except Exception as e:
        logger.error(f'Error al crear las tablas: {e}')
              

