import funciones as fn
import os

def mostrar_menu(lista_marcas:list, lista_modelos:list, lista_cantidades:list, lista_precios:list)->None:
    """
    Eligue la opcion que el usuario ingresa

    :params: lista_marcas(list) = Lista de marcas que ingresa el usuario
    :params: lista_modelos(list) = Lista de modelos que ingresa el usuario
    :params: lista_cantidades(list) = Lista de cantidades que ingresa el usuario
    :params: lista_precios(list) = Lista de precios que ingresa el usuario

    :returns:
    Devuelve la opcion que el usuario eligio
    """

    corriendo = True

    while corriendo:

        opciones =\
        f"""

        [1] Recorrer la lista imprimiendo por consola el modelo de autos que hay en cada garage.
        [2] Recorrer la lista imprimiendo por consola el modelo de autos que hay en cada garage junto con la cantidad que posee. 
        [3] Recorrer las listas y determinar cuál es el modelo de auto que más cantidad posee la concesionaria (MÁXIMO). 
        [4] Recorrer las listas y determinar cuál es el modelo de auto que menos cantidad posee la concesionaria (MÍNIMO). 
        [5] Recorrer la lista y determinar la cantidad promedio de autos por garage.
        [6] Calcular e informar cuál es el modelo de autos más costoso.
        [7] Calcular e informar cuál es el modelo de auto menos costoso.
        [8] Determinar el valor promedio de todos los autos de la concesionaria e informar qué modelos de autos están por debajo de ese valor.
        [9] Calcular e informar la cantidad total de autos por marca.
        [10] Calcular e informar el porcentaje de autos por modelo.
        [11] Calcular e informar el porcentaje de autos por marca.
        [12] Ordenar las listas según precio ASC
        [13] Ordenar las listas según cantidad DESC
        [14] Salir
        """
        print(opciones)
        
        eleccion = input("Eliga una opcion de nuestro menu: ")

    #    validacion recursiva
        match eleccion:
            case "1":
                fn.imprimir_modelos(lista_modelos)
            case "2":
                fn.imprimir_modelo_y_cantidad(lista_modelos, lista_cantidades)
            case "3":
                fn.encontrar_modelo_segun_condicion(lista_modelos, lista_cantidades, "mayor", "cantidad")
            case "4":
                fn.encontrar_modelo_segun_condicion(lista_modelos,lista_cantidades, "menor","cantidad")
            case "5":
                print(fn.promediar_cantidad_autos(lista_cantidades))
            case "6":
                fn.encontrar_modelo_segun_condicion(lista_modelos, lista_precios, "mayor", "precio")
            case "7":
                fn.encontrar_modelo_segun_condicion(lista_modelos, lista_precios,"menor", "precio")
            case "8":
                fn.mostrar_debajo_promedio(lista_precios, lista_modelos)
            case "9":
                fn.sumar_cantidad_por_marca(lista_marcas, lista_cantidades)
            case "10":
                fn.promediar_por_condicion(lista_modelos, lista_cantidades)
            case "11":
                fn.promediar_por_condicion(lista_marcas,lista_cantidades)
            case "12":
                print(fn.ordenar_lista(lista_precios,"ASC"))
            case "13":
                print(fn.ordenar_lista(lista_cantidades,"DESC"))
            case "14":
                print("Gracias por su visita, nos vemos pronto!")
                corriendo = False

        os.system('pause')
        os.system('cls')