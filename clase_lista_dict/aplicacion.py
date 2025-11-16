from menu import stark_menu_principal
from funciones import (
    stark_imprimir_heroe_genero,
    stark_calcular_imprimir_heroe_genero,
    stark_calcular_imprimir_promedio_altura_genero
)

import os



def stark_marvel_app(lista_heroes: list[dict]) -> None:

    running = True
    lista_heroes_app = lista_heroes.copy()
    while running:

        
        opcion = stark_menu_principal()


        match opcion:
            case 1:
                stark_imprimir_heroe_genero(heroes=lista_heroes_app, genero='Masculino')
            case 2:
                stark_imprimir_heroe_genero(heroes=lista_heroes_app, genero='No-Binario')
            case 3:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='maximo', key='altura_mts', valor_genero='Masculino')
            case 4:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='maximo', key='altura_mts', valor_genero='No-Binario')
            case 5:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='minimo', key='fuerza', valor_genero='Masculino')
            case 6:
                stark_calcular_imprimir_heroe_genero(lista_heroes_app, calculo='minimo', key='fuerza', valor_genero='No-Binario')
            case 7:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes_app, key='fuerza', valor_genero='Masculino')
            case 8:
                stark_calcular_imprimir_promedio_altura_genero(lista_heroes_app, key='fuerza', valor_genero='No-Binario')
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                print('Gracias por usar la aplicación.')
                running = False
        os.system('pause')
        os.system('cls') # 'clear' para UNIX (Mac/Linux)
            

if __name__ == '__main__':

    from utn_fra.datasets import lista_alias_pp

    print('Hola Mundo')