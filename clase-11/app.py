from menu import stark_menu_principal
import os
from functions import(
    stark_imprimir_heroe_genero,
    stark_calcular_imprimir_heroe_genero,
    stark_calcular_imprimir_promedio_altura_genero,
    stark_calcular_cantidad_por_tipo,
    stark_listar_heroes_por_dato
)

def stark_marvel_app(lista_heroes:list[dict])->None:
    """
    Crea una aplicacion de heroes e imrpime por consola los resultados

    Args:
        lista_heroes (list[dict]): La lista de heroes 
    """

    running = True

    while running:

        lista_heroes_copia = lista_heroes.copy()
        opcion = stark_menu_principal()

        match opcion:
            case 1:
                stark_imprimir_heroe_genero(lista_heroes_copia, 'Masculino')
            case 2:
                stark_imprimir_heroe_genero(lista_heroes_copia, 'Femenino')
            case 3:
                stark_calcular_imprimir_heroe_genero(lista_heroes_copia, 'maximo', 'altura_mts', 'Masculino')
            case 4:
                stark_calcular_imprimir_heroe_genero(lista_heroes_copia, 'maximo', 'altura_mts', 'Femenino')
            case 5:
                stark_calcular_imprimir_heroe_genero(lista_heroes_copia, 'minimo', 'altura_mts', 'Masculino')
            case 6:
                stark_calcular_imprimir_heroe_genero(lista_heroes_copia, 'minimo', 'altura_mts', 'Femenino')
            case 7:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes_copia, 'altura_mts', 'Masculino')
            case 8:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes_copia, 'altura_mts', 'Femenino')
            case 9:
                stark_nombres_asociados(lista_heroes_copia)
            case 10:
                stark_calcular_cantidad_por_tipo(lista_heroes_copia, 'color_ojos')
            case 11:
                stark_calcular_cantidad_por_tipo(lista_heroes_copia, 'color_pelo')
            case 12:
                stark_calcular_cantidad_por_tipo(lista_heroes_copia, 'inteligencia')
            case 13:
                stark_listar_heroes_por_dato(lista_heroes_copia, "color_ojos")
            case 14:
                stark_listar_heroes_por_dato(lista_heroes_copia, "color_pelo")
            case 15:
                stark_listar_heroes_por_dato(lista_heroes_copia, "inteligencia")
            case 16:
                running = False
                print("Nos vemos!")

        os.system('pause')
        os.system('clear')