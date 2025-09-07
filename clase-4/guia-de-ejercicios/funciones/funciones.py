#                               Funciones

import math

# 1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def ingresar_numero()->int:
    """
    Solicita al ususario que ingrese un numero
    
    :params: 
    Tipo texto
    
    :return:
    Devuelve un numero previamente ingresado por el usuario
    
    """
    numero_usuario_str = input("Ingrese un numero: ")
    numero_usuario_int = int(numero_usuario_str)
    return(numero_usuario_int)

# 2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def ingresar_numero_flotante()-> float:
    """
    Solicita al usuario un numero flotante
    
    :params:
    
    :return:
    Devuelve el numero flotante ingresado
    """
    numero_usuario_str = input("Ingrese un numero flotante: ")
    numero_usuario_float = float(numero_usuario_str)
    return(numero_usuario_float)


# 3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def ingresar_texto()->str:
    """
    Solicita al usuario el ingreso de una cadena caracteres
    
    :params:
    texto: Espera un argumento de tipo string
    
    :return:
    Retorna la cadena de strings previamente ingresada por el usuario
    """
    cadena_ingresada = input("Ingrese una cadena de caracteres: ")
    return(cadena_ingresada)

# 4. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

def calcular_area_rectangulo(base:float, altura:float)->float:
    """
    Calcula el area de un rectangulo

    :params: base: - La base del rectangulo
    :params: altura - La altura del rectangulo

    :returns:
        Devuelve el area del rectangulo de las medidas previamente ingresadas por el ususario
    """
    area = base * altura
    return(area)

# 5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def calcular_area_circulo(radio:float)->float:
    """
    Calcula el area de un circulo

    :params: radio - El radio del circulo

    :returns:
        Devuelve el area del circulo con las medidas ingresadas
    """
    area = math.pi * radio ** 2
    return(area)

# 6. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def verificar_par_o_impar(numero:int)->str:
    """
    Verifica si el numero ingresado por el usuario es un numero par o impar

    :params: numero- El numero ingresado por el usuario en formato string

    :returns:
        Devuelve el resultado de si su numero es par o impar
    """
    mensaje = " "
    par = f"El numero {numero} es par"
    impar = f"El numero {numero} es impar"
    if numero % 2 == 0:
        mensaje = par
    else:
        mensaje = impar
    return(mensaje)

# 7. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def verificar_par(numero:int)->bool:
    """
    Verifica si el numero ingresado es un numero par

    :params: numero - El numero ingresado por el usuario

    :returns:
        Devuelve si el numero ingresado es par 
    """
    return(numero % 2 == 0)

# 8. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def encontrar_maximo_terna(numero_a:int, numero_b: int, numero_c:int)->int:
    """
    Define cual es el numero maximo entre los tres numeros ingresados

    :params: numero_a - Numero ingresado por el usuario
    :params: numero_b - Numero ingresado por el usuario
    :params: numero_c - Numero ingresado por el usuario

    :retunrs:
        Devuelve el numero maximo entre los tres ingresados
    """
    maximo_numero = 0
    if (numero_a > numero_b and numero_a > numero_c):
        maximo_numero = numero_b
    elif numero_b > numero_c:
        maximo_numero = numero_b
    else: 
        maximo_numero = numero_c
    
    return(maximo_numero)

# 9. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def calcular_potencia(base:int, exponente:int)->int:
    """
    Calcula la potencia del numero por el exponente ingresado del usuario

    :params: base - El numero ingresado por el usuario
    :params: exponente - El numero ingresado por el usuario

    :returns:
        Devuelve el resultado de potencia del numero ingresado por el usuario
    """

    potencia = base ** exponente
    return(potencia)

# 10. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def verificar_primo(numero:int):
    """
    Verifica si el numero ingresado por el usuario es primo

    :params: numero - El numero ingresado por el usuario

    :return: 
        Devuelve si el numero ingresado por el usuario es primo
    """
    if numero < 2:
        mensaje = f"SYSTEM ERROR - El numero a ingresar debe ser mayor a 1"
    else:
        cantidad_divisibles = 2 

        for posible_divisible in range(2,numero):
            if numero % posible_divisible == 0:
                cantidad_divisibles += 1
                break
        mensaje = cantidad_divisibles == 2
    return(mensaje)

# 11. Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre la unidad y un número 
# ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

def encontrar_numeros_primos(user_number:int)->int:
    """
        Muestra la cantidad de todos los numeros primos que se encuntra bajo el rango del numero ingresado

        :params: user_number = Numero ingresado por el usuario

        :returns:
            Devuelve la cantidad de numeros primos encontrados
    """
    cantidad_de_primos = 0
    for posible_primo in range(user_number,1,-1):
        if verificar_primo(posible_primo):
            cantidad_de_primos += 1
    return(cantidad_de_primos)



# 12. Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

def imprimir_tabla_mult(numero_user:int, numero_inicio:int = 1,numero_fin:int = 10)->None:
    """
    Imprime la tabla de multiplicar de un numero ingresado por el usuario

    :params: numero = El numero ingresado por el usuario el cual sera multiplicado
    :params: numero_inicio = Rango inicial de la multiplicacion ingresado por el usuario 
    :params: numero_fin = Rango final de la multiplicacion ingresado por el usuario

    :returns:
        No devuelve nada
    """

    inicio_bucle = numero_inicio
    fin_bucle = numero_fin + 1

    for multiplicador in range(inicio_bucle, fin_bucle):
        resultado = numero_user * multiplicador
        mensaje = f"{numero_user} X {multiplicador} = {resultado}"
        print(mensaje)


# 13. Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
def ingresar_tipo(tipo):
    """
    Solicita al usuario un tipo de elemento
    
    :params: tipo = El tipo que debe de ingresar el usuario
    
    :return:
    Devuelve el elemento ingresado con el tipo deseado
    """
    elemento_str = None

    while elemento_str == None:
        elemento_str = input(f"Ingrese un tipo {tipo}: ")

    elemento = tipo(elemento_str)
    return(elemento)