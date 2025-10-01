"""
Crear Matriz: para ello deberá crear una función que en base a las listas, cree una matriz con los datos para trabajar.

"""

def crear_matriz(lista_a:list, lista_b:list, lista_c:list)->list[list]:
    """
    Crea una matriz

    :params: lista_a(list) = La lista que ingrese el usuario
    :params: lista_b(list) = La lista que ingrese el usuario
    :params: lista_c(list) = La lista que ingrese el usuario

    :returns:
    Devuelve una matriz con las listas asignadas
    """

    mi_matriz = [
        lista_a,
        lista_b,
        lista_c
    ]

    return mi_matriz


def cantidad_filas(matriz:list[list])->int:
    """
    Cuenta la cantidad de filas de una matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario

    :returns:
    Devuelve la cantidad total de filas
    """

    return(len(matriz))


def recorrer_matriz_cxf(matriz:list[list])->None:
    """
    Recorre la matriz columna x fila

    :params: matriz(list[list]) = La matriz que ingrese el usuario

    :returns:
    None
    """

    cantidad_filas = len(matriz)

    cantidad_columnas = len(matriz[0])

    print(f"Nombres, Vistas, Duracion\n")

    for indice_columna in range(cantidad_columnas):
        mensaje = " "
        for indice_fila in range(cantidad_filas):
            mensaje = f"{mensaje}{matriz[indice_fila][indice_columna]}"
        
            if indice_fila < cantidad_filas -1:
                mensaje = f"{mensaje}, "

        print(mensaje)


def mapear_indice(seccion:str)->int:
    """
    Deriva una de las secciones (nombre, vistas, duracion) del video por un indice

    :params: seccion(str) = La seccion que ingresara el usuario 

    :returs:
    Devuelve el numero de indice
    """

    match seccion:
        case "nombre":
            return 0
        case "vistas":
            return 1
        case "duracion":
            return 2


def filtrar_matriz(matriz:list[list], indice:str, digito:str)->list[list]:
    """
    Filtra una matriz en base a un indice dado por el usuario

    :params: matriz(list[list]) = La matrizx que ingrese el usuario
    :params: indice(int) = Indice dentro de la matriz dada
    :params: digito(str) = El dato por el cual se filtrara la matriz

    :returns:
    Devuelve una matriz filtrada
    """

    matriz_filtrada = [
        [],
        [],
        []
    ]
    indice_a_filtrar = mapear_indice(indice)
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[indice_a_filtrar])

    for indice_columna in range(cantidad_columnas):
        if buscar_string(matriz[indice_a_filtrar][indice_columna], digito):
            for indice_fila in range(cantidad_filas):
                matriz_filtrada[indice_fila].append(matriz[indice_fila][indice_columna])
    return(matriz_filtrada)


def buscar_string(cadena_strings:list, char:str)->bool:
    """
    Verifica si un dato se enceuntra en la cadena de strings

    :params: cadena_string(list) = Una lista de caracteres ingresada por el usuario
    :params: char(str) = El dato el cual se buscara

    :returs:
    Devuelve si el datos a buscar se encuentra en la cadena de strings
    """

    fue_encontrado = False

    for digito in cadena_strings:
        fue_encontrado = digito == char

        if fue_encontrado == True:
            break
    return fue_encontrado


def buscar_elementos(matriz:list[list],indice:str, modo:str)->list[list]:
    """
    Busca por toda la matriz el numero mas alto de vistas

    :params: matriz(list[list]) = La matrizx que ingrese el usuario

    :returns:
    Devuelve una matriz filtrada
    """

    indice_a_filtrar = mapear_indice(seccion=indice)
    cantidad_columnas = len(matriz[indice_a_filtrar])
    lista_seleccionado = []
    seleccionado = matriz[indice_a_filtrar][0]

    for indice_columna in range(cantidad_columnas):
        valor_actual = matriz[indice_a_filtrar][indice_columna]
        if(modo == "ASC" and seleccionado < valor_actual or
            modo == "DES" and seleccionado > valor_actual):
            seleccionado = valor_actual
            lista_seleccionado = [valor_actual]
        elif seleccionado == valor_actual:
            lista_seleccionado.append(valor_actual)

    return lista_seleccionado


