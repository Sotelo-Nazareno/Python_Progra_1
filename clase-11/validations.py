
def validar_rango(numero_a:int, numero_b:int)->int:
    """
    Valida el valor que ingresa el usuario

    Args:
        numero_a (int): Numero desde donde comienza el rango
        numero_b (int): Numero desde donde termina el rango

    Returns:
        int: Devuelve el numero valido del usuario
    """

    numero_str = input(f"Ingrese un valor [{numero_a} - {numero_b}]: ")
    numero_int = int(numero_str)

    if not(numero_a <= numero_int <= numero_b):
        print("El valor ingresado esta fuera de rango. Intentelo de nuevo")
        return validar_rango(numero_a, numero_b)
    
    return numero_int