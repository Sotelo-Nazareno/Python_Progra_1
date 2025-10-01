

def crear_matriz(lista_a:list, lista_b:list, lista_c:list, lista_d:list)-> list[list]:
    """
    Crea una matriz

    :params: lista_a(list) = La lista que ingrese el usuario 
    :params: lista_b(list) = La lista que ingrese el usuario 
    :params: lista_c(list) = La lista que ingrese el usuario 
    :params: lista_d(list) = La lista que ingrese el usuario 

    :returns: 
    Devuelve una matriz con las listas ingresadas
    """

    mi_matriz = [
        lista_a, 
        lista_b, 
        lista_c, 
        lista_d
    ]
    print("La matriz ya esta creada")
    return mi_matriz


def contar_cantidad_elementos(matriz:list[list])->int:
    """
    Cuenta la cantidad de elementos que hay en una matriz

    :params: matriz(list[list]) = La matriz que ingresa el usuario

    :returns:
    Devuelve la cantidad de elementos que hay en la matriz ingresada
    """

    return len(matriz[0])


def recorrer_matriz_cxf(matriz:list[list])->None:
    """
    Imprime por consola los datos de una matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario

    :returns:
    None
    """

    cantidad_columnas = len(matriz[0])

    for indice_columna in range(cantidad_columnas):
        mensaje_matriz = ""
        for indice_fila in range(len(matriz)):
            mensaje_matriz = f"{mensaje_matriz}{matriz[indice_fila][indice_columna]}"

            if indice_fila < len(matriz) - 1:
                mensaje_matriz = f"{mensaje_matriz}, "
        
        print(mensaje_matriz)


def promediar_elementos(matriz:list[list], indice_fila:int)->float:
    """
    Promedia los elementos de una matriz

    :params: matriz(list[list]) = La matriz que ingresa el usuario
    :params: indice_fila(int) = El indice en el cual se desea sacar el promedio en una matriz
    """

    total_elementos = contar_cantidad_elementos(matriz)
    sumatoria = 0

    for indice_fila in (matriz[indice_fila]):
        sumatoria += int(indice_fila)


    if sumatoria > 0:
        promedio = sumatoria / total_elementos
    else:
        promedio = 0

    return promedio


def filtrar_matriz_segun_promedio(matriz:list[list], indice_a_filtrar:int, dato_filtrar:str, modo:str)->None:
    """
    Filtra una matriz por el indice dado

    :params: matriz(list[list]) = La matriz que ingrese el usuario
    :params: indice_a_filtrar(int) = El indice en el cual se filtrara la matriz

    :returns: 
    None
    """

    cantidad_columnas = len(matriz[indice_a_filtrar])
    promedio_alturas = promediar_elementos(matriz, indice_a_filtrar)


    for indice_columna in range(cantidad_columnas):
        mensaje_filtrado = ""
        if ((modo == "DES" and int(matriz[indice_a_filtrar][indice_columna]) < promedio_alturas) or
            (modo == "ASC" and int(matriz[indice_a_filtrar][indice_columna]) > promedio_alturas)):
            if matriz[1][indice_columna] == dato_filtrar:
                for indice_fila in range(len(matriz)):
                    mensaje_filtrado = f"{mensaje_filtrado}{matriz[indice_fila][indice_columna]} "
                    
                print(mensaje_filtrado)


def filtrar_matriz(matriz:list[list], indice_a_filtrar:int, dato_filtrar:str)->list[list]:
    """
    Filtra una matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario
    :params: indice_a_filtrar(int) = El indice el cual se filtrara
    :params: dato_filtrar = El dato a cual se filtrara

    :returns:
    Devuelve la matriz filtrada
    """

    matriz_filtrada = [
        [],
        [],
        [],
        []
    ]

    cantidad_columnas = len(matriz[indice_a_filtrar])
    cantidad_filas = len(matriz)
    

    for indice_columna in range(cantidad_columnas):
        if matriz[indice_a_filtrar][indice_columna] == dato_filtrar:
            for indice_fila in range(cantidad_filas):
                dato_filtrada = matriz[indice_fila][indice_columna]
                matriz_filtrada[indice_fila].append(dato_filtrada)
    return matriz_filtrada


def ordenar_matriz(matriz:list[list],indice_ordenar, modo:str)->list[list]:
    """
    Ordena la matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario
    :params: indice_ordenar(int) = El indice el cual se ordenara la matriz
    :params: modo(str) = El orden de la matriz

    :returns:
    Devuelve la matriz ordenada
    """

    for indice_columna in range(len(matriz[indice_ordenar])-1):
        elemento_seleccionado = indice_columna

        for sig_indice_columna in range(indice_columna +1, len(matriz[indice_ordenar]), 1):
            if ( modo == "ASC" and matriz[indice_ordenar] [elemento_seleccionado] > matriz [indice_ordenar] [sig_indice_columna] or\
                modo == "DESC" and matriz[indice_ordenar] [elemento_seleccionado] < matriz [indice_ordenar] [sig_indice_columna]):
                elemento_seleccionado = sig_indice_columna

            if elemento_seleccionado != indice_columna:
                auxiliar = matriz [indice_ordenar] [elemento_seleccionado]
                matriz [indice_ordenar] [elemento_seleccionado] = matriz[indice_ordenar][indice_columna] 
                matriz[indice_ordenar][indice_columna] = auxiliar

    return matriz


def ordenar_matriz_segun_genero(matriz:list[list], indice:int, genero:str, modo:str)->None:
    """
    Imprime ordenada la matriz segun el genero

    :params: matriz(list[list]) = La matriz que ingrese el usuario
    :params: indice(int) = El indice el cual se ordenara
    :params: genero(str) = El genero a filtrar
    :params: modo(str) = El orden en que se ejecuta

    :returns:
    None
    """
    matriz_filtrada = filtrar_matriz(matriz, 1, genero)
    matriz_ordenada = ordenar_matriz(matriz_filtrada, indice, modo)
    recorrer_matriz_cxf(matriz_ordenada)


def trasponer_matriz_ordenada(matriz:list[list], indice:int, modo:str):
    """
    Imprime la matriz traspuesta y ordenada

    :params: matriz(list[list]) = La matriz que ingrese el usuario
    :params: indice(int) = El indice el cual se ordenara
    :params: modo(str) = El orden en que se ejecuta

    :return:
    None
    """

    matriz_ordenada = ordenar_matriz(matriz, indice, modo)
    recorrer_matriz_cxf(matriz_ordenada)