def filtrar_por_orden(matriz:list[list], indice:str, modo:str)->list[list]:
    """
    Filtra los videos mas vistos

    :params: matriz(list[list]) = La matrizx que ingrese el usuario
    :params: indice(int) = Indice dentro de la matriz dada
    :params: modo(str) - El orden en que se ejecutara


    :returns:
    Devuelve una matriz filtrada
    """

    matriz_filtrada = [
        [],
        [],
        []
    ]
    numero_seleccionados = buscar_elementos(matriz, indice, modo)
    indice_a_filtrar = mapear_indice(indice)
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[indice_a_filtrar])

    for indice_columna in range(cantidad_columnas):
        if matriz[indice_a_filtrar][indice_columna] in numero_seleccionados:
            for indice_fila in range(cantidad_filas):
                matriz_filtrada[indice_fila].append(matriz[indice_fila][indice_columna])
    recorrer_matriz_cxf(matriz_filtrada)


"Buscar y mostrar la info de los videos que no superen el promedio de vistas."

def promedio_de_elementos(matriz:list[list], fila:str)->float:
    """
    Calcula el promedio de la suma de los elementos de la lista fila

    :params: matriz(list[list]) = La matriz que ingrese le usuario
    :params: fila(str) = La fila matriz a la que se quiere promediar (nombre, vistas, duracion)

    :returns:
    Devuelve el promedio de toda la fila asignada
    """

    indice_promediar = mapear_indice(fila)
    cantidad_elementos = len(matriz[indice_promediar])
    lista_promediar = matriz[indice_promediar]
    sumatoria = 0

    for elemento in lista_promediar:
        sumatoria += elemento

    if sumatoria > 0:
        promedio = sumatoria / cantidad_elementos
    else:
        promedio = 0

    return(promedio)


def filtrar_por_promedio(matriz:list[list], fila:str, modo:str):
    """
    Filtra una matriz por un pormedio determinado

    :params: matriz(list[list]) = La matriz que ingrese le usuario
    :params: fila(str) = La fila matriz a la que se quiere promediar (nombre, vistas, duracion)
    :params: modo(str) = Segunda condicion para filtrar la matriz (mayores o menores del promedio)

    :returs:
    Devuelve la matriz filtrada por el promedio asignado
    """

    promedio = promedio_de_elementos(matriz, fila)
    indice_filtrar = mapear_indice(fila)
    
    matriz_filtrada = [
        [],
        [],
        []
    ]


    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[indice_filtrar])

    for indice_columna in range(cantidad_columnas):
        valor_actual = matriz[indice_filtrar][indice_columna]
        if ((modo == "mayor" and valor_actual > promedio) or
            (modo == "menor" and valor_actual < promedio)):
            for indice_fila in range(cantidad_filas):
                matriz_filtrada[indice_fila].append(matriz[indice_fila][indice_columna])


    mensaje = f"El promedio fue de {fila} es: {promedio} y estos son los videos que son {modo}"
    print(mensaje)
    return(matriz_filtrada)


def ordenar_matriz(matriz:list[list],tipo:str, modo:str)->list[list]:
    """
    Ordena la matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario
    :params: tipo(str) = La lista por la cual se ordenara la matriz
    :params: modo(str) = El orden de la matriz

    :returns:
    Devuelve la matriz ordenada
    """
    indice_ordenar = mapear_indice(tipo)

    for indice_columna in range(len(matriz[indice_ordenar])-1):
        indice_seleccionado = indice_columna

        for sig_indice_columna in range(indice_columna +1, len(matriz[indice_ordenar]), 1):
            if ( modo == "ASC" and matriz[indice_ordenar] [indice_seleccionado] > matriz [indice_ordenar] [sig_indice_columna] or\
                modo == "DES" and matriz[indice_ordenar] [indice_seleccionado] < matriz [indice_ordenar] [sig_indice_columna]):
                indice_seleccionado = sig_indice_columna

            if indice_seleccionado != indice_columna:
                auxiliar = matriz [indice_ordenar] [indice_seleccionado]
                matriz [indice_ordenar] [indice_seleccionado] = matriz[indice_ordenar][indice_columna] 
                matriz[indice_ordenar][indice_columna] = auxiliar

    return matriz

