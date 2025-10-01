import funciones as fn
import validaciones as vl

def aplicacion(lista_a:list, lista_b:list, lista_c:list, lista_d:list)->None:
    """
    Imprime una aplicacion de Stars Wars

    :params: lista_a(list) = La lista que ingrese el usuario
    :params: lista_b(list) = La lista que ingrese el usuario
    :params: lista_c(list) = La lista que ingrese el usuario
    :params: lista_d(list) = La lista que ingrese el usuario

    :retuns:
    None
    """

    corriendo = True

    mensaje = f"""
            [1] Crear una matriz
            [2] Mostrar existencias
            [3] Mostrar Datos
            [4] Mostrar la informacion de los personajes de género “n/a” que no superen el promedio de altura.
            [5] Mostrar todos los personajes de género “male” que superen el promedio de peso y mostrarlos.
            [6] Mostrar todos los personajes de género “female” que no superen el promedio de altura y mostrarlos
            [7] Ordenar la matriz según altura DES los personajes que sean “female”
            [8] Ordenar la matriz según peso ASC los personajes que sean “male”
            [9] Ordenar la matriz según altura ASC los personajes que sean “n/a”
            [10] Trasponer la matriz y mostrar su información prolija con una función que acepte ese tipo de matriz, además debe estar ordenada por altura DES.
            [11] Salir
                """

    nave_matriz = []
    while corriendo:

        print(mensaje)
        opcion = vl.validar_rango(1, 11)
        match opcion:
            case 1:
                nave_matriz = fn.crear_matriz(lista_a, lista_b, lista_c, lista_d)
            case 2:
                if vl.verificar_matriz_vacia(nave_matriz):
                    print(f"La cantidad de existencias son: {fn.contar_cantidad_elementos(nave_matriz)} tripulantes")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 3:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.recorrer_matriz_cxf(nave_matriz)
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 4:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.filtrar_matriz_segun_promedio(matriz=nave_matriz, indice_a_filtrar=2, dato_filtrar="n/a", modo="DES")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 5:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.filtrar_matriz_segun_promedio(matriz=nave_matriz, indice_a_filtrar=3, dato_filtrar="male", modo="ASC")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 6:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.filtrar_matriz_segun_promedio(matriz=nave_matriz, indice_a_filtrar=2, dato_filtrar="female", modo="DES")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 7:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.ordenar_matriz_segun_genero(matriz= nave_matriz, indice= 2, genero="female", modo= "DES")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 8:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.ordenar_matriz_segun_genero(matriz= nave_matriz, indice= 2, genero="male", modo= "ASC")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 9:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.ordenar_matriz_segun_genero(matriz= nave_matriz, indice= 2, genero="n/a", modo= "ASC")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 10:
                if vl.verificar_matriz_vacia(nave_matriz):
                    fn.trasponer_matriz_ordenada(matriz= nave_matriz, indice= 2, modo= "DES")
                else:
                    print("ERROR: Antes debe acceder a la opcion 1")
            case 11:
                print("Nos vemos!")
                corriendo = False