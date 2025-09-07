"""
📌 Desafío: Encuesta Tecnológica en UTN Technologies
UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo 
desarrollo en Python, con el objetivo de revolucionar el mercado.
Las tecnologías en evaluación son:
🔹 Inteligencia Artificial (IA)
🔹 Realidad Virtual/Aumentada (RV/RA)
🔹 Internet de las Cosas (IOT)
Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el 
propósito de analizar ciertas métricas.
🔹 Recolección de Datos
Cada empleado encuestado deberá proporcionar la siguiente información:
✔️ Nombre
✔️ Edad (debe ser 18 años o más)
✔️ Género (Masculino, Femenino, Otro)
✔️ Tecnología elegida (IA, RV/RA, IOT)
El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
🔹 Análisis de Datos
A partir de las respuestas, se deben calcular las siguientes métricas:
1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 
50 años (inclusive).
2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
Su género no sea Femenino 
Su edad está entre los 33 y 40 años.
3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


🔹 Requisitos del Programa
✔️ Los datos deben solicitarse y validarse correctamente.
✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
✔️ Presentar los resultados de manera clara y organizada.

"""

limite_datos = 3
datos_cargados = 0
cantidad_empleados = 0
empleados_contra_ia = 0
mayor_edad = None
nombre_mas_mayor = None
tecnologia_mas_mayor = None

while datos_cargados < limite_datos:
    nombre_ingresado = None
    while nombre_ingresado == None:
        nombre_ingresado = input("Ingrese su nombre: ")
    
    edad_ingresada = 0
    while (edad_ingresada < 18 or
        edad_ingresada > 90):
        edad_ingresada_str = input("Ingrese su edad: ")
        edad_ingresada = int(edad_ingresada_str)
        
    genero_ingresado = None
    while (genero_ingresado != "M" and
            genero_ingresado != "F" and
            genero_ingresado != "O"):
        genero_ingresado = input("Ingrese su genero [ M - F - O]: ")
        

    tecnologia_ingresada = None
    while(tecnologia_ingresada != "IA" and
        tecnologia_ingresada != "RV/RA" and
        tecnologia_ingresada != "IOT"):
        tecnologia_ingresada = input("Ingrese una tecnologia [IA - RV/RA - IOT] : ")
        
    # Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 
    # 50 años (inclusive).
    if (genero_ingresado == "M" and
    (tecnologia_ingresada == "IA" or tecnologia_ingresada == "IOT") and
    (edad_ingresada >= 25 and edad_ingresada <=50)):
        cantidad_empleados += 1
        
    #Porcentaje de empleados que NO votaron por IA, siempre y cuando:
    #Su género no sea Femenino 
    #Su edad está entre los 33 y 40 años.
    
    if (tecnologia_ingresada != "IA" and
        genero_ingresado != "F" and
        (edad_ingresada >= 33 and edad_ingresada <= 40)):
        empleados_contra_ia += 1
        
    #Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.
    if (genero_ingresado == "M" and
        (mayor_edad == None or mayor_edad < edad_ingresada)):
        nombre_mas_mayor = nombre_ingresado
        tecnologia_mas_mayor = tecnologia_ingresada
        
    datos_cargados += 1
    

porcentaje = (empleados_contra_ia / datos_cargados) *100
    

mensaje =\
    f"""
        #1. La cantidad de empleados es: {cantidad_empleados}
        #2. El porcentaje de empleados que no votaron IA {porcentaje}
        #3. El empleado mas mayor es {nombre_mas_mayor} con la tecnologia {tecnologia_mas_mayor}
    """
print(mensaje)