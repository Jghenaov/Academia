from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from utils.logs import get_logger
from dotenv import load_dotenv
import os

load_dotenv()

logger = get_logger(__name__)

DIALECT = os.getenv("DB_DIALECT")
DRIVER = os.getenv("DB_DRIVER")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

Engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()

def get_db():
    db = Session()
    try:    
        yield db
    finally:
        db.close()
        

def conexion():    
    try:
        Engine.connect()
        logger.info('Conexion exitosa a la base de datos')
    except Exception as e:
        logger.error(f'Error al conectar a la base de datos: {e}')
        
def crear_tablas():
    try:
        Base.metadata.create_all(bind=Engine)
        logger.info('Tablas creadas exitosamente')
    except Exception as e:
        logger.error(f'Error al crear las tablas: {e}')
              

