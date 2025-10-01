import funciones as fn
import validaciones as val
import os

def pokedex(lista_ids, lista_nombres, lista_tipos, lista_poderes, lista_condiciones)->None:
    """
    Realizas diferentes informes de pokemons vistos por el usuario

    :params:

    :returns:
    Devuelve la opcion elegida por el usuario
    """


    corriendo = True
    matriz_pokedex = []

    while corriendo:

        print\
            (f"""
                [1] Crear una matriz en la pokedex
                [2] Mostrar cantidad de pokemon en la pokedex
                [3] Mostrar informacion de cada pokemon
                [4] Mostrar informacion de los Pokémons que superen el promedio de poder
                [5] Mostrar todos los Pokémons cuyo tipo sea fuego
                [6] Mostrar todos los Pokémons cuyo tipo sea electrico
                [7] Ordenar la matriz según poder DES los Pokémons que sean legendarios
                [8] Ordenar la matriz según poder ASC los Pokémons que sean normales
                [9] Trasponer la matriz y mostrar su información prolija con una función que acepte ese tipo de matriz
                [10] Salir
            """)
        
        opcion = str(val.validar_rango(1, 10))

        match opcion:
            case "1":
                matriz_pokedex = fn.crear_matriz(lista_ids, lista_nombres, lista_tipos, lista_poderes, lista_condiciones)
                print("Tu pokedex esta lista!")
            case "2":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.mostrar_cantidad_pokemons(matriz=matriz_pokedex)
            case "3":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.recorrer_matriz_cxf(matriz=matriz_pokedex)
            case "4":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.mostrar_mas_fuertes(matriz=matriz_pokedex)
            case "5":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.mostrar_poekmons_tipo(matriz=matriz_pokedex, tipo="fuego")
            case "6":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.mostrar_poekmons_tipo(matriz=matriz_pokedex, tipo="eléctrico")
            case "7":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.ordenar_matriz(matriz=matriz_pokedex, indice_a_ordenar=3, modo="DESC", condicion="legendario")
            case "8":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.ordenar_matriz(matriz=matriz_pokedex, indice_a_ordenar=3, modo="ASC", condicion="normal")
            case "9":
                if val.validar_matriz_con_elementos(matriz=matriz_pokedex):
                    fn.recorrer_matriz_cxf(matriz=matriz_pokedex)
            case "10":
                print("Nos vemos pronto!")
                corriendo = False
        
        os.system('pause')
        os.system('cls')
