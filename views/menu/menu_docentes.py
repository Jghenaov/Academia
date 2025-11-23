from controller.docentes_controller import registro_docente, obtener_docentes, obtener_docente_por_id, actualizar_docente, eliminar_docente, existe_numero_documento
from views.vista_docentes import mostrar_docentes, mostrar_docente
from utils.others import limpiar_consola

def menuDocentes():
    while True:
        limpiar_consola()  
        print('----------Menu de docentes----------')
        print('\n1. Obtener docentes')
        print('2. Registrar docente')
        print('3. Actualizar docente')
        print('4. Eliminar docente')
        print('5. Mostrar docente por id')
        print('6. Salir')
        print('----------------------------------')

        opcion = input('\nSeleccione una opcion: ')

        if opcion == '1':
            limpiar_consola()
            docentes = obtener_docentes()
            if not docentes:
                print('No se encontraron docentes')
                input('Presione enter para continuar...')
                continue
            mostrar_docentes(docentes)
            input('Presione enter para continuar...')
                
        elif opcion == '2':
            limpiar_consola()
            numero_documento = input('Ingrese el numero de documento: ')
            if existe_numero_documento(numero_documento):
                print('El numero de documento ya existe')
                input('Presione enter para continuar...')
                continue
            nombre = input('Ingrese el nombre del docente: ')
            apellido = input('Ingrese el apellido del docente: ')
            email = input('Ingrese el email del docente: ')
            especialidad = input('Ingrese la especialidad del docente: ')
            registro_docente(numero_documento, nombre, apellido, email, especialidad)
            input('Docente registrado exitosamente. Presione enter para continuar...')

        elif opcion == '3':
            limpiar_consola()
            docentes = obtener_docentes()
            mostrar_docentes(docentes)
            id_docente = int(input("Ingrese el ID del docente a actualizar: "))
            docente = obtener_docente_por_id(id_docente)
            if docente:
                print(f"\nDocente encontrado: {docente.nombre} {docente.apellido}")
                print("Ingrese los nuevos datos (dejar vacío para mantener el actual):")

                numero_documento = input(f"Ingresa nuevo numero de documento [{docente.numero_documento}]: ") or docente.numero_documento
                nombre = input(f"Ingresa nuevo Nombre [{docente.nombre}]: ") or docente.nombre
                apellido = input(f"Apellido [{docente.apellido}]: ") or docente.apellido
                email = input(f"Email [{docente.email}]: ") or docente.email
                especialidad = input(f"Especialidad [{docente.especialidad}]: ") or docente.especialidad

                actualizado = actualizar_docente(id_docente, numero_documento, nombre, apellido, email, especialidad)
                if actualizado:
                    print("Docente actualizado exitosamente.")
                else:
                    print("Error al actualizar el docente.")
            else:
                print("Docente no encontrado.")
            input('Docente actualizado exitosamente. Presione enter para continuar...')

        elif opcion == '4':
            limpiar_consola()
            docentes = obtener_docentes()
            mostrar_docentes(docentes)
            try:
                id_docente = int(input("Ingrese el ID del docente a eliminar: "))
                busqueda = obtener_docente_por_id(id_docente)
                if not busqueda:
                    print("Docente no encontrado.")
                    input('Presione enter para continuar...')
                    continue
                confirmacion = input(f"Está seguro de eliminar el docente {busqueda.nombre} {busqueda.apellido}? (S/N): ")
                if confirmacion.lower() == 's':
                    eliminar_docente(id_docente)
                    print("Docente eliminado exitosamente.")
                else:
                    print("Operación cancelada.")
            except ValueError:
                print("ID de docente inválido.")
            input('Docente eliminado exitosamente. Presione enter para continuar...')

        elif opcion == '5':
            limpiar_consola()
            docentes = obtener_docentes()
            mostrar_docentes(docentes)
            try:
                id_docente = int(input("Ingrese el ID del docente: "))
                docente = obtener_docente_por_id(id_docente)
                if docente:
                    mostrar_docente(docente)
                else:
                    print("Docente no encontrado.")
            except ValueError:
                print("ID de docente inválido.")
            input('Docente obtenido exitosamente. Presione enter para continuar...')

        elif opcion == '6':
            break