from menu.menu_cursos import menuCursos, limpiar_consola
from menu.menu_docentes import menuDocentes

def menuGeneral():
    while True:
        limpiar_consola()
        print('----------Menu general----------')
        print('\n1. Cursos')
        print('2. Docentes')
        print('3. Salir')
        print('-------------------------------')

        opcion = input('\nSeleccione una opcion: ')

        if opcion == '1':
            menuCursos()
        elif opcion == '2':
            menuDocentes()
        elif opcion == '3':
            break