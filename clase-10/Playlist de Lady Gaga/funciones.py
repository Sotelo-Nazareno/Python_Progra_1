import playlist_lady_gaga as lg
import datetime as dt

#🔹 1. Normalización de Datos
#El formato original de los datos no está estandarizado, por lo que se deben normalizar utilizando funciones preexistentes. 
# Cada video deberá contener la siguiente información correctamente estructurada:

#Título (str): Nombre del tema.
#Colaboradores (list): Lista de artistas invitados (si los hay).
#Vistas (int): Cantidad de reproducciones en números enteros.
#Duración (int): Duración del video en segundos.
#Link (str): Enlace directo al video en YouTube.
#Fecha de lanzamiento (date): Fecha de publicación del video.


def normalizar_vistas(video:dict):
    """
    Normaliza las vistas de los videos

    Args:
        diccionario (dict): El diccionario que ingrese el usuario
    """

    datos_vistas = (video["Vistas"]).split(" ")
    cantidad = int(datos_vistas[0])

    vistas_normalizadas = cantidad * 1000000
    video["Vistas"] = vistas_normalizadas


def normalizar_duracion(video:dict):
    """
    Normaliza la duracion de los videos en segundos

    Args:
        diccionario (dict): El diccionario que ingrese el usuario
    """

    datos_duracion = (video["Duracion"]).split(":")
    duracion_segs = int(datos_duracion[0]) * 60 + int(datos_duracion[1])

    video["Duracion"] = duracion_segs


def normalizar_titulos(video:dict):
    """
    Normaliza el titulo de la cancion y agrega colaborador si es que lo hay

    Args:
        diccionario (dict): El diccionario que ingrese el usuario
    """

    dato_titulo = (video["Tema"]).split(" - ")
    video["Titulo"] = video.pop("Tema")
    if len(dato_titulo) > 1:
        video["Titulo"] = dato_titulo[1]
        colaboradores = dato_titulo[0].split("|")
        video["Colaboradores"] = colaboradores
    else:
        video["Titulo"] = dato_titulo[0]


def normalizar_fecha(video:dict):
    """
    Normaliza la fecha de la cancion

    Args:
        diccionario (dict): El diccionario que ingrese el usuario
    """

    fecha = dt.datetime.strptime(video.get('Fecha lanzamiento'), '%Y-%m-%d')
    fecha = fecha.date()
    video["Fecha lanzameinto"] = fecha


def normalizar_datos(lista_dict:list[dict])->list[dict]:
    """
    Normaliza los datos de la lista de diccionarios ingresada

    Args:
        lista_dict (list[dict]): La lista de diccionarios ingresada por el usuario

    Returns:
        list[dict]: Devuelve una lista normalizada
    """
    
    copia_list = lista_dict.copy()

    for cancion in copia_list:
        normalizar_titulos(cancion)
        normalizar_vistas(cancion)
        normalizar_duracion(cancion)
        normalizar_fecha(cancion)

    return copia_list



#-------------------------------------------------------------------------------------------------------------------------------------

#4. Promedio de Vistas
#Se calculará y mostrará el promedio de vistas de todos los videos en millones.

def promedio_total(videos:list[dict], categoria:str)->int:
    """
    Clcula el promedio de una categoria de los videos

    Args:
        videos (list[dict]): La lista de videos
        categoria (str): La categoria de los videos

    Returns:
        int: Devuelve el promedio 
    """

    sumatoria = 0 
    cantidad = len(videos)

    for video in videos:
        sumatoria += video.get(categoria)

    promedio = sumatoria / cantidad

    return promedio

def mostrar_promedio(videos:list[dict], categoria:str):
    """
    Clcula el promedio de una categoria de los videos

    Args:
        videos (list[dict]): La lista de videos
        categoria (str): La categoria de los videos
    """

    promedio_calculado = promedio_total(videos, categoria)
    promedio_redondeado = round(promedio_calculado / 100000, 2)
    mensaje = f"El promedio de {categoria} es de {promedio_redondeado} millones"
    print(mensaje)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Máxima Reproducción
# Se listará el video (o los videos) con la mayor cantidad de vistas.
#  6. Mínima Reproducción
# Se listará el video (o los videos) con la menor cantidad de vistas.


def buscar_max_min(videos:list[dict], key:str, orden:str)->list[any]:
    """
    Busca el valor min o max de una categora de los videos

    Args:
        videos (list[dict]): La lista de videos
        categoria (str): La categoria del video
        orden (str): El orden que se buscara (min - max)
    """

    lista_seleccionados = []
    seleccionado = None

    for video in videos:
        if orden == "max" and(seleccionado == None or video.get(key) > seleccionado.get(key))or\
            orden == "min" and(seleccionado == None or video.get(key) < seleccionado.get(key)):
            seleccionado = video
            lista_seleccionados = [video]
        elif video.get(key) == seleccionado.get(key):
            lista_seleccionados.append(video)

    
    return lista_seleccionados


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Búsqueda por Código 
# El usuario ingresará un código de video y el programa mostrará todos los detalles asociados a ese video.

