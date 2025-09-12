from menu.menu_cursos import menuCursos

def menuGeneral():
    while True:
        print('Menu general')
        print('1. Cursos')
        print('2. Salir')

        opcion = input('Seleccione una opcion: ')

        if opcion == '1':
            menuCursos()
        elif opcion == '2':
            break