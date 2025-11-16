
def mostrar_opciones()->None:
    """
    Muestra por consola las opciones
    """
    opciones =\
        f"""
        [1] Normalización de Datos
        [2] Mostrar Lista de Temas
        [3] Ordenar Temas
        [4] Promedio de Vistas
        [5] Máxima Reproducción
        [6] Mínima Reproducción
        [7] Búsqueda por Código
        [8] Listar por Colaborador
        [9] Listar por Mes de Lanzamiento
        [10] Salir
        """ 
    
    print(opciones)



# ------------------------------------------------------------------------

# 2. Mostrar Lista de Temas
# Se presentará la lista de todos los temas en formato tabular. 
# No es necesario mostrar todos los datos, solo los esenciales (por ejemplo, título y duración)

def mostrar_duracion(diccionario: list[dict]):
    """
    Muestra por consola el titulo y duracion del video

    Args:
        diccionario (list[dict]): La lista de videos
    """
    mensaje =f"                  Titulo                       |  Duracion \n"
    mensaje +=f"--------------------------------------------------------------\n"
    
    for cancion in diccionario:
        dato = ""
        dato += f" {cancion["Titulo"]:45} | "
        dato += f" {cancion["Duracion"]:5}  "
        mensaje += f"{dato} \n"
    print(mensaje)



def mostrar_informacion(videos: list[dict]):
    """
    Imprime por consola la informacion de los videos

    Args:
        videos (list[dict]): La lista de videos
    """

    mensaje =f"                  Titulo                       |  Vistas   |  Duracion  \n"
    mensaje +=f"------------------------------------------------------------------------\n"
    
    for cancion in videos:
        dato = ""
        dato += f" {cancion["Titulo"]:45} | "
        dato += f" {cancion["Vistas"]:5} | "
        dato += f" {cancion["Duracion"]:5}  "
        mensaje += f"{dato} \n"
    print(mensaje)