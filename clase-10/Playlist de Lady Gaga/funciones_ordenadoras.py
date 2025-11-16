


#🔹 3. Ordenar Temas
#Los videos se ordenarán por duración, de mayor a menor.



def ordenar_quick_temas(videos:list[dict], valor_ordenar:str, modo:str):
    """
    Ordena los temas 

    Args:
        videos (list[dict]): La lista diccionarios que ingres ele usuario
        valor_ordenar (str): L acategoria por la cual se ordenanara
        modo (str): El orden en el que se ordenanara (ASC - DES)
    """

    if len(videos) < 2:
        return videos
    

    pivot = videos.pop()

    mas_grandes = []
    mas_chicos = []

    for video in videos:
        if video.get(valor_ordenar) > pivot.get(valor_ordenar):
            mas_grandes.append(video)
        else:
            mas_chicos.append(video)

    if modo == "ASC":
        return ordenar_quick_temas(mas_chicos, valor_ordenar, modo) + [pivot] + ordenar_quick_temas(mas_grandes, valor_ordenar, modo)
    else:
        return ordenar_quick_temas(mas_grandes, valor_ordenar, modo) + [pivot] + ordenar_quick_temas(mas_chicos, valor_ordenar, modo)

