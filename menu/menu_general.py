from menu.menu_cursos import menuCursos, limpiar_consola

def menuGeneral():
    while True:
        limpiar_consola()
        print('----------Menu general----------')
        print('\n1. Cursos')
        print('2. Salir')
        print('-------------------------------')

        opcion = input('\nSeleccione una opcion: ')

        if opcion == '1':
            menuCursos()
        elif opcion == '2':
            break