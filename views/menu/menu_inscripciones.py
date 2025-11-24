from controller.inscriciones_controller import (registrar_inscripcion, 
                                                obtener_inscripciones, 
                                                obtener_inscripciones_estudiante,
                                                obtener_inscripciones_curso, 
                                                obtener_inscripcion_por_id, 
                                                actualizar_inscripcion, 
                                                eliminar_inscripcion
                                                )
from controller.estudiantes_controller import obtener_estudiante_por_id, obtener_estudiantes
from controller.cursos_controller import existe_curso, obtener_cursos
from views.vista_estudiante import mostrar_estudiantes
from views.vista_cursos import mostrar_cursos
from views.vista_inscripciones import  mostar_inscripciones, mostrar_inscripciones_curso, mostrar_inscripciones_estudiante
from utils.others import limpiar_consola
from datetime import datetime

def menuInscripciones():
    while True:
        limpiar_consola()
        print("------------Menu de Inscripciones------------")
        print("\n1. Realizar Inscripción")
        print("2. Mostrar Inscripciones")
        print("3. Mostrar Inscripciones por Estudiante")
        print("4. Mostrar Inscripciones por Curso")
        print("5. Actualizar Inscripción")
        print("6. Eliminar Inscripción")
        print("7. Salir")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            try:
                limpiar_consola()
                estudiantes = obtener_estudiantes()
                mostrar_estudiantes(estudiantes)
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                estudiante = obtener_estudiante_por_id(id_estudiante)
                if not estudiante:
                    print("Estudiante no encontrado.")
                    input("Presione enter para continuar...")
                    continue
                cursos = obtener_cursos()
                mostrar_cursos(cursos)
                id_curso = int(input("Ingrese el ID del curso: "))
                curso = existe_curso(id_curso)
                if not curso:
                    print("Curso no encontrado.")
                    input("Presione enter para continuar...")
                    continue
                fecha_inscripcion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                registrar_inscripcion(id_estudiante, id_curso, fecha_inscripcion)
                input("Incripcion realizada con exito. Presione enter para continuar...")
            except ValueError as  e:
                print(f"Error: {e}")
                input("Presione enter para continuar...")

        elif opcion == "2":
            try:
                limpiar_consola()
                inscripciones = obtener_inscripciones()
                if not inscripciones:
                    print("No hay inscripciones registradas.")
                    input("Presione enter para continuar...")
                    continue
                mostar_inscripciones(inscripciones)
                input("Presione enter para continuar...")
            except Exception as e:
                print(f"Error: {e}")
                input("Presione enter para continuar...")

        elif opcion == "3":
            try:
                limpiar_consola()
                estudiantes = obtener_estudiantes()
                mostrar_estudiantes(estudiantes)
                id_estudiante = int(input("Ingrese el ID del estudiante: ")) 
                esttudiante =obtener_inscripciones_estudiante(id_estudiante)
                if not esttudiante:
                    print(f"No hay inscripciones registradas para el estudiante con ID {id_estudiante}.")
                    input("Presione enter para continuar...")
                    continue
                mostrar_inscripciones_estudiante(esttudiante)
                input("Presione enter para continuar...")
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione enter para continuar...")

        elif opcion == "4":
            try:
                limpiar_consola()
                cursos = obtener_cursos()
                mostrar_cursos(cursos)
                id_curso = int(input("Ingrese el ID del curso: "))
                cursos = obtener_inscripciones_curso(id_curso)
                if not cursos:
                    print(f"No hay inscripciones registradas para el curso con ID {id_curso}.")
                    input("Presione enter para continuar...")
                    continue
                mostrar_inscripciones_curso(cursos)
                input("Presione enter para continuar...")
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione enter para continuar...")

        elif opcion == "5":
            try:
                limpiar_consola()
                inscripciones = obtener_inscripciones()
                mostar_inscripciones(inscripciones)
                id_inscripcion = int(input("Ingrese el ID de la inscripcion: "))
                inscripcion = obtener_inscripcion_por_id(id_inscripcion)
                if not inscripcion:
                    print(f"No se encontro la inscripcion con ID {id_inscripcion}.")
                    input("Presione enter para continuar...")
                    continue
                id_estudiante = int(input(f"Ingrese el ID del estudiante ({inscripcion.id_estudiante}):  ")) or inscripcion.id_estudiante
                id_curso = int(input(f"Ingrese el ID del curso ({inscripcion.id_curso}):  ")) or inscripcion.id_curso
                fecha_inscripcion = input(f"Ingrese la fecha de inscripcion ({inscripcion.fecha_inscripcion}):  ") or inscripcion.fecha_inscripcion
                actualizar_inscripcion(id_inscripcion, id_estudiante, id_curso, fecha_inscripcion)
                input("Inscripcion actualizada con exito. Presione enter para continuar...")
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione enter para continuar...")

        elif opcion == "6":
            try:
                limpiar_consola()
                inscripciones = obtener_inscripciones()
                mostar_inscripciones(inscripciones)
                id_inscripcion = int(input("Ingrese el ID de la inscripcion: "))
                inscripcion = obtener_inscripcion_por_id(id_inscripcion)
                if not inscripcion:
                    print(f"No se encontro la inscripcion con ID {id_inscripcion}.")
                    input("Presione enter para continuar...")
                    continue
                eliminar_inscripcion(id_inscripcion)
                input("Inscripcion eliminada con exito. Presione enter para continuar...")
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione enter para continuar...")

        elif opcion == "7":
            break