
def elegir_opcion()->None:
    """
    Eligue la opcion que el usuario ingresa

    :returns:
    Devuelve la opcion que el usuario eligio
    """

    opcion_str = input("Eliga una opcion de nuestro menu: ")
    
    # validacion recursiva

    match opcion_str:
        case "1":
            