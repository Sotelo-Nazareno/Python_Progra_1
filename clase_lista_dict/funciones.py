
def es_genero(heroe: dict, genero: str) -> bool:
    return heroe.get('genero') == genero

def mostrar_datos_heroe(heroe: dict) -> None:
    message =\
    f"""{heroe.get("nombre")[:15]:15} | {heroe.get("identidad")[:15]:15} | {heroe.get("alias")[:15]:15} | {heroe.get("genero")[:15]:15}"""
    print(message)

def mostrar_datos_heroes(heroes: list[dict]) -> None:
    header = f'Nombre          | Identidad       | Alias          | Género'
    print(header)
    for heroe in heroes:
        mostrar_datos_heroe(heroe)

def filtrar_heroes_por_genero(heroes: list[dict], genero: str):
    heroes_filtrados = []
    for heroe in heroes:
        if es_genero(heroe, genero):
            heroes_filtrados.append(heroe)
    return heroes_filtrados

def stark_imprimir_heroe_genero(heroes: list[dict], genero: str) -> None:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, genero)
    mostrar_datos_heroes(heroes_filtrados)

def calcular_min(heroes: list[dict], key: str) -> dict:
    minimo = None
    for heroe in heroes:
        if minimo == None or heroe.get(key) < minimo.get(key):
            minimo = heroe
    return minimo

def calcular_max(heroes: list[dict], key: str) -> dict:
    maximo = None
    for heroe in heroes:
        if maximo == None or heroe.get(key) > maximo.get(key):
            maximo = heroe
    return maximo

def calcular_min_genero(heroes: list[dict], key: str, valor_genero: str) -> dict:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    heroe_minimo = calcular_min(heroes_filtrados, key)
    return heroe_minimo

def calcular_max_genero(heroes: list[dict], key: str, valor_genero: str) -> dict:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    heroe_maximo = calcular_max(heroes_filtrados, key)
    return heroe_maximo

def calcular_max_min_dato_genero(heroes: list[dict], calculo: str, key: str, valor_genero: str) -> dict:
    heroe_seleccionado = {}

    if calculo == 'maximo':
        heroe_seleccionado = calcular_max_genero(heroes, key, valor_genero)
    else:
        heroe_seleccionado = calcular_min_genero(heroes, key, valor_genero)
    return heroe_seleccionado

def stark_calcular_imprimir_heroe_genero(heroes: list[dict], calculo: str, key: str, valor_genero: str):
    if len(heroes) > 0:
        heroe_seleccionado = calcular_max_min_dato_genero(heroes, calculo, key, valor_genero)
        mostrar_datos_heroes([heroe_seleccionado])

def sumar_valor_clave(heroes: list[dict], key: str) -> float:
    suma = 0
    for heroe in heroes:
        suma += heroe.get(key, 0)
    return suma

def sumar_dato_heroe_genero(heroes: list[dict], key: str, valor_genero: str) -> float:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    suma = sumar_valor_clave(heroes_filtrados, key)
    return suma

def cantidad_heroes_genero(heroes: list[dict], valor_genero: str) -> int:
    heroes_filtrados = filtrar_heroes_por_genero(heroes, valor_genero)
    return len(heroes_filtrados)

def calcular_promedio_genero(heroes: list[dict], key: str, valor_genero: str) -> float:
    suma = sumar_dato_heroe_genero(heroes, key, valor_genero)
    cantidad = cantidad_heroes_genero(heroes, valor_genero)

    if cantidad != 0:
        promedio = suma / cantidad
    else:
        promedio = 0
    return promedio

def stark_calcular_imprimir_promedio_altura_genero(heroes: list[dict], key: str, valor_genero: str) -> None:
    if len(heroes) == 0:
        print('ERROR: La lista esta vacía')
    else:
        promedio = calcular_promedio_genero(heroes, key, valor_genero)
        print(f'El promedio de {key.capitalize()} de genero {valor_genero} es: {promedio:.2f}')


def cantidad_tipo(heroes: list[dict], key: str) ->dict:

    dict_colores = dict()

    for heroe in heroes:
        if heroe.get(key) not in dict_colores.keys():
            dict_colores[heroe.get(key)] =  1
        else:
            dict_colores[heroe.get(key)] +=  1

    return dict_colores


def calcular_cantidad_tipo(heroes: list[dict], key: str) ->dict:

    if len == 0:
        print("La lista no debe estar vacia")
    else:
        cantidad_tipo(heroes, key)