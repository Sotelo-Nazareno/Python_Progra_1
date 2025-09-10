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

def multiplicar_elementos

mi_lista = [0,-1,2,3,4,5]
print(promediar_elementos_positivos(mi_lista))