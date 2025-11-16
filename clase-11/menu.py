from validations import validar_rango


def obtener_menu()->str:
    """
    Obtiene el menu de opciones

    Returns:
    str: Devuelve un texto de opciones
    """

    mensaje=\
    """
    1- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    2- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    3- Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
    4- Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
    5- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
    6- Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
    7- Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
    8- Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
    9- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    10- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    11- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    12- Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
    13- Listar todos los superhéroes agrupados por color de ojos.
    14- Listar todos los superhéroes agrupados por color de pelo.
    15- Listar todos los superhéroes agrupados por tipo de inteligencia
    16- Salir
    """

    return mensaje

def mostrar_menu()->None:
    """
    Imprime por consola el menu de opciones
    """

    menu_opciones = obtener_menu()
    print(menu_opciones)


def imprimir_menu()->None:
    """
    Imprime por consola las opciones del menu
    """

    mostrar_menu()


# Crear la función ‘stark_menu_principal’ la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de 
# las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero. 

def stark_menu_principal()->None:
    """
    Imprime las opciones del menu y le pide al usuario una opcion
    """

    imprimir_menu()
    seleccion = validar_rango(1, 16)
    return seleccion