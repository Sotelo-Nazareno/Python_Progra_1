

def es_genero(heroe:dict, genero:str)->bool:
    """
    Evalua si el heroe dado tiene el genero ingresado

    Args:
        heroe (dict): El heroe de la lista
        genero (str): Un genero ('M'.'F' o 'N-B')

    Returns:
        bool: Devuelve el valor booleano del genero en el heroe
    """

    return(heroe.get('genero') == genero)

def filtrar_heroes(lista_heroes:list[dict], genero:str)->list[dict]:
    """
    Filtra la lista de heroes solo con el mismo genero ingresado

    Args:
        lista_heroes (list[dict]): La lista de heroes
        genero (str): El genero ('M', 'F' o 'N-B')

    Returns:
        list: Devuelve una lista filtrada
    """

    lista_filtrada = []
    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            lista_filtrada.append(heroe)
    return lista_filtrada

def mostrar_heroes(lista_heroes:list[dict])->None:
    """
    Imprime por consola los heroes de la lista

    Args:
        lista_heroes (list): La lista de heroes
    """
    mensaje = f"    Nombre       |   Genero   \n"
    mensaje += f"------------------------------\n"
    for heroe in lista_heroes:
        mensaje += f" {heroe.get('nombre')[:15]:15} | {heroe.get('genero')}\n"
    print(mensaje)

def stark_imprimir_heroe_genero(lista_heroes:list[dict], genero:str)->None:
    """
    Imprime por consola los nombres de los heroes con el genero ingresado

    Args:
        lista_heroes (list[dict]): La lista de heroes
        genero (str): El genero ('M', 'F' o 'N-B')
    """

    heroes_genero = filtrar_heroes(lista_heroes, genero)
    mostrar_heroes(heroes_genero)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def calcular_min_genero(lista_heroes:list[dict], dato:str, genero:str)->dict:
    """
    Calcula el/los heroe que cumpla con las condiciones minimas dadas

    Args:
        lista_heroes (list[dict]): La lista de heroes
        dato (str): El dato del heroe (altura, peso, ..)
        genero (str): El genero ('M', 'F' o 'N-B')
    Returns:
        dict: Devuelve el heroes que cumplan las condiciones minimas
    """

    heroes_seleccionados = filtrar_heroes(lista_heroes, genero)
    minimo = None
    for heroe in heroes_seleccionados:
        if minimo == None or heroe.get(dato) < minimo.get(dato):
            minimo = heroe
    return minimo


def calcular_max_genero(lista_heroes:list[dict], dato:str, genero:str)->dict:
    """
    Calcula el/los heroe que cumpla con las condiciones maximas dadas

    Args:
        lista_heroes (list[dict]): La lista de heroes
        dato (str): El dato del heroe (altura, peso, ..)
        genero (str): El genero ('M', 'F' o 'N-B')
    Returns:
        dict: Devuelve el heroes que cumplan las condiciones maximas
    """

    heroes_seleccionados = filtrar_heroes(lista_heroes, genero)
    maximo = None
    for heroe in heroes_seleccionados:
        if maximo == None or heroe.get(dato) > maximo.get(dato):
            maximo = heroe
    return maximo


def calcular_max_min_dato_genero(lista_heroes:list[dict], calculo:str, dato:str, genero:str)->dict:
    """
    Calcula el/los heroe que cumpla con las condiciones maximas dadas

    Args:
        lista_heroes (list[dict]): La lista de heroes
        calculo (str): El calculo por el cual se buscara el valor (minimo, maximo)
        dato (str): El dato del heroe (altura, peso, ..)
        genero (str): El genero ('M', 'F' o 'N-B')
    Returns:
        dict: Devuelve el heroes que cumplan las condiciones maximas
    """

    heroe_seleccionado = dict()
    if calculo == 'maximo':
        heroe_seleccionado = calcular_max_genero(lista_heroes, dato, genero)
    else:
        heroe_seleccionado = calcular_min_genero(lista_heroes, dato, genero)

    return heroe_seleccionado

def mostrar_info_heroes(heroe: dict)->None:
    """
    Imprime por consola un heroe con su informacion

    Args:
        heroe (dict): El heroe seleccionado
    """
    mensaje = f"    Nombre       |   Genero  |  Altura\n"
    mensaje += f"------------------------------------------\n"
    mensaje += f" {heroe.get('nombre')[:15]:15} | {heroe.get('genero'):3} | {heroe.get('altura_mts')}\n"
    print(mensaje)


