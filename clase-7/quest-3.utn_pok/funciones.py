
# 	[Nivel 1]

def crear_matriz(lista_a:list, lista_b:list, lista_c:list, lista_d:list, lista_e:list)->list[list]:
    """
    Crea una matriz

    :params: lista_a(list) = Lista que ingresa el usuario
    :params: lista_b(list) = Lista que ingresa el usuario
    :params: lista_c(list) = Lista que ingresa el usuario
    :params: lista_d(list) = Lista que ingresa el usuario
    :params: lista_e(list) = Lista que ingresa el usuario

    :returns:
    Devuelve una matriz con las listas dadas
    """

    mi_matriz = [
        lista_a, 
        lista_b, 
        lista_c, 
        lista_d, 
        lista_e
    ]

    return mi_matriz


def contar_elementos_matriz(matriz:list[list])->int:
    """
    Cuenta la cantidad de elementos que hay en una matriz

    :params: matriz(list[list]) = La matriz que ingresara el usuario

    :returns:
    Devuelve la cantidad de elementos de la matriz dada
    """

    return len(matriz[0])


def mostrar_cantidad_pokemons(matriz:list[list])->None:
    """
    
    """

    cantidad = contar_elementos_matriz(matriz)
    mensaje = f"En la pokedex hay actualmente {cantidad} pokemons"
    print(mensaje)


def obtener_datos_fila(matriz, indice):
    """
    
    """
    mensaje_fila =''
    fila_actual = matriz[indice]
    for indice_columna in range(len(fila_actual)):
        mensaje_fila = f' {mensaje_fila} | {fila_actual[indice_columna]:10} '
    mensaje_fila = f' {mensaje_fila} | \n ' 

    return mensaje_fila


def recorrer_matriz_fxc(matriz:list[list]):
    """
    Recorre una matriz en el orden de filas por columnas

    :params: matriz(list[list]) = La matriz que ingresa el usuario

    :returns:
    Devuelve la matriz en cadenas de strings de forma ordenada
    """

    matriz_mensaje = ''

    for indice_fila in range(len(matriz)):
        mensaje_fila = obtener_datos_fila(matriz, indice_fila)
        matriz_mensaje = f'{matriz_mensaje}{mensaje_fila}'
    print(matriz_mensaje)




def recorrer_matriz_cxf(matriz:list[list])->None:
    """
    Recorre una matriz en el orden de columnas por fila

    :params: matriz(list[list]) = La matriz que ingresa el usuario

    :returns:
    Devuelve la matriz en cadenas de strings de forma ordenada
    """

    # Me fijo la cantidad de columnas para saber hasta cuanto iterar
    cantidad_columnas = len(matriz[0])

    # comienzo con las columnas para hacer columnas x fila
    for indice_columna in range(cantidad_columnas):
        mensaje_matriz = ''

        # continuo con las filas
        for indice_fila in range(len(matriz)):
            mensaje_matriz =f'{mensaje_matriz:10}{matriz[indice_fila][indice_columna]:10}'

            # condicion para que en la ultima columna no termine con un -1 para contar al 0 en el indice ,
            if indice_fila < len(matriz) - 1:
                mensaje_matriz = f'{mensaje_matriz} | '

        print(mensaje_matriz)


def sumar_elementos_lista(lista:list)->int:
    """
    Suma todos los elementos de una lista

    :params: lista (list) = Lista que ingrese el usuario

    :returs:
    Devuelve la suma de la cantidades registradas de todos los autos
    """

    sumatoria = 0

    for indice in range(len(lista)):
        cantidad_actual = lista[indice]
        sumatoria += cantidad_actual
    return sumatoria


def promediar_cantidad_elementos(lista:list)->float:
    """
    Promedia la cantidad de autos por garage

    :params: lista_cantidades(list) = Lista de elementos

    :returns:
    Devuelve el promedio de autos por garage
    """

    cantidad_elementos = len(lista)
    promedio = sumar_elementos_lista(lista)/ cantidad_elementos
    if promedio < 1:
        return 0
    else:
        return promedio



def mostrar_mas_fuertes(matriz:list[list]):
    """
    Muestra por consola la infornacion de los pokemons mas fuerte

    :params: matriz(list[list]) = La pokedex del entrenador

    :returns:
    Devuelve la informacion de pokemons
    """

    matriz_filtrada = []
    promedio_poderes = promediar_cantidad_elementos(matriz[3])

    for indice_columna in range(len(matriz[3])):
        poder_actual = matriz[3][indice_columna]

        if poder_actual > promedio_poderes:
            columna_filtrada = []
            for indice_fila in range(len(matriz)):
                columna_filtrada.append(matriz[indice_fila][indice_columna])
            matriz_filtrada.append(columna_filtrada)



    recorrer_matriz_fxc(matriz_filtrada)
    mensaje = f'El promedio a superar era de {promedio_poderes} con {len(matriz_filtrada)} pokemons superandola'
    print(mensaje)


def mostrar_poekmons_tipo(matriz:list[list], tipo:str):
    """
    Muestra por consola la infornacion de los pokemons mas fuerte

    :params: matriz(list[list]) = La pokedex del entrenador

    :returns:
    Devuelve la informacion de pokemons
    """

    matriz_filtrada = []

    for indice_columna in range(len(matriz[2])):
        tipo_actual = matriz[2][indice_columna]

        if tipo_actual == tipo :
            columna_filtrada = []
            for indice_fila in range(len(matriz)):
                columna_filtrada.append(matriz[indice_fila][indice_columna])
            matriz_filtrada.append(columna_filtrada)



    recorrer_matriz_fxc(matriz_filtrada)
    mensaje = f'Los pokemons de tipo {tipo} son {len(matriz_filtrada)} en total'
    print(mensaje)



def ordenar_matriz(matriz:list[list], indice_a_ordenar:int, modo:str, condicion:str):
    """
    
    """

    

    for indice_columna in range(len(matriz[indice_a_ordenar]) - 1):
        if matriz[indice_a_ordenar +1] [indice_columna] == condicion:
            indice_elemento_menor = indice_columna

            for indice_columna_sig in range(indice_columna +1,len(matriz[indice_a_ordenar]), 1):
                if ( modo == "ASC" and matriz[indice_a_ordenar] [indice_elemento_menor] > matriz [indice_a_ordenar] [indice_columna_sig] or\
                    modo == "DESC" and matriz[indice_a_ordenar] [indice_elemento_menor] < matriz [indice_a_ordenar] [indice_columna_sig]):
                    indice_elemento_menor = indice_columna_sig

            if indice_elemento_menor != indice_columna:
                for indice_fila in range(len(matriz)):
                    elemento_auxiliar = matriz [indice_fila] [indice_elemento_menor]
                    matriz [indice_fila] [indice_elemento_menor] = matriz [indice_fila] [indice_columna]
                    matriz [indice_fila] [indice_columna] = elemento_auxiliar
        else:
            continue

    recorrer_matriz_cxf(matriz)
