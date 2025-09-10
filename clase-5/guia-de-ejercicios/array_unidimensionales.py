"Arrays unidimensionales"

# 1. Desarrollar una función que permita crear un array de números con la cantidad de elementos
# que establezca el parámetro recibido.

def crear_array_con_n_elementos(cantidad: int)->list:
    """
    Crea un array con la cantidad de elementos del valor ingresado
    
    :params: cantidad(int) = Cantidad que ingrese el usuario
    
    :returns:
    Devuelve una lista con la cantidad de elementos ingresado
    """
    mi_lista = []
    
    for elemento in range(cantidad):
        elemento += 1
        mi_lista.append(elemento)
    return mi_lista


# 2.Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  
# Crear el array con la función del punto 1.


        
# 3. Escribir una función que reciba una lista de enteros,
# la misma calculará y devolverá el promedio de todos los números. 

def promediar_elementos_lista(lista_numeros:list)->int:
    """
    Calcula el promedio de todos los elementos de la lista ingresada
    
    :params: lista_numeros(list) = La lista de numeros que ingresa el usuario
    
    :returns:
    Devuelve el promedio de todos los elementos de la lista
    """
    
    sumatoria = 0
    
    for indice in range(len(lista_numeros)):
        elemento = lista_numeros[indice]
        sumatoria += elemento
    return sumatoria / len(lista_numeros)
    

# 4. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver 
# el promedio de los números positivos.

def promediar_elementos_positivos(lista_numeros:list)->int:
    """
    Calcula el promedio de los numeros positivos
    
    :params: lista_numeros(list) = Lista de numeros qu ingresa el usuario
    
    :returns:
    Devuelve el promedio de todos los numeros positivos
    """
    sumatoria_positiva = 0
    cantidad_positivo = 0
    
    for indice in range(len(lista_numeros)):
        elemento = lista_numeros[indice]
        if elemento > 0:
            cantidad_positivo +=1
            sumatoria_positiva += elemento
    return sumatoria_positiva / cantidad_positivo


# 5.Escribir una función que calcule y retorne el producto de todos los elementos de la 
# lista que recibe como parámetro

def multiplicar_elementos(lista_numeros:list)->int:
    """
    Calcula la multiplicacion de todos los elementos de la lista ingresada

    :params: lista_numeros (list) = La lista de numeros que ingresa el usuario

    :returns: 
    Devuelve el resultado de multiplicar todos los elementos de la lista
    """

    resultado = 1

    for indice in range(len(lista_numeros)):
        elemento = lista_numeros[indice]
        resultado *= elemento
    return(resultado)


# 6. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def encontrar_el_mayor(lista_numeros:list)->int:
    """
    Encuentra el elemento mayor dentro de la lista ingresada por el usuario.
    La lista debe contener elementos del tipo int o float

    :params: lista_numeros(list) = La lista que ingresa el usuario

    :returns:
    Devuelve la posicion del elemento mayor
    """

    elemento_mayor = None
    posicion_mayor = None

    for indice in range(len(lista_numeros)):
        elemento_actual = lista_numeros[indice]
        if (elemento_mayor == None or elemento_mayor < elemento_actual):
            elemento_mayor = elemento_actual
            posicion_mayor = indice
    return(posicion_mayor)
            

# 7. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def encontrar_mayores(lista_numeros:list)->list:
    """
    Encuentra el/los elemento/s mayor/es que contenga una lista de elementos. 
    La lista debe contener elementos de tipo int o float

    :params: lista_numeros(list) = La lista que ingrese el usuario.

    :returns:
    Devuelve la lista de posiciones de los elementos mayor que se pueda llegar a repetir en la lista
    """

    posiciones_mayores = []
    elemento_mayor = None
    posicion_mayor = None

    for indice in range(len(lista_numeros)):
        elemento_actual = lista_numeros[indice]
        if (elemento_mayor == None or elemento_mayor < elemento_actual):
            elemento_mayor = elemento_actual
            posicion_mayor = indice
            posiciones_mayores = []
            posiciones_mayores.append(posicion_mayor)
        elif elemento_mayor == elemento_actual:
            elemento_mayor = elemento_actual
            posicion_mayor = indice
            posiciones_mayores.append(posicion_mayor)

    
    return posiciones_mayores


# 8. Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
#   Una lista de nombres (lista_nombres).
#   Un nombre a buscar en la lista (nombre_antiguo).
#   Un nombre de reemplazo (nombre_nuevo).
#   La función debe realizar las siguientes acciones:
#   Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
#   Retornar la cantidad total de reemplazos realizados.

def reemplazar_nombres(lista_nombres:list, nombre_antiguo:str, nombre_nuevo:str)->int:
    """
    Remplaza las aparciones de nombre_antiguo por nombre_nuevo en la lista ingresada por el usuario.

    :params: lista_nombres(list) = La lista que ingresa el usuario
    :params: nombre_antiguo(str) = El nombre al cual se quiere reemplazar
    :params: nombre_nuevo(str) = El nombre que reemplaza

    :returns:
    Devuelve la cantidad de aparicones de nombre_antiguo y en la lista por nombre_nuevo
    """

    cantidad_reemplazos = 0

    for indice in range(len(lista_nombres)):
        nombre_actual = lista_nombres[indice]
        if nombre_actual == nombre_antiguo:
            cantidad_reemplazos +=1
            lista_nombres[indice] = nombre_nuevo
    return cantidad_reemplazos


# 9. Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

def interseccionar_arrays(lista_a:list, lista_b:list)->list:
    """
    Intersecciona los elementos de dos lista

    :params: lista_a(list) = Lista que ingresa el usuario 
    :params: lista_a(list) = Lista que ingresa el usuario 

    :returns:
    Devuelve los elementos en comun que se encuentran en ambas listas sin repetir
    """

    interseccion = []

    for indice in range(len(lista_a)):
        elemento_actual_a = lista_a[indice]
        for indice in range(len(lista_b)):
            elemento_actual_b = lista_b[indice]
            if (elemento_actual_a == elemento_actual_b and not(elemento_actual_a in interseccion)):
                interseccion.append(elemento_actual_a)
    return interseccion


# 10. Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

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


# 11. Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.

def diferenciar_arrays(lista_a:list, lista_b:list)->list:
    """
    Diferencia la primer lista de las segunda quedando solo los elementos que se encuentre unicamente en la primer lista

    :params: lista_a(list) = Lista que ingresa el usuario 
    :params: lista_a(list) = Lista que ingresa el usuario 

    :returns:
    Devuelve los elementos que se encuentran unicamente en la primer lista
    """

    resultado = []

    for indice in range(len(lista_a)):
        elemento_actual = lista_a[indice]
        if not(elemento_actual in lista_b):
            resultado.append(elemento_actual)

    return resultado
