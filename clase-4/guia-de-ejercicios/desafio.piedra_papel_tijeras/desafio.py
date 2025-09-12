import random
import os

def verificar_ganador_ronda(jugador, maquina)->str:
    """
    Determina quién ganó la ronda según las elecciones del jugador y la máquina.

    :params: jugador (int)= Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera).
    :params: maquina (int)= Elección de la máquina (1 para Piedra, 2 para Papel, 3 para Tijera).

    :returns:
    Devuelve el ganador de la ronda, en caso que no haya habra empate
    """

    if jugador == maquina:
        return("Empate")
    elif ((jugador == 3 and maquina == 2) or
        (jugador == 2 and maquina == 1) or
        (jugador == 1 and maquina == 3)):
        return("Jugador")
    else:
        return("Maquina")


def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual)->bool:
    """
    Determina si la partida sigue en curso o ya ha finalizado.

    :params: aciertos_jugador (int) = Cantidad de rondas ganadas por el jugador.
    :params: aciertos_maquina (int) = Cantidad de rondas ganadas por la máquina.
    :params: ronda_actual (int) = Número de la ronda actual.

    :returns:
    Devuelve si la partida sigue en curso
    """
    en_cuerso = True
    if(ronda_actual == 2 and 
    (aciertos_jugador == 2 or
    aciertos_maquina == 2)):
        en_cuerso = False

    return(en_cuerso)


def elegir_jugada_usuario()->int:
    """
    Selecciona la jugada del usuario

    :returns:
    Devuelve la jugada del usuario (1 pierda, 2 papel, 3 tijeras)
    """
    jugada_int = 0
    while(jugada_int != 1 and
        jugada_int != 2 and
        jugada_int != 3):
        jugada_usuario_str = input("Ingrese su jugada [1 Piedra - 2 Papel - 3 Tijera]: ")
        jugada_int = int(jugada_usuario_str)
    return(jugada_int)


def verificar_ganador_partida(aciertos_jugador, aciertos_maquina)->str:
    """
    Determina quién ganó la partida comparando los aciertos finales.

    :params: aciertos_jugador (int) = Cantidad de rondas ganadas por el jugador.
    :params: aciertos_maquina (int) = Cantidad de rondas ganadas por la máquina.

    :returns:
    Devuelve al que tiene mas puntos
    """
    if aciertos_jugador > aciertos_maquina:
        return("Jugador")
    else:
        return("Maquina")

def mostrar_elemento(eleccion)->str:
    """
    Convierte la elección numérica en un texto legible.

    :params: eleccion (int) = Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera).

    :returns:
    Devuelve la eleccion de juego
    """
    if eleccion == 1:
        eleccion_str = "Piedra"
    elif eleccion == 2:
        eleccion_str = "Papel"
    else:
        eleccion_str = "Tijera"
    return(eleccion_str)


def jugar_piedra_papel_tijera()->str:
    """
    Gestiona toda la lógica del juego piedra, papel y tijera

    :returns:
    Devuelve quién ganó la partida ("Jugador" o "Máquina")
    """
    puntos_jugador = 0
    puntos_maquina = 0
    ronda_numero = 0

    while verificar_estado_partida(puntos_jugador, puntos_maquina, ronda_numero):

        jugada_usuario = elegir_jugada_usuario()
        jugada_maquina = random.choice([1, 2, 3])

        if verificar_ganador_ronda(jugada_usuario, jugada_maquina) == "Jugador":
            print(f"Su jugada: {mostrar_elemento(jugada_usuario)} / Jugada maquina {mostrar_elemento(jugada_maquina)}")
            puntos_jugador += 1
        elif verificar_ganador_ronda(jugada_usuario, jugada_maquina) == "Maquina":
            print(f"Su jugada: {mostrar_elemento(jugada_usuario)} / Jugada maquina {mostrar_elemento(jugada_maquina)}")
            puntos_maquina += 1
        else:
            print(f"Su jugada: {mostrar_elemento(jugada_usuario)} / Jugada maquina {mostrar_elemento(jugada_maquina)}")
        ronda_numero += 1
        print(f"""El ganador de esta ronda es: {verificar_ganador_ronda(jugada_usuario, jugada_maquina)}
        Ronda Nº{ronda_numero}""")


    if verificar_ganador_partida(puntos_jugador,puntos_maquina) == "Jugador":
        mensaje = "Felicidades, ganaste la partida!"
    else:
        mensaje = "Perdiste, vuelvelo a intentar"
    return(mensaje)