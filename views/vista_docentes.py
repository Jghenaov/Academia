from prettytable import PrettyTable

def mostrar_docente(docente):
    """Muestra la información de un docente."""
    tabla = PrettyTable()
    tabla.field_names = [ "ID",  "Número de documento", "Nombre", "Apellido", "Email", "Especialidad"]
    tabla.add_row([docente.id_docente, docente.numero_documento, docente.nombre, docente.apellido, docente.email, docente.especialidad])
    print(tabla)

def mostrar_docentes(docentes):
    """Muestra la lista de docentes."""
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Número de documento", "Nombre", "Apellido", "Email", "Especialidad"]
    for docente in docentes:
        tabla.add_row([docente.id_docente, docente.numero_documento, docente.nombre, docente.apellido, docente.email, docente.especialidad])
    print(tabla)