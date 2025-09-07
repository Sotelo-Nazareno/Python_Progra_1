#      WHILE
#   Validaciones

# 1. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
#    Tendrá intentos indeterminados.
clave_ingresada = None

while clave_ingresada != "clave":
    clave_ingresada = input("Ingrese la clave [clave]: ")


# 2. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. 
# Solo tendrá 3 intentos.
clave_ingresada = None
intentos = 0

while clave_ingresada != "clave":
    clave_ingresada = input("Ingrese la clave [clave]: ")
    intentos += 1
    
    if intentos == 3:
        break

# 3. Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
nota_ingresada = 0

while (nota_ingresada < 1 or
    nota_ingresada > 10):
    nota_ingresada_str = input("Ingrese una nota entre 1 y 10: ")
    nota_ingresada = int(nota_ingresada_str)
    

# 4. Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.
color_ingresado = None

while (color_ingresado != "Azul" and
    color_ingresado != "Rojo" and
    color_ingresado != "Verde"):
    color_ingresado = input("Igrese un color [Azul - Rojo - Verde ]: ")


#   Integrador Validaciones

"""
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, 
nos pide realizar la carga y validación de datos.

Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.

"""

tope_datos = 3
datos_cargados = 0


while datos_cargados < tope_datos:
    
    apellido_ingresado = None
    while apellido_ingresado == None:
        apellido_ingresado = input("Ingrese su apellido: ")
        
    edad_ingresada = 0
    
    while (edad_ingresada < 18 or
        edad_ingresada > 90):
        edad_ingresada_str = input("Ingrese su edad [+18]: ")
        edad_ingresada = int(edad_ingresada_str)
    
    estado_civil_ingresado = None
    while (estado_civil_ingresado != "Soltero" and
        estado_civil_ingresado != "Casado" and
        estado_civil_ingresado != "Divorciado" and
        estado_civil_ingresado != "Viudo"):
        estado_civil_ingresado = input("Ingrese su estado civil [ Soltero - Casado - Divorciado - Viudo]: ")
        
    numero_legajo_ingresado = 0
    while numero_legajo_ingresado < 1000:
        numero_legajo_ingresado_str = input("Ingrese su numero de legajo: ")
        numero_legajo_ingresado = int(numero_legajo_ingresado_str)
    
    mensaje =\
        f"""
            Apellido: {apellido_ingresado}
            Edad: {edad_ingresada}
            Estado Civil: {estado_civil_ingresado}
            Numero Legajo: {numero_legajo_ingresado}
        """
    print(mensaje)