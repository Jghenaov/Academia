from controller.cursos_controller import obtener_cursos, registro_curso, actualizar_curso, eliminar_curso, mostrar_cursos_docente, existe_docente
from controller.docentes_controller import obtener_docentes
from views.vista_cursos import mostrar_cursos, mostrar_curso_por_docente
from views.vista_docentes import mostrar_docentes
from utils.others import limpiar_consola



def menuCursos():
    while True:
        limpiar_consola()  
        print('----------Menu de cursos----------')
        print('\n1. Obtener cursos')
        print('2. Registrar curso')
        print('3. Actualizar curso')
        print('4. Eliminar curso')
        print('5. Mostrar cursos de un docente')
        print('6. Salir')
        print('----------------------------------')

        opcion = input('\nSeleccione una opcion: ')

        if opcion == '1':
            limpiar_consola()
            cursos = obtener_cursos()
            if not cursos:
                print('No se encontraron cursos')
                input('Presione enter para continuar...')
                continue
            mostrar_cursos(cursos)
            input('Presione enter para continuar...')
                
        elif opcion == '2':
            limpiar_consola()
            nombre_curso = input('Ingrese el nombre del curso: ')
            descripcion = input('Ingrese la descripcion del curso: ')
            creditos = input('Ingrese los creditos del curso: ')
            try:
                id_docente = int(input('Ingrese el id del docente: '))
                if not existe_docente(id_docente):
                    print('El id del docente no existe')
                    input('Presione enter para continuar...')
                    continue
            except ValueError:
                print('El id del docente debe ser un numero')
                input('Presione enter para continuar...')
                continue           
            registro_curso(nombre_curso, descripcion, creditos, id_docente)
            input('Curso registrado exitosamente, presione enter para continuar...')
            
        elif opcion == '3':
            limpiar_consola()
            cursos = obtener_cursos()
            mostrar_cursos(cursos)
            if not cursos:
                print('No se encontraron cursos')
                input('Presione enter para continuar...')
                continue
            id_curso = int(input('Ingrese el id del curso: '))
            nombre_curso = input('Ingrese el nombre del curso: ')
            descripcion = input('Ingrese la descripcion del curso: ')
            creditos = input('Ingrese los creditos del curso: ')
            id_docente = input('Ingrese el id del docente: ')
            actualizar_curso(id_curso, nombre_curso, descripcion, creditos, id_docente)
            input('Curso actualizado exitosamente, presione enter para continuar...')
            
        elif opcion == '4':
            limpiar_consola()
            cursos = obtener_cursos()
            mostrar_cursos(cursos)
            if not cursos:
                print('No se encontraron cursos')
                input('Presione enter para continuar...')
                continue
            id_curso = int(input('Ingrese el id del curso: '))
            confirmacion = input('Desea eliminar el curso? (s/n): ')
            if confirmacion.lower() == 's':
                eliminar_curso(id_curso)
            input('Curso eliminado exitosamente, presione enter para continuar...')
            
        elif opcion == '5':
            limpiar_consola()
            docentes = obtener_docentes()
            mostrar_docentes(docentes)
            id_docente = int(input('Ingrese el id del docente: '))
            if not existe_docente(id_docente):
                print('El id del docente no existe')
                input('Presione enter para continuar...')
                continue
            cursos = mostrar_cursos_docente(id_docente) 
            if not cursos:
                print('No se encontraron cursos')
                input('Presione enter para continuar...')
                continue
            mostrar_curso_por_docente(cursos)  
            input('Presione enter para continuar...')
                
        elif opcion == '6':            
            break