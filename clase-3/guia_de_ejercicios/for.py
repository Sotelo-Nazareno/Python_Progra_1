#                               For

# 1.  Mostrar los números ascendentes desde el 1 al 10
inicio_bucle = 1
final_bucle = 10 + 1

for numero in range(inicio_bucle,final_bucle,1):
    print(numero)


# 2.  Mostrar los números descendentes desde el 10 al 1
inicio_bucle = 10
final_bucle = 0

for numero in range(inicio_bucle,final_bucle,-1):
    print(numero)

# 3. Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero_str = input("Ingrese hasta que numero quiere ver: ")
limite_bucle = int(numero_str) + 1

for numero in range(limite_bucle):
    print(numero)


"""
# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

	5 x 0 = 0
	5 x 1  = 5
	5 x 2 = 10
	5 x 3  = 15 …

"""

numero_str = input("Ingrese el numero a multiplicar: ")
numero_multiplicar = int(numero_str)

for numero in range(11):
    multiplicacion = numero_multiplicar * numero
    cuenta_progresiva = f"{numero_multiplicar} x {numero} = {multiplicacion}"
    print(cuenta_progresiva)


# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

numeros_a_ingresar = 10
sumatoria = 0
salir = False

for numero in range(numeros_a_ingresar):
    numero_str = input("Ingrese un numero: ")
    numero_int = int(numero_str)

    if numero_int > 0:
        sumatoria += numero_int
    else:
        salir = True
        break

if salir:
    cuenta_progresiva = f"La suma de los numeros ingresados es: {sumatoria} con el promedio de {sumatoria / numero}"
else:
    cuenta_progresiva = f"La suma de los numeros ingresados es: {sumatoria} con el promedio de {sumatoria / (numero + 1)}"
print(cuenta_progresiva)


# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10.
inicio_bucle = 1
final_bucle = 11

for numero in range(inicio_bucle,final_bucle,1):
    resultado = 3 * numero
    print(resultado)


# 7. Mostrar los números pares que hay desde la unidad hasta el número 50.

numero_ingresado = input("Ingrese el numero de inicio: ")
numero_ingresado_int = int(numero_ingresado)

final_bucle = 51

for posible_par in range(numero_ingresado_int,final_bucle,1):
    if posible_par % 2 == 0:
        print(posible_par)
    

# 8. Realizar un programa que permita mostrar una pirámide de números. 
#Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

numero_piramide_str = input("Ingrese el largo y ancho de la piramide: ")
numero_piramide_int = int(numero_piramide_str) + 1

for numero in range(1,numero_piramide_int,1):
    cuenta_progresiva = " "
    numero_progresivo = 1
    while numero_progresivo <= numero:
        cuenta_progresiva += str(numero_progresivo)
        numero_progresivo += 1
    print(cuenta_progresiva)


# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

numero_ingresado_str = input("Ingrese un numero: ")
numero_ingresado_int = int(numero_ingresado_str)

for posible_divisor in range(1,numero_ingresado_int + 1,1):
    if numero_ingresado_int % posible_divisor == 0:
        mensaje = f"El numero {posible_divisor} es divisor de {numero_ingresado_int}"
        print(mensaje)


# 10. Ingresar un número. Determinar si el número es primo o no.

numero_ingresado_str = input("Ingrese un numero: ")
numero_ingresado_int = int(numero_ingresado_str)
cantidad_divisores = 2

for posible_primo in range(2,numero_ingresado_int,1):
    if numero_ingresado_int % posible_divisor == 0:
        cantidad_divisores += 1

if cantidad_divisores > 2:
    mensaje = f"El numero {numero_ingresado_int} NO es un numero primo"
else:
    mensaje = f"El numero {numero_ingresado_int} Es un numero primo"

print(mensaje)


# 11. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
numero_ingresado_str = input("Ingrese un numero: ")
numero_ingresado_int = int(numero_ingresado_str)
cantidad_numeros_primos = 0

for posible_primo in range(2,numero_ingresado_int,1):
    cantidad_divisores = 1
    for numero in range(1,posible_primo,1):
        if posible_primo % numero == 0:
            cantidad_divisores += 1

    if cantidad_divisores == 2:
        cantidad_numeros_primos += 1
        print(posible_primo)

mensaje =f"Se encontraron {cantidad_numeros_primos} numeros primos"
print(mensaje)

