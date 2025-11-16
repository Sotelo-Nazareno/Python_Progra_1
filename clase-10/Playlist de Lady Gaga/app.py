import funciones_impresas as fni
import funciones_ordenadoras as fno
import funciones as fn

def mostrar_menu(songs:list[dict[str, str]])->None:
    """
    Crea un menu de opciones

    Args:
        songs (list[dict[str, str]]): La lista del ususario
    """

    playlist = []
    corriendo = True

    while corriendo:
        fni.mostrar_opciones()
        seleccion = input("Ingrese una opcion: ")

        match seleccion:
            case "1":
                playlist = fn.normalizar_datos(songs)
                print(playlist)
            case "2":
                fni.mostrar_duracion(playlist)
            case "3":
                fni.mostrar_duracion(fno.ordenar_quick_temas(playlist, "Duracion", "DESC"))
            case "4":
                fn. mostrar_promedio(playlist, "Vistas")
            case "5":
                fni.mostrar_informacion(fn.buscar_max_min(playlist, "Vistas", "max"))
            case "6":
                fni.mostrar_informacion(fn.buscar_max_min(playlist, "Vistas", "min"))
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case "10":
                print("Nos vemos!")
                corriendo = False