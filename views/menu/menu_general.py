from .menu_cursos import menuCursos
from .menu_docentes import menuDocentes
from .menu_estudiante import menuEstudiantes
from utils.others import limpiar_consola

def menuGeneral():
    while True:
        limpiar_consola()
        print('----------Menu general----------')
        print('\n1. Cursos')
        print('2. Docentes')
        print('3. Estudiantes')
        print('4. Salir')
        print('-------------------------------')

        opcion = input('\nSeleccione una opcion: ')

        if opcion == '1':
            menuCursos()
        elif opcion == '2':
            menuDocentes()
        elif opcion == '3':
            menuEstudiantes()
        elif opcion == '4':
            break
        else:
            print('Opcion no valida')
            input('Presione enter para continuar...')