

def crear_matriz(lista_a:list, lista_b:list, lista_c:list, lista_d:list)->list[list]:
    """
    Crea una matriz

    :params: lista_a(list) = La lista que ingrese el usuario
    :params: lista_b(list) = La lista que ingrese el usuario
    :params: lista_c(list) = La lista que ingrese el usuario
    :params: lista_d(list) = La lista que ingrese el usuario

    :returns:
    Devuelve una matriz con las listas asignadas
    """

    mi_matriz = [
        lista_a,
        lista_b,
        lista_c,
        lista_d
    ]

    return mi_matriz

def agregar_video(matriz:list[list]):
    """
    Agrega un video a la matriz ingresada

    :params: matriz(lis[list]) = La matriz ingresada por el usuario
    :params: titulo(str) = El titulo del video
    :params: duracion(int) = La duracion del video
    :params: views(int) = La vistas del video
    :params: like(int) = Los likes del video

    :returns:
    Devuelve la matriz con el video agregado
    """

    cantidad_filas = len(matriz)

    for indice_fila in range(cantidad_filas):
        match indice_fila:
            case 0:
                titulo = input("Ingrese el titulo del video: ")
                matriz[indice_fila].append(titulo.title())
            case 1:
                duracion = input("Ingrese la duracion del video: ")
                matriz[indice_fila].append(duracion)
            case 2:
                views = input("Ingrese las vistas del video: ")
                matriz[indice_fila].append(views)
            case 3:
                like = input("Ingrese los likes del video: ")
                matriz[indice_fila].append(like)


def cantidad_elementos(matriz:list[list])->int:
    """
    Cuenta la cantidad de elementos de una matriz

    :params: matriz(list[list]) = La matriz que ingrese el usuario

    :returns:
    Devuelve la cantidad total de elementos de la matriz
    """

    return(len(matriz[0]))


def mapear_indice(seccion:str)->int:
    """
    Deriva una de las secciones (nombre, vistas, duracion) del video por un indice

    :params: seccion(str) = La seccion que ingresara el usuario 

    :returs:
    Devuelve el numero de indice
    """

    match seccion:
        case "titulo":
            return 0
        case "duracion":
            return 1
        case "vistas":
            return 2
        case "likes":
            return 3

def obtener_datos_filtrados(matriz:list[list], matriz_filtrada:list[list], indice_col:int):
    """
    Obtiene los datos filtrados de una matriz

    :params:  matriz(list[list]) = La matriz que ingrese el usuario

    """
    for indice_fila in range(len(matriz)):
        dato = matriz[indice_fila][indice_col]
        matriz_filtrada[indice_fila].append(dato)
    return matriz_filtrada


def filtrar_titulo(matriz:list[list],tipo:str, frase:str):
    """
    Filtra los titulos de los videos

    :params:  matriz(list[list]) = La matriz que ingrese el usuario
    :params: tipo(str) = El

    :returns:
    Devuelve la matriz filtrada
    """

    matriz_filtrada = [
        [],
        [],
        [],
        []
    ]

    indice_a_filtrar = mapear_indice(tipo)
    cantidad_columnas = len(matriz[indice_a_filtrar])

    for indice_columna in range(cantidad_columnas):
        titulo_actual = matriz[indice_a_filtrar][indice_columna]
        if frase in titulo_actual:
            obtener_datos_filtrados(matriz, matriz_filtrada, indice_columna)
    return matriz_filtrada


def cantidad_videos_por_titulo(matriz:list[list],tipo:str, frase:str):
    """
    """

    cantidad_videos = cantidad_elementos(filtrar_titulo(matriz, tipo, frase))

    mensaje = f"Existen {cantidad_videos} con {frase} en su {tipo}"
    print(mensaje)


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


def buscar_elementos(matriz:list[list],tipo:str, modo:str)->list[list]:
    """
    Busca por toda la matriz el numero mas alto de vistas

    :params: matriz(list[list]) = La matriz que ingrese el usuario

    :returns:
    Devuelve una matriz filtrada
    """

    indice_a_filtrar = mapear_indice(tipo)
    cantidad_columnas = len(matriz[indice_a_filtrar])
    lista_seleccionado = []
    seleccionado = matriz[indice_a_filtrar][0]

    for indice_columna in range(cantidad_columnas):
        valor_actual = matriz[indice_a_filtrar][indice_columna]
        if(modo == "mas" and seleccionado < valor_actual or
            modo == "menos" and seleccionado > valor_actual):
            seleccionado = valor_actual
            lista_seleccionado = [valor_actual]
        elif seleccionado == valor_actual:
            lista_seleccionado.append(valor_actual)

    return lista_seleccionado

def filtrar_por_orden(matriz:list[list], tipo:str, modo:str)->list[list]:
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
    numero_seleccionados = buscar_elementos(matriz, tipo, modo)
    indice_a_filtrar = mapear_indice(tipo)
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[indice_a_filtrar])

    for indice_columna in range(cantidad_columnas):
        if matriz[indice_a_filtrar][indice_columna] in numero_seleccionados:
            for indice_fila in range(cantidad_filas):
                valor_actual = matriz[indice_fila][indice_columna]
                matriz_filtrada[indice_a_filtrar].append(valor_actual)
    recorrer_matriz_cxf(matriz_filtrada)
