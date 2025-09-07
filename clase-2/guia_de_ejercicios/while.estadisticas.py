#                               WHILE
#           Contadores - Acumuladores - Máximos y mínimos


# 1.  Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
inicio_bucle = 1
fin_bucle = 10

while inicio_bucle <= fin_bucle:
    print(inicio_bucle)
    inicio_bucle += 1


# 2.  Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
inicio_bucle = 10
fin_bucle = 1

while inicio_bucle >= fin_bucle:
    print(inicio_bucle)
    inicio_bucle -= 1

# 3.  Mostrar la suma de los números desde el 1 hasta el 10.
inicio_bucle = 1
fin_bucle = 10
sumatoria = 0

while inicio_bucle <= fin_bucle:
    sumatoria += inicio_bucle
    inicio_bucle += 1

print(sumatoria)


# 4.  Mostrar la suma de los números pares desde el 1 hasta el 10.
inicio_bucle = 1
fin_bucle = 10
sumatoria = 0

while inicio_bucle <= fin_bucle:
    if inicio_bucle % 2 == 0:
        sumatoria += inicio_bucle
    inicio_bucle += 1

print(sumatoria)

# 5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
# 5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.
tope_datos = 5
datos_a_cargar = 0
sumatoria = 0

while datos_a_cargar < tope_datos:
    numero_ingresado_str = input("Ingrese un numero: ")
    numero_ingresado_int = int(numero_ingresado_str)
    sumatoria += numero_ingresado_int
    datos_a_cargar += 1

mensaje = f"L a suma de los 5 numeros ingresados es {sumatoria} y su promedio es: {sumatoria/datos_a_cargar}"    
print(mensaje)
    
# 6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos

quiere_ingresar_numero = True
datos_cargados = 0
sumatoria = 0

while quiere_ingresar_numero:
    numero_ingresado_str = input("Ingrese un numero: ")
    numero_ingresado_int = int(numero_ingresado_str)
    sumatoria += numero_ingresado_int
    quiere_ingresar_numero_str = input("Quiere ingresar otro numero? [s/n]: ")
    
    if quiere_ingresar_numero_str == "n":
        quiere_ingresar_numero = False
        
    datos_cargados += 1

mensaje = f"La suma de todos los numeros ingresados es {sumatoria} y el promedio {sumatoria/datos_cargados}"
print(mensaje)


# 7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos

quiere_ingresar_numero = True
sumatoria = 0
producto = 1

while quiere_ingresar_numero:
    numero_ingresado_str = input("Ingrese un numero: ")
    numero_ingresado_int = int(numero_ingresado_str)
    
    if numero_ingresado_int > 0:
        sumatoria += numero_ingresado_int
    else:
        producto *= numero_ingresado_int
        
    quiere_ingresar_numero_str = input("Quiere ingresar otro numero? [s/n]: ")
    
    if quiere_ingresar_numero_str == "n":
        quiere_ingresar_numero = False
    
        
mensaje =\
    f"""
        # La suma de los numeros positivos es: {sumatoria}
        # El producto de los numeros negativos es: {producto}
    """
print(mensaje)

# 8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.
tope_datos = 10
datos_cargados = 0
maximo_numero = None
minimo_numero = None

while datos_cargados < tope_datos:
    numero_ingresado_str = input("Ingrese un numero: ")
    numero_ingresado_int = int(numero_ingresado_str)
    
    if maximo_numero == None or maximo_numero < numero_ingresado_int:
        maximo_numero = numero_ingresado_int
        
    if minimo_numero == None or minimo_numero > numero_ingresado_int:
        minimo_numero = numero_ingresado_int
        
    datos_cargados += 1
        
mensaje =\
    f"""
    # El maximo numero ingresado fue: {maximo_numero}
    # El minimo numero ingresado fue: {minimo_numero}
    """
print(mensaje)

#   Anexo:

# 9. Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.

quiere_ingresar_numero = True
sumatoria = 0
datos_cargados = 0

while quiere_ingresar_numero:
    numero_ingresado_str = input("Ingrese un numero: ")
    numero_ingresado_int = int(numero_ingresado_str)
    sumatoria += numero_ingresado_int
    datos_cargados += 1
    
    if datos_cargados > 4:
        quiere_ingresar_numero_str = input("Quiere seguir ingresando numeros [s/n]: ")
        if quiere_ingresar_numero_str == "n":
            quiere_ingresar_numero = False
            
mensaje =\
    f"""
        # La suma de los numeros ingresados es {sumatoria} y el promedio es {sumatoria / datos_cargados}
    """
print(mensaje)
    
    
# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos.
quiere_ingresar_numero = True
sumatoria = 0
datos_cargados = 0

while quiere_ingresar_numero:
    numero_ingresado_str = input("Ingrese un numero: ")
    numero_ingresado_int = int(numero_ingresado_str)
    sumatoria += numero_ingresado_int
    datos_cargados += 1
    
    if datos_cargados == 10:
        break
    elif datos_cargados > 4:
        quiere_ingresar_numero_str = input("Quiere seguir ingresando numeros [s/n]: ")
        if quiere_ingresar_numero_str == "n":
            quiere_ingresar_numero = False
            
mensaje =\
    f"""
        # La suma de los numeros ingresados es {sumatoria} y el promedio es {sumatoria / datos_cargados}
    """
print(mensaje)


#   Integrador While

# Realizar un programa que permita que el usuario ingrese todos los números que desee. 
# Una vez finalizada la carga determinar:
    #La suma acumulada de los números negativos.
    #La suma acumulada de los números positivos.
    #La cantidad de números negativos ingresados.
    #El promedio de los números positivos.
    #El número positivo más grande.
    #El porcentaje de números negativos ingresados, respecto del total de ingresos.  
    
quiere_ingresar_numero = True
sumatoria_positivos = 0
sumatoria_negativa = 0
contador_numeros_negativos = 0
contador_numeros_positivos = 0
mayor_numero = None 
total_numeros_ingresados = 0


while quiere_ingresar_numero:
    numero_ingresado_str = input("Ingrese un numero: ")
    numero_ingresado_int = int(numero_ingresado_str)
    
    if numero_ingresado_int > 0:
        contador_numeros_positivos += 1
        sumatoria_positivos += numero_ingresado_int
    else:
        contador_numeros_negativos += 1
        sumatoria_negativa += numero_ingresado_int
        

    if mayor_numero == None or mayor_numero < numero_ingresado_int:
        mayor_numero = numero_ingresado_int
        
    quiere_ingresar_numero_str = input("Quiere continuar ingresando numeros? [s/n]: ")
    if quiere_ingresar_numero_str == "n":
        quiere_ingresar_numero = False
    
    total_numeros_ingresados += 1
        
promedio_numeros_positivos = sumatoria_positivos / contador_numeros_positivos

mensaje =\
    f"""
        #1. La suma acumulada de los numeros positivos es {sumatoria_positivos}
        #2. La suma acumulada de los numeros negativos es {sumatoria_negativa}
        #3. La cantidad de numeros negativos es {contador_numeros_negativos}
        #4. El promedio de los numeros positivos es {promedio_numeros_positivos}
        #5. El numero positivo mas grande es {mayor_numero}
        #6. El porcentaje de numeros negativos respecto de total ingresado es: {contador_numeros_negativos/total_numeros_ingresados}
    """
print(mensaje)