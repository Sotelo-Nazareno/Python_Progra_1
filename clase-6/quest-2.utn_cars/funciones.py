# NIVEL 1


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

def imprimir_modelo_y_cantidad(lista_modelos:list, lista_cantidades:list)->None:
    """
    Muestra por consola el modelo de auto de cada garage con su cantidad
    
    :params: lista_modelos(list) = La lista de modelos de autos
    :params: lista_cantidades(list) = La lista de cantidades de autos
    
    :returns:
    Devuelve por consola el modelo del auto con su cantidad
    """
    
    for indice in range(len(lista_modelos)):
        modelo_actual = lista_modelos[indice]
        cantidad_actual = lista_cantidades[indice]
        mensaje = f"Garage N°{indice + 1}: modelo - {modelo_actual} | cantidad {cantidad_actual}"
        print(mensaje)
        

# Recorrer las listas y determinar cuál es el modelo de auto que más cantidad 
# posee la concesionaria (MÁXIMO).

#Recorrer las listas y determinar cuál es el modelo de auto que menos cantidad 
# posee la concesionaria (MÍNIMO).



def encontrar_modelo_segun_condicion(lista_modelos:list, lista_cantidades:list, modo:str = "mayor", tema:str = "precio")->None:
    """
    Encuentra el modelo que ingrese el usuario en la lista

    :params: lista_modelos(list) = Lista que ingrese el usuario
    :params: lista_cantidades(list) = Lista que ingrese el usuario
    :params: modo(str) = El orden que ingrese el usuario [mayor o menor] 
    :params: tema(str) = El tema del orden en que se va a encontrar el modelo

    :returns:
    Devuelve un elemento de la lista segun el orden que ingrese el usuario
    """

    cantidad_seleccionada = None
    elemento_seleccionado = None

    for indice_cantidad in range(len(lista_cantidades)):
        cantidad_actual = lista_cantidades[indice_cantidad]
        if cantidad_seleccionada == None or\
            (modo == "mayor" and cantidad_seleccionada < cantidad_actual) or\
            (modo == "menor" and cantidad_seleccionada > cantidad_actual):
            cantidad_seleccionada = cantidad_actual
            elemento_seleccionado = lista_modelos[indice_cantidad]

    if tema == "cantidad":
        mensaje = f"El modelo con {modo} cantidades es {elemento_seleccionado} con {cantidad_seleccionada}"
    else:
        mensaje = f"El modelo con {modo} precio es {elemento_seleccionado} con ${cantidad_seleccionada}"

    print(mensaje)


# NIVEL 2


# Recorrer la lista y determinar la cantidad promedio de autos por garage.

def sumar_elementos_lista(lista:list)->int:
    """
    Suma todos los autos

    :params: lista (list) = Lista que ingrese el usuario

    :returs:
    Devuelve la suma de la cantidades registradas de todos los autos
    """

    sumatoria = 0

    for indice in range(len(lista)):
        cantidad_actual = lista[indice]
        sumatoria += cantidad_actual
    return sumatoria

def promediar_cantidad_autos(lista:list)->float:
    """
    Promedia la cantidad de autos por garage

    :params: lista_cantidades(list) = Lista de las cantidades de autos

    :returns:
    Devuelve el promedio de autos por garage
    """

    garages = len(lista) +1 
    return sumar_elementos_lista(lista)/ garages


# Calcular e informar cuál es el modelo de autos más costoso.

# Calcular e informar cuál es el modelo de auto menos costoso.



#  Determinar el valor promedio de todos los autos de la concesionaria e informar qué modelos de autos están por debajo de ese valor.

def mostrar_debajo_promedio(lista_precios,lista_modelos):
    """
    Imprime por consola los modelos de autos que tienen un precio por debajo del promedio

    :params: lista_precios = La lista de precios de autos
    :params: lista_modelos = La lista de modelos de autos

    :returns:
    Devuelve los autos que tienen un precio por debajo al promedio
    """

    promedio = promediar_cantidad_autos(lista_precios)

    for indice_precio in range(len(lista_precios)):
        precio_actual = lista_precios[indice_precio]
        if precio_actual < promedio:
            modelo_pordebajo = lista_modelos[indice_precio]
            mensaje = f"El modelo {modelo_pordebajo} esta por debajo del promedio con un precio de ${precio_actual}"
            print(mensaje)



#           [Nivel 3]

def unir_arrays(lista_a:list, lista_b:list)->list:
    """
    Une los elementos de dos listas

    :params: lista_a(list) = Lista que ingresa el usuario 
    :params: lista_a(list) = Lista que ingresa el usuario 

    :returns:
    Devuelve los elementos que se encuentran en ambas listas sin repetir
    """


    for indice in range(len(lista_a)):
        elemento_actual__a = lista_a[indice]
        if not(elemento_actual__a in lista_b):
            lista_b.append(elemento_actual__a)
    
    return (lista_b)

def sumar_cantidad_por_marca(lista_marca:list, lista_cantidad:list)->None:
    """
    Suma la cantidades de autos por marcas

    :params: lista_cantidad(list) = La lista de marcas de los autos
    :params: lista_cantidad(list) = La lista de cantidades de autos

    :returns:
    Devuelve la cantidad total de autos por marca
    """

    vistos = unir_arrays(lista_marca, [])
    

    for indice_visto in range(len(vistos)):
        elemento_visto = vistos[indice_visto]
        cantidad_marca = 0
        for indice_marca in range(len(lista_marca)):
            if elemento_visto == lista_marca[indice_marca]:
                cantidad_marca += lista_cantidad[indice_marca]
        mensaje = f"La marca {elemento_visto} tiene {cantidad_marca} unidades"
        print(mensaje)


# [10] Calcular e informar el porcentaje de autos por modelo.

def promediar_por_condicion(lista_a:list, lista_cantidad:list):
    """
    Promedia la cantidades de autos por la condicion [marcas o modelos]

    :params: lista_a(list) = Lista la cual se promediara en base a ello
    :params: lista_cantidad(list) = Lista de cantidades de autos

    :returs:
    Devuelve el promedio de cantidades por la condicion de lista
    """

    lista_sin_repetir = unir_arrays(lista_a, [])

    for indice_visto in range(len(lista_sin_repetir)):
        elemento_visto = lista_sin_repetir[indice_visto]
        cantidad_total = 0
        for indice_modelo in range(len(lista_a)):
            if elemento_visto == lista_a[indice_modelo]:
                cantidad_total += lista_cantidad[indice_modelo]

        if cantidad_total == 0:
            promedio = 0
        else:
            promedio = cantidad_total / len(lista_sin_repetir)

        mensaje = f"Promedio {elemento_visto} de %{promedio} cantidades" 
        print(mensaje)


# [12] Ordenar las listas según precio ASC

def ordenar_lista(lista_a:list, modo= "ASC"):
    """
    Ordena una lista en orden ascendente o descendente
    :params: lista_a(list) = La lista que ingrese el usuario a ordenar
    :params: modo(str) = El orden que va a tener la lista

    :returns:
    Devuelve la lista ordenada
    """
    if len(lista_a) < 2:
        return lista_a
    
    pivot = lista_a.pop()  #primer elemento de la lista
    menores = []
    mayores = []


    for elemento in lista_a:
        if elemento > pivot:
            mayores.append(elemento)
        else:
            menores.append(elemento)

    if modo == "ASC":
        orden = ordenar_lista(menores) + [pivot] + ordenar_lista(mayores)
    else:
        orden = ordenar_lista(mayores) + [pivot] + ordenar_lista(menores)

    return orden
