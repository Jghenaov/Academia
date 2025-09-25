from controller.estudiante_controller import  * #registro_estudiante, obtener_estudiantes, obtener_estudiante_por_id, actualizar_estudiante, eliminar_estudiante
from views.vista_estudiante import mostrar_estudiantes, mostrar_estudiante
from utils.others import limpiar_consola

def menuEstudiantes():
    while True:
        limpiar_consola()
        print("----------Menu de estudiantes----------")
        print("\n1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar estudiante por ID")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            limpiar_consola()
            numero_documento = input("Ingrese el numero de documento: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
            email = input("Ingrese el email: ")
            telefono = input("Ingrese el telefono: ")
            registro_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
            input("Presione enter para continuar...")
            
        elif opcion == "2":
            limpiar_consola()
            estudiantes = obtener_estudiantes()
            if not estudiantes:
                print("No se encontraron estudiantes")
                input("Presione enter para continuar...")
                continue
            mostrar_estudiantes(estudiantes)
            input("Presione enter para continuar...")
            
        elif opcion == "3":
            limpiar_consola()
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                estudiante = obtener_estudiante_por_id(id_estudiante)
                if estudiante:
                    mostrar_estudiante(estudiante)
                    input("Presione enter para continuar...")
                else:
                    print("Estudiante no encontrado")
                    input("Presione enter para continuar...")
            except ValueError:
                print("ID inválido")
                input("Presione enter para continuar...")
                
        elif opcion == "4":
            limpiar_consola()
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                estudiante = obtener_estudiante_por_id(id_estudiante)
                if estudiante:
                    print(f'Estudiante encontrado: {estudiante.nombre} {estudiante.apellido}')
                    print('Ingrese los nuevos datos (dejar en blanco si no desea actualizar para mantener el dato actual)')
                    
                    numero_documento = input(f'Ingresa nuevo numero de documento ({estudiante.numero_documento}): ') or estudiante.numero_documento
                    nombre = input(f'Ingresa nuevo nombre ({estudiante.nombre}): ') or estudiante.nombre
                    apellido = input(f'Ingresa nuevo apellido ({estudiante.apellido}): ') or estudiante.apellido
                    fecha_nacimiento = input(f'Ingresa nueva fecha de nacimiento ({estudiante.fecha_nacimiento}): ') or estudiante.fecha_nacimiento
                    email = input(f'Ingresa nuevo email ({estudiante.email}): ') or estudiante.email
                    telefono = input(f'Ingresa nuevo telefono ({estudiante.telefono}): ') or estudiante.telefono
                    
                    actualizacion = actualizar_estudiante(id_estudiante, numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
                    if actualizacion:
                        print("Estudiante actualizado exitosamente")
                    else:
                        print("Error al actualizar el estudiante")
                else:
                    print("Estudiante no encontrado")
                input("Estudiantes actualizados exitosamente. Presione enter para continuar...")
                
            except ValueError as e:
                print("ERROR:", e )
                input("Presione enter para continuar...")
                
        elif opcion == "5":
            limpiar_consola()
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                estudiante = obtener_estudiante_por_id(id_estudiante)
                if estudiante:
                    eliminar_estudiante(id_estudiante)
                    print("Estudiante eliminado exitosamente")
                else:
                    print("Estudiante no encontrado")
                input("Estudiante eliminado exitosamente. Presione enter para continuar...")
            except ValueError as e:
                print("ERROR:", e )
                input("Presione enter para continuar...")
                
        elif opcion == "6":
            break