from prettytable import PrettyTable

#Muestra la información de un curso.
def mostrar_cursos(cursos):
    tabla = PrettyTable()
    tabla.title = "Cursos"
    tabla.field_names = ["ID", "Nombre", "Descripción", "Creditos", "Docente"]
    for curso in cursos:
        nombre_docente = f"{curso.docente.nombre} {curso.docente.apellido}" if curso.docente else "No asignado"
        tabla.add_row([curso.id_curso, curso.nombre_curso, curso.descripcion, curso.creditos, nombre_docente])
    print(tabla)
    
#Muestra la información de un curso por el id del docente    
def mostrar_curso_por_docente(cursos):
    tabla = PrettyTable()
    tabla.field_names = ["Nombre", "Descripción", "Creditos"]

    if cursos and cursos[0].docente:
        nombre_docente = f"{cursos[0].docente.nombre} {cursos[0].docente.apellido}"
        tabla.title = f"Cursos dictados por el docente {nombre_docente}"
    else:
        tabla.title = "Cursos dictados por el docente"

    for curso in cursos:
        tabla.add_row([curso.nombre_curso, curso.descripcion, curso.creditos])
    print(tabla)