def stark_calcular_imprimir_heroe_genero(lista_heroes: list[dict], calculo:str, dato:str, genero:str)->None:
    """
    Imprime por consola el heroe que cumpla las condiciones dadas

    Args:
        lista_heroes (list[dict]): La lista de heroes
        calculo (str): El calculo por el cual se buscara el valor (minimo, maximo)
        dato (str): El dato del heroe (altura, peso, ..)
        genero (str): El genero ('M', 'F' o 'N-B')
    """

    if len(lista_heroes) < 1:
        print(-1)
    else:
        mostrar_info_heroes(calcular_max_min_dato_genero(lista_heroes, calculo, dato, genero))


#--------------------------------------------------------------------------------------------------------------

def sumar_dato_heroe_genero(lista_heroes: list[dict], dato:str, genero:str)-> int:
    """
    Suma los datos de los heroes seleccioandos

    Args:
        lista_heroes (list[dict]): La lista de heroes
        dato (str): El dato del heroe (altura, peso, ..)
        genero (str): El genero ('M', 'F' o 'N-B')

    Returns:
        int: Devuelve la suma total
    """

    heroes_seleccionados = filtrar_heroes(lista_heroes, genero)
    sumatoria = 0

    if len(heroes_seleccionados) > 0:
        for heroe in heroes_seleccionados:
            sumatoria += heroe.get(dato, 0)

    return sumatoria


def cantidad_heroes_genero(lista_heroes: list[dict], genero:str)-> int:
    """
    Calcula la cantidad de heroes con el mismo genero seleccioando

    Args:
        lista_heroes (list[dict]): La lista de heroes
        genero (str): El genero ('M', 'F' o 'N-B')

    Returns:
        int: Devuelve la cantidad de heroes con el mismo genero
    """

    heroes_seleccionados = filtrar_heroes(lista_heroes, genero)
    return(len(heroes_seleccionados))


def calcular_promedio_genero(lista_heroes: list[dict], dato:str, genero:str)-> float:
    """
    Calcula el promedio de la lista de heroes por el genero y el dato sleeccionados

    Args:
        lista_heroes (list[dict]): La lista de heroes
        dato (str): El dato del heroe (altura, peso, ..)
        genero (str): El genero ('M', 'F' o 'N-B')

    Returns:
        float: Devuelve el promedio
    """

    promedio = sumar_dato_heroe_genero(lista_heroes, dato, genero) / cantidad_heroes_genero(lista_heroes, genero)

    if promedio == 0:
        promedio = 0
    else:
        promedio

    return promedio


def stark_calcular_imprimir_promedio_altura_genero(lista_heroes: list[dict], dato:str, genero:str)-> None:
    """
    Imprime por consola el promedio la la lista de heroes por el genero y dato seleccioando

    Args:
        lista_heroes (list[dict]): La lista de heroes
        dato (str): El dato del heroe (altura, peso, ..)
        genero (str): El genero ('M', 'F' o 'N-B')
    """
    promedio = calcular_promedio_genero(lista_heroes, dato, genero)
    print(f"El promedio de los heroes {genero} por su {dato} es: {promedio:.2f}")



def stark_nombres_asociados(lista_heroes:list[dict]):
    """
    Imprime por consola los heroes asociados

    Args:
        lista_heroes (list[dict]): Lista de heroes
    """


    stark_calcular_imprimir_heroe_genero(lista_heroes, 'maximo', 'altura_mts', 'Masculino')
    stark_calcular_imprimir_heroe_genero(lista_heroes, 'maximo', 'altura_mts', 'Femenino')
    stark_calcular_imprimir_heroe_genero(lista_heroes, 'minimo', 'altura_mts', 'Masculino')
    stark_calcular_imprimir_heroe_genero(lista_heroes, 'minimo', 'altura_mts', 'Femenino')
    stark_calcular_imprimir_promedio_altura_genero(lista_heroes, 'altura_mts', 'Masculino')
    stark_calcular_imprimir_promedio_altura_genero(lista_heroes, 'altura_mts', 'Femenino')




#-------------------------------------------------------------------------------------------------------------------------------------------------------

