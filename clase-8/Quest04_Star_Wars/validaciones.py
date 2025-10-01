

def verificar_matriz_vacia(matriz:list[list])->bool:
    """
    Verifica si la matriz dada esta vacia

    :params: matriz(list[list]) = La matriz dada por el usuario

    :returns:
    Devuelve un valor booleano
    """

    return len(matriz) > 0


def validar_rango(numero_a:int, numero_b:int)->int:
    """
    Valida el valor que ingresa el usuario

    :params: numero_a = Numero desde donde comienza el rango
    :params: numero_b = Numero desde donde termina el rango

    :retruns:
    Devuelve el numero valido del usuario
    """

    numero_str = input(f"Ingrese un valor [{numero_a} - {numero_b}]: ")
    numero_int = int(numero_str)

    if not(numero_a <= numero_int <= numero_b):
        print("El valor ingresado esta fuera de rango. Intentelo de nuevo")
        return validar_rango(numero_a, numero_b)
    
    return numero_int
