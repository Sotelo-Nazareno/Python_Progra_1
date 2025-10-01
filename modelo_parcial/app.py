import funciones as fn
import validaciones as vl

def aplicacion(lista_a:list, lista_b:list, lista_c:list, lista_d:list)->None:
    """
    Imprime por consola una aplicacion

    :params: lista_a(list) = La lista que ingrese el usuario
    :params: lista_b(list) = La lista que ingrese el usuario
    :params: lista_c(list) = La lista que ingrese el usuario
    :params: lista_d(list) = La lista que ingrese el usuario
    """

    corriendo = True
    matriz_datos = []
    mensaje_error = f"ERROR: Debe crear una matriz de datos(opcion[1]) antes de acceder a esta opcion"


    while corriendo:

        opciones= \
        """
            [1] Crear Matriz
            [2] Debes poder agregar un video a la matriz, los datos a incluir son: Titulo, Vistas, Likes, Duración.
            [3] Mostrar la cantidad de videos que hay en el set de datos.
            [4] Mostrar la cantidad de videos que contengan en su titulo “(En vivo…)”
            [5] Mostrar la cantidad de videos que contengan en su título: (Video Oficial)
            [6] Recorrer la matriz y mostrar la info (con una función que acepte ese tipo de matriz) con formato: nombre,vistas,likes,duración
            [7] Recorrer la matriz y mostrar la info (con una función que acepte ese tipo de matriz) con formato: nombre,vistas,likes,duración
                solamente de los videos que sean “En vivo…”
            [8] Determinar cuál o cuáles son los videos con mas vistas y mostrar sus datos, junto con la cantidad
            [25] Salir
        """

        print(opciones)

        eleccion = int(input("Ingrese una opcion: "))


        match eleccion:
            case 1:
                matriz_datos = fn.crear_matriz(lista_a, lista_b, lista_c, lista_d)
                print(matriz_datos)
            case 2:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    print(fn.agregar_video(matriz=matriz_datos))
                else:
                    print(mensaje_error)
            case 3:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    print(fn.cantidad_elementos(matriz=matriz_datos))
                else:
                    print(mensaje_error)
            case 4:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    print(fn.cantidad_videos_por_titulo(matriz=matriz_datos,tipo="titulo", frase= 'En Vivo'))
                else:
                    print(mensaje_error)
            case 5:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    print(fn.cantidad_videos_por_titulo(matriz=matriz_datos,tipo="titulo", frase= 'Video Oficial'))
                else:
                    print(mensaje_error)
            case 6:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    print(fn.recorrer_matriz_cxf(matriz=matriz_datos))
                else:
                    print(mensaje_error)
            case 7:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.buscar_elementos()
                else:
                    print(mensaje_error)
            case 8:
                if not(vl.verificar_matriz_vacia(matriz=matriz_datos)):
                    fn.recorrer_matriz_cxf(fn.filtrar_por_orden(matriz=matriz_datos, tipo="vistas", modo="mas"))
                else:
                    print(mensaje_error)
            case 25:
                print("Vuelva pronto!")
                corriendo = False