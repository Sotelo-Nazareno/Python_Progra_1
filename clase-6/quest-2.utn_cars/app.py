import funciones_nivel_1 as lvl1
from utn_fra.datasets import (
        lista_autos_marcas,
        lista_autos_modelos,
        lista_autos_cantidades,
        lista_autos_precios
    )



def elegir_opcion()->int|None:
    """
    Eligue la opcion que el usuario ingresa

    :returns:
    Devuelve la opcion que el usuario eligio
    """

    opcion_str = input("Eliga una opcion de nuestro menu: ")
    
    # validacion recursiva

    match opcion_str:
        case "1":
            lvl1.imprimir_modelos(lista_autos_modelos)
        case "2":
            lvl1.imprimir_modelo_y_cantidad(lista_autos_modelos, lista_autos_cantidades)
        case "3":
            