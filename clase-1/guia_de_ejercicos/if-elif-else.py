#  --             IF - ELSE -ELIF               --

"""
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
  * Menos de 160 cm: Base
  * Entre 160 cm y 179 cm: Escolta
  * Entre 180 cm y 199 cm: Alero
  * 200 cm o más: Ala-Pívot o Pívot
"""

altura = input("Ingrese su altura: ")
altura_cms = float(altura)

if altura_cms < 1.60:
    mensaje = f"El jugador con {altura}cm estara en la posicion de Base"
elif altura_cms < 1.80:
    mensaje = f"El jugador con {altura}cm estara en la posicion de Escolta"
elif altura_cms < 2.00:
    mensaje = f"El jugador con {altura}cm estara en la posicion de Alero"
else:
    mensaje = f"El jugador con {altura}cm estara en la posicion de Ala-pivot o Pivot"

print(mensaje)

""""""""""""""""""

"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...
"""

nota = input("Ingrese su nota: ")
nota_int = int(nota)

if nota_int < 4:
    devolucion = f"Desaprobado, la nota es {nota}"
elif nota_int < 6:
    devolucion = f"Aprobado, la nota es {nota}"
else:
    devolucion = f"Promocion directa, la nota es {nota}"


print(devolucion)