def calcular_cantidad_tipo(lista_heroes: list[dict], key:str)->dict:
    """
    Calcula la cantidad de un tipo dado en la lista

    Args:
        lista_heroes (list[dict]): La lista de heroes
        key (str): Un dato en la lista de heroes
    """

    diccionario = dict()

    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if heroe.get(key) not in diccionario:
                diccionario[heroe.get(key)] = 1
            else:
                diccionario[heroe.get(key)] += 1

    return diccionario


def imprimir_cantidad_heroes_tipo(heroe: dict, valor: str)->None:
    """
    Imprime la cantidad de heroes que tiene el valor asociado

    Args:
        heroe (dict): El heroe la lista
        valor (str): El valor de una clave
    """
    if valor == "-":
        print(f"Característica: color_ojos Desconocido - Cantidad de héroes: {heroe.get(valor)}")
    else:
        print(f"Característica: color_ojos {valor} - Cantidad de héroes: {heroe.get(valor)}")


def stark_calcular_cantidad_por_tipo(lista_heroes: list[dict], key:str)->None:
    """
    Calcula la cantidad de heroes con el tipo seleccioando

    Args:
        lista_heroes (list[dict]): La lista de heroes
        key (str): Un dato en la lista de heroes
    """

    tipos =  calcular_cantidad_tipo(lista_heroes, key)
    for clave in tipos.keys():
        imprimir_cantidad_heroes_tipo(tipos, clave)



#--------------------------------------------------------------------------------------------------------------------------------------------


def obtener_lista_de_tipos(lista_heroes: list[dict], key:str)->list:
    """
    Obtiene una lista de tipos de la key de la lista de heroes sin repetidos

    Args:
        lista_heroes (list[dict]): La lista de heroes
        key (str): Un dato de la lista de heroes

    Returns:
        list: Devuelve una lista sin repetidos
    """

    tipos_sin_repetir = set()
    tipos =  calcular_cantidad_tipo(lista_heroes, key)

    for clave in tipos.keys():
        if clave in ('-', '', None):
            tipos_sin_repetir.add('N/A')
        else:
            tipos_sin_repetir.add(clave)

    lista = list(tipos_sin_repetir)
    return lista


def normalizar_dato(valor:str, valor_defecto:str)-> str:
    """
    Normaliza el dato

    Args:
        valor (str): El valor de un dato de un heroe
        valor_defecto (str): El valor a reemplazar si el parametro anterior es vacio

    Returns:
        str: Devuelve el valor de un heroe 
    """
    if valor in ('-', '', None):
        return valor_defecto
    else:
        return valor
    

def obtener_heroes_por_tipo(lista_heroes:list[dict], lista_var: list, key: str)->dict:
    """
    Obtiene los heroes por tipo de la key seleccionada

    Args:
        lista_heroes (list[dict]): La lista de heroes
        lista_var (list): La lista de variedades
        key (str): El tipo de dato de un heroe

    Returns:
        dict: Devuelve un diccionario de heroes por tipo
    """

    
    diccionario_tipo = dict()

    for tipo in lista_var:

        diccionario_tipo[tipo] = []

        for heroe in lista_heroes:
            tipo_heroe = normalizar_dato(heroe.get(key), "N/A")

            if tipo_heroe in diccionario_tipo.keys():
                if heroe.get('nombre') not in diccionario_tipo[tipo_heroe]:
                    diccionario_tipo[tipo_heroe].append(heroe.get('nombre'))
    
    return diccionario_tipo


def imprimir_heroes_por_tipo(diccionario: dict, key:str)->None:
    """
    Imprime por consola los heroes por su tipo de key

    Args:
        diccionario (dict): El diccinario de tipos con nombres
        key (str): El dato de los heroes
    """

    for clave, valor in diccionario.items():
        nombres = " | ".join(valor)
        print(f"{key} {clave}: {nombres}")


def stark_listar_heroes_por_dato(lista_heroes: list[dict], key:str)->None:
    """
    Imprime por consola cada tipo con sus heroes 

    Args:
        lista_heroes (list[dict]): La lista de heroes
        key (str): El tipo de dato de un heroe
    """

    lista_tipos = obtener_lista_de_tipos(lista_heroes, key)
    heroes_por_tipo = obtener_heroes_por_tipo(lista_heroes, lista_tipos, key)
    imprimir_heroes_por_tipo(heroes_por_tipo, key)