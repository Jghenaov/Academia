from prettytable import PrettyTable

def mostar_inscripciones(inscripciones):
    """Mostrar los datos de una inscripciónes."""
    tabla = PrettyTable()
    tabla.title = "Inscripciones"
    tabla.field_names = ["ID Inscripción", "Número Documento", "Nombre Estudiante", "ID Curso", "Nombre Curso", "Fecha Inscripción"]

    for ins in inscripciones:
        tabla.add_row([ins.id_inscripcion, ins.estudiantes.numero_documento, f"{ins.estudiantes.nombre} {ins.estudiantes.apellido}", ins.cursos.id_curso, ins.cursos.nombre_curso, ins.fecha_inscripcion])

    print(tabla)
    

# Mostrar inscripciones de un estudiante
def mostrar_inscripciones_estudiante(inscripciones):
    if not inscripciones:
        print("No hay inscripciones para este estudiante.")
        return
    
    estudiante = inscripciones[0].estudiantes
    
    tabla = PrettyTable()
    tabla.title = f"Inscripciones del estudiante {estudiante.nombre} {estudiante.apellido}"
    tabla.field_names = ["ID Inscripción", "ID Curso", "Nombre Curso", "Fecha Inscripción"]

    for ins in inscripciones:
        tabla.add_row([ins.id_inscripcion, ins.cursos.id_curso, ins.cursos.nombre_curso, ins.fecha_inscripcion])

    print(tabla)
    
    
# Mostrar inscripciones de un curso
def mostrar_inscripciones_curso(inscripciones):
    if not inscripciones:
        print("No hay inscripciones para este curso.")
        return
    
    curso = inscripciones[0].cursos
    
    tabla = PrettyTable()
    tabla.title = f"Inscripciones del curso {curso.nombre_curso}"
    tabla.field_names = ["ID Inscripción", "Número Documento", "Nombre Estudiante", "Fecha Inscripción"]

    for ins in inscripciones:
        tabla.add_row([ins.id_inscripcion, ins.estudiantes.numero_documento, f"{ins.estudiantes.nombre} {ins.estudiantes.apellido}", ins.fecha_inscripcion])

    print(tabla)