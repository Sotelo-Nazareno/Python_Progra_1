# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales

def sumar_naturales(numero: int)->int:
    """
    Suma los numeros natural dentro del rango asignado

    :params: numero = El rango ingresado del usuario

    :returns:
    Devuelve la suma de todos los numeros dentro del rango del numero ingresado
    """
    if numero == 0:
        return 0
    
    anterior = numero - 1
    sumatoria = numero + sumar_naturales(anterior)
    return(sumatoria)

# 2. Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base: int, exponente: int)->int:
    """
    Calcula la potencia ingresada de un numero ingresado

    :params: base = Numero ingresado por el ususario
    :params: exponente = Numero ingresado por el ususario

    :returns:
    Devuelve la potencia del numero ingresado
    """

    if exponente == 0:
        return 1
    
    potencia = base * calcular_potencia(base, exponente -1)
    return(potencia)

# 3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

#def sumar_digitos(numero: int)->int:
    """
    Suma los digitos de un numero

    :params: numero = El numero ingresado por el usuario

    :returns:
    Devuelve el resultado de haber sumado oos digitos de un numero
    """
    

# 4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola.

def calcular_fibonacci(numero: int)->int:
    """
    Calcula la sucesion de fibonacci desde el numero ingresado

    :params: numero = El numero desde donde comenzara la funcion

    :returns:
    Devuelve la sucesion de fibonacci
    """

    if numero == 0 or numero == 1:
        return numero
    
    fibo = calcular_fibonacci(numero-1) + calcular_fibonacci(numero-2)
    return(fibo)