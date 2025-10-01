import funciones as fn

def validar_rango(numero_a:int, numero_b:int)->int:
    """
    Valida el valor que ingresa le usuario

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



def validar_matriz_con_elementos(matriz: list[list])->bool:
    """
    Valida si la matriz no esta vacia
    """

    corriendo = True

    if len(matriz) == 0 :
        print("ERROR -Debe crear primero la matriz con la opcion 1 para acceder a esta funcion")
        return False
    
    return corriendo

