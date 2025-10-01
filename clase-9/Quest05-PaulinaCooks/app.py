import funciones as fn
import validaciones as vl

def aplicacion(lista_a:list, lista_b:list, lista_c:list)->None:
    """
    Imprime por consola una aplicacion

    :params: lista_a(list) = La lista que ingrese el usuario
    :params: lista_b(list) = La lista que ingrese el usuario
    :params: lista_c(list) = La lista que ingrese el usuario
    """

    corriendo = True
    matriz_datos = []
    mensaje_error = f"ERROR: Debe crear una matriz de datos(opcion[1]) antes de acceder a esta opcion"


    while corriendo:

        opciones= \
        """
            [1] Crear Matriz
            [2] Mostrar la cantidad de videos que hay en el set de datos.
            [3] Recorrer la matriz y mostrar la info con formato: nombre,vistas,duraciones
            [4] Recorrer la matriz y mostrar la info  con formato: nombre,vistas,duraciones solamente de los videos que tengan al menos un hashtag (“#”) en su nombre
            [5] Determinar cuál o cuáles son los videos con mas vistas y mostrar sus datos, junto con la cantidad
            [6] Determinar cual o cuales son los videos mas cortos de tiempo y mostrar sus datos, junto con la duración.
            [7] Buscar y mostrar la info de los videos que no superen el promedio de vistas.
            [8] Filtrar/buscar en la matriz todos los videos que superen el promedio de vistas y mostrarlos.
            [9] Filtrar/buscar en la matriz todos los videos que no superen el promedio de vistas y al mismo tiempo que no superen el promedio de duración.
            [10] Calcular el promedio de duración y vistas de los videos.
            [11] Solamente de los videos que tengan al menos un hashtag en su título, mostrar la info completa de los que superen el promedio de vistas entre esos videos.
            [12] Ordenar la matriz según vistas DES
            [13] Ordenar la matriz según duración ASC
            [14] Ordenar la matriz según nombres ASC
            [15] Trasponer la matriz y mostrar su información prolija con una función que acepte ese tipo de matriz, además debe estar ordenada por Likes DES.
            [16] Salir

        """

        print(opciones)

        eleccion = int(input("Ingrese una opcion: "))


        match eleccion:
            case 1:
                matriz_datos = fn.crear_matriz(lista_a, lista_b, lista_c)
                print(matriz_datos)
            case 2:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    print(fn.cantidad_filas(matriz=matriz_datos))
                else:
                    print(mensaje_error)
            case 3:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    print(fn.recorrer_matriz_cxf(matriz=matriz_datos))
                else:
                    print(mensaje_error)
            case 4:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.filtrar_matriz(matriz=matriz_datos, indice="nombre" , digito="#"))
                else:
                    print(mensaje_error)
            case 5:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.filtrar_por_orden(matriz=matriz_datos,indice="vistas", modo="ASC")
                else:
                    print(mensaje_error)
            case 6:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.filtrar_por_orden(matriz=matriz_datos, indice="duracion", modo="DES")
                else:
                    print(mensaje_error)
            case 7:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.filtrar_por_promedio(matriz=matriz_datos, fila="vistas", modo="menor"))
                else:
                    print(mensaje_error)
            case 8:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.filtrar_por_promedio(matriz=matriz_datos, fila="vistas", modo="mayor"))
                else:
                    print(mensaje_error)
            case 9:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.filtrar_por_promedio (matriz=(fn.filtrar_por_promedio(matriz=matriz_datos, fila="vistas", modo="menor")),fila="duracion", modo="menor"))
                else:
                    print(mensaje_error)
            case 10:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    promedio_videos = f"El promedio de vistas es los videos es de: {fn.promedio_de_elementos(matriz=matriz_datos, fila="vistas")}"
                    promedio_duracion = f"El promedio de duracion de los videos es de: {fn.promedio_de_elementos(matriz=matriz_datos,fila="duracion")}"
                    print(promedio_videos)
                    print(promedio_duracion)
                else:
                    print(mensaje_error)
            case 11:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.filtrar_por_promedio(matriz=(fn.filtrar_matriz(matriz=matriz_datos, indice="nombre" , digito="#")), fila="vistas", modo="mayor"))
                else:
                    print(mensaje_error)
            case 12:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.ordenar_matriz(matriz=matriz_datos, tipo="vistas", modo="DES"))
                else:
                    print(mensaje_error)
            case 13:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.ordenar_matriz(matriz=matriz_datos, tipo="duracion", modo="ASC"))
                else:
                    print(mensaje_error)
            case 14:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.ordenar_matriz(matriz=matriz_datos, tipo="nombre", modo="ASC"))
                else:
                    print(mensaje_error)
            case 16:
                print("Vuelva pronto!")
                corriendo = False