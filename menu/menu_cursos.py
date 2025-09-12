from controller.cursos_controller import obtener_cursos, registro_curso, actualizar_curso, eliminar_curso

def menuCursos():
    while True:
        print('Menu de cursos')
        print('1. Obtener cursos')
        print('2. Registrar curso')
        print('3. Actualizar curso')
        print('4. Eliminar curso')
        print('5. Salir')

        opcion = input('Seleccione una opcion: ')

        if opcion == '1':
            cursos = obtener_cursos()
            if not cursos:
                print('No se encontraron cursos')
                continue
            for curso in cursos:
                print(curso)
        elif opcion == '2':
            nombre_curso = input('Ingrese el nombre del curso: ')
            descripcion = input('Ingrese la descripcion del curso: ')
            creditos = input('Ingrese los creditos del curso: ')
            id_docente = input(int('Ingrese el id del docente: '))
            registro_curso(nombre_curso, descripcion, creditos, id_docente)
        elif opcion == '3':
            id_curso = input(int('Ingrese el id del curso: '))
            nombre_curso = input('Ingrese el nombre del curso: ')
            descripcion = input('Ingrese la descripcion del curso: ')
            creditos = input('Ingrese los creditos del curso: ')
            id_docente = input('Ingrese el id del docente: ')
            actualizar_curso(id_curso, nombre_curso, descripcion, creditos, id_docente)
        elif opcion == '4':
            id_curso = input(int('Ingrese el id del curso: '))
            eliminar_curso(id_curso)
        elif opcion == '5':
            break