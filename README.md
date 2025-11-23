# Academia

Proyecto de consola para gestionar estudiantes, docentes, cursos e inscripciones utilizando SQLAlchemy y PostgreSQL.

## Descripción
Aplicación modular en Python que permite:
- Crear/leer/actualizar/eliminar docentes y cursos.
- Registrar inscripciones de estudiantes en cursos.
- Interacción mediante menú en consola con vistas formateadas (PrettyTable).
- Logging de operaciones y errores en `app.log`.

## Requisitos
- Python 3.10+ (Linux)
- PostgreSQL (o DB soportada por SQLAlchemy)
- Virtualenv (recomendado)
- Dependencias en `requirements.txt` (SQLAlchemy, psycopg2-binary, python-dotenv, prettytable, ...)


## Variables de entorno (.env) — ejemplo
```
DB_DIALECT=postgresql
DB_DRIVER=psycopg2
DB_USERNAME=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=academia_db
```

## Instalación rápida (Linux)
1. Crear y activar venv:
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```
3. Configurar `.env` con los datos de tu BD.

## Inicializar la base de datos y ejecutar
La aplicación inicializa tablas desde `main.py` (usa `crear_tablas()`).

