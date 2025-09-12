from utn_fra.datasets import (
        lista_autos_marcas,
        lista_autos_modelos,
        lista_autos_cantidades,
        lista_autos_precios
    )


# Recorrer la lista imprimiendo por consola el modelo de autos que hay en cada garage
def imprimir_modelos(lista_modelos:list)->None:
    """
    Muestra por consola los modelos de auto que hay por cada garage
    
    :params: lista_modelos(list) = La lista de modelos de autos
    
    :returns: 
    Imprime la cantidad de modelos de autos
    """
    
    for indice in range(len(lista_modelos)):
        modelo_actual = lista_modelos[indice]
        mensaje = f"En el garage N°{indice + 1} esta el modelo {modelo_actual}"
        print(mensaje)


# Recorrer la lista imprimiendo por consola el modelo de autos que hay en cada garage 
# junto con la cantidad que posee.

def imprimir_modelo_y_cantidad(lista_modelo:list, lista_cantidaes:list)->None:
    """
    Muestra por consola el modelo de auto de cada garage con su cantidad
    
    :params: lista_modelos(list) = La lista de modelos de autos
    :params: lista_cantidades(list) = La lista de cantidades de autos
    
    :returns:
    Devuelve por consola el modelo del auto con su cantidad
    """
    
    for indice in range(len(lista_modelo)):
        modelo_actual = lista_modelo[indice]
        cantidad_actual = lista_cantidaes[indice]
        mensaje = f"Garage N°{indice + 1}: modelo - {modelo_actual} | cantidad {cantidad_actual}"
        print(mensaje)
        

# Recorrer las listas y determinar cuál es el modelo de auto que más cantidad 
# posee la concesionaria (MÁXIMO).

